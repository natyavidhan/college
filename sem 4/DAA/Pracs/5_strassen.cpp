#include <bits/stdc++.h>
using namespace std;

typedef vector<vector<int>> Matrix;

Matrix addMatrices(const Matrix& A, const Matrix& B) {
    int n = A.size();
    Matrix C(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
    return C;
}

Matrix subtractMatrices(const Matrix& A, const Matrix& B) {
    int n = A.size();
    Matrix C(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] - B[i][j];
    return C;
}

Matrix getSubmatrix(const Matrix& M, int row, int col, int size) {
    Matrix sub(size, vector<int>(size));
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            sub[i][j] = M[row + i][col + j];
    return sub;
}

void setSubmatrix(Matrix& M, int row, int col, const Matrix& sub) {
    int size = sub.size();
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            M[row + i][col + j] = sub[i][j];
}

Matrix strassen(const Matrix& A, const Matrix& B) {
    int n = A.size();
    
    if (n == 1) {
        return {{A[0][0] * B[0][0]}};
    }
    
    int half = n / 2;
    
    Matrix A11 = getSubmatrix(A, 0, 0, half);
    Matrix A12 = getSubmatrix(A, 0, half, half);
    Matrix A21 = getSubmatrix(A, half, 0, half);
    Matrix A22 = getSubmatrix(A, half, half, half);
    
    Matrix B11 = getSubmatrix(B, 0, 0, half);
    Matrix B12 = getSubmatrix(B, 0, half, half);
    Matrix B21 = getSubmatrix(B, half, 0, half);
    Matrix B22 = getSubmatrix(B, half, half, half);
    
    Matrix M1 = strassen(addMatrices(A11, A22), addMatrices(B11, B22));
    Matrix M2 = strassen(addMatrices(A21, A22), B11);
    Matrix M3 = strassen(A11, subtractMatrices(B12, B22));
    Matrix M4 = strassen(A22, subtractMatrices(B21, B11));
    Matrix M5 = strassen(addMatrices(A11, A12), B22);
    Matrix M6 = strassen(subtractMatrices(A21, A11), addMatrices(B11, B12));
    Matrix M7 = strassen(subtractMatrices(A12, A22), addMatrices(B21, B22));
    
    Matrix C11 = addMatrices(subtractMatrices(addMatrices(M1, M4), M5), M7);
    Matrix C12 = addMatrices(M3, M5);
    Matrix C21 = addMatrices(M2, M4);
    Matrix C22 = addMatrices(subtractMatrices(addMatrices(M1, M3), M2), M6);
    
    Matrix C(n, vector<int>(n));
    setSubmatrix(C, 0, 0, C11);
    setSubmatrix(C, 0, half, C12);
    setSubmatrix(C, half, 0, C21);
    setSubmatrix(C, half, half, C22);
    
    return C;
}

void printMatrix(const Matrix& M) {
    for (const auto& row : M) {
        for (int val : row)
            cout << val << " ";
        cout << endl;
    }
}

int main() {
    cout << "=== STRASSEN'S MATRIX MULTIPLICATION ===" << endl << endl;
    
    // Test Case 1: 2x2 matrices
    cout << "Test Case 1: 2x2 Matrices" << endl;
    Matrix A1 = {{1, 2}, {3, 4}};
    Matrix B1 = {{5, 6}, {7, 8}};
    
    cout << "Matrix A:" << endl;
    printMatrix(A1);
    cout << "Matrix B:" << endl;
    printMatrix(B1);
    
    Matrix C1 = strassen(A1, B1);
    cout << "Result (A * B):" << endl;
    printMatrix(C1);
    cout << endl;
    
    // Test Case 2: 4x4 matrices
    cout << "Test Case 2: 4x4 Matrices" << endl;
    Matrix A2 = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    Matrix B2 = {{1, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}};
    
    cout << "Matrix A:" << endl;
    printMatrix(A2);
    cout << "Matrix B (Identity):" << endl;
    printMatrix(B2);
    
    Matrix C2 = strassen(A2, B2);
    cout << "Result (A * B):" << endl;
    printMatrix(C2);
    
    return 0;
}

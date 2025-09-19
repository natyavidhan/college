#include <iostream>
using namespace std;

// Function to create a dynamically allocated 2D array
int** createMatrix(int rows, int cols) {
    int **mat = new int*[rows];
    for(int i = 0; i < rows; i++)
        mat[i] = new int[cols];
    return mat;
}

// Function to input elements into the matrix
void inputMatrix(int **mat, int rows, int cols) {
    cout << "Enter matrix elements:\n";
    for(int i = 0; i < rows; i++)
        for(int j = 0; j < cols; j++)
            cin >> mat[i][j];
}

// Function to print the matrix
void printMatrix(int **mat, int rows, int cols) {
    cout << "Matrix:\n";
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++)
            cout << mat[i][j] << " ";
        cout << endl;
    }
}

// Function to add two matrices
void addMatrices(int **mat1, int **mat2, int rows, int cols) {
    int **result = createMatrix(rows, cols);
    for(int i = 0; i < rows; i++)
        for(int j = 0; j < cols; j++)
            result[i][j] = mat1[i][j] + mat2[i][j];
    cout << "Addition Result:\n";
    printMatrix(result, rows, cols);
    for(int i = 0; i < rows; i++)
        delete[] result[i];
    delete[] result;
}

// Function to multiply two matrices
void multiplyMatrices(int **mat1, int r1, int c1, int **mat2, int r2, int c2) {
    if(c1 != r2) {
        cout << "Multiplication not possible due to dimension mismatch!\n";
        return;
    }
    int **result = createMatrix(r1, c2);
    for(int i = 0; i < r1; i++) {
        for(int j = 0; j < c2; j++) {
            result[i][j] = 0;
            for(int k = 0; k < c1; k++)
                result[i][j] += mat1[i][k] * mat2[k][j];
        }
    }
    cout << "Multiplication Result:\n";
    printMatrix(result, r1, c2);
    for(int i = 0; i < r1; i++)
        delete[] result[i];
    delete[] result;
}

// Function to compute the transpose of a matrix
void transposeMatrix(int **mat, int rows, int cols) {
    int **result = createMatrix(cols, rows);
    for(int i = 0; i < rows; i++)
        for(int j = 0; j < cols; j++)
            result[j][i] = mat[i][j];
    cout << "Transpose of the matrix:\n";
    printMatrix(result, cols, rows);
    for(int i = 0; i < cols; i++)
        delete[] result[i];
    delete[] result;
}

// Function to delete the matrix and free memory
void deleteMatrix(int **mat, int rows) {
    for(int i = 0; i < rows; i++)
        delete[] mat[i];
    delete[] mat;
}

int main() {
    int choice;
    while (true) {
        cout << "\nMenu:\n";
        cout << "1. Add two matrices\n";
        cout << "2. Multiply two matrices\n";
        cout << "3. Transpose a matrix\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 4)
            break;

        if (choice == 1) {
            int rows, cols;
            cout << "Enter number of rows and columns: ";
            cin >> rows >> cols;
            int **mat1 = createMatrix(rows, cols);
            int **mat2 = createMatrix(rows, cols);
            cout << "Enter elements of first matrix:\n";
            inputMatrix(mat1, rows, cols);
            cout << "Enter elements of second matrix:\n";
            inputMatrix(mat2, rows, cols);
            addMatrices(mat1, mat2, rows, cols);
            deleteMatrix(mat1, rows);
            deleteMatrix(mat2, rows);
        } else if (choice == 2) {
            int r1, c1, r2, c2;
            cout << "Enter rows and columns of first matrix: ";
            cin >> r1 >> c1;
            cout << "Enter rows and columns of second matrix: ";
            cin >> r2 >> c2;
            int **mat1 = createMatrix(r1, c1);
            int **mat2 = createMatrix(r2, c2);
            cout << "Enter elements of first matrix:\n";
            inputMatrix(mat1, r1, c1);
            cout << "Enter elements of second matrix:\n";
            inputMatrix(mat2, r2, c2);
            multiplyMatrices(mat1, r1, c1, mat2, r2, c2);
            deleteMatrix(mat1, r1);
            deleteMatrix(mat2, r2);
        } else if (choice == 3) {
            int rows, cols;
            cout << "Enter number of rows and columns: ";
            cin >> rows >> cols;
            int **mat = createMatrix(rows, cols);
            cout << "Enter elements of the matrix:\n";
            inputMatrix(mat, rows, cols);
            transposeMatrix(mat, rows, cols);
            deleteMatrix(mat, rows);
        } else {
            cout << "Invalid choice!\n";
        }
    }
    cout << "Program exited.\n";
    return 0;
}

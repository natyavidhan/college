#include <iostream>

using namespace std;

#define MAX 100

template <class T> class Stack {
private:
    int top;
    T arr[MAX];
public:
    Stack() {
        top = -1;
    }

    void push(T x) {
        if (isFull()) {
            cout << "Stack Overflow\n";
            return;
        }
        arr[++top] = x;
    }

    void pop() {
        if (isEmpty()) {
            cout << "Stack Underflow\n";
            return;
        }
        top--;
    }

    T topElemet() {
        if (isEmpty()) {
            cout << "Stack is empty\n";
            return T();
        }
        return arr[top];
    }

    bool isFull() {
        return top >= MAX - 1;
    }

    bool isEmpty() {
        return top < 0;
    }

};
#include <iostream>
using namespace std;

class Node{
    int data;
    Node* next;

    Node(int d){
        data = d;
        next = nullptr;
    }
    friend class Stack;
    friend class Queue;
};
class Stack{
    Node* top;
public:
    Stack() {
        top = 0;
    }
    public:
    void push(Node* p){
        if(!top) {
            top = p;
            return;
        }
        p->next = top;
        top=p;
    }
    Node* pop(){
        Node* temp = top;
        top=top->next;
        temp->next = nullptr;
        return temp;
    }
    bool is_empty(){
        if(!top) return true;
        else return false;
    }
    void print() {
        Node *p = top;
        while (p) {
            cout << p->data << "<-";
            p = p->next;
        }
        cout << endl;
        return;
    }
    friend class Queue;
};

class Queue{
    Stack *s1;
    Stack *s2;
public:
    Queue() {
        s1 = new Stack();
        s2 = new Stack();
    }
    void enqueue(int value){
        Node* p = new Node(value);
        s1->push(p);
    }
    void dequeue(){
        Node* p = s1->pop();
        while(!s1->is_empty()){
            s2->push(p);
            p=s1->pop();
        }
        while(!s2->is_empty()){
            s1->push(s2->pop());
        }
        return;
    }
    void print() {
        Node *p = s1->top;
        while (p) {
            cout << p->data << "<-";
            p = p->next;
        }
        cout << endl;
        return;
    }

};

int main() {
    Queue q;
    q.enqueue(5);
    q.enqueue(6);
    q.enqueue(7);
    q.enqueue(8);
    q.print();
    q.dequeue();
    q.print();
    return 0;
}
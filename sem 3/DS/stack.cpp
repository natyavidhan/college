// Push():
// Pop():
// Peek()
// isEmpty()
// size()
// clear()
// search()

#include <iostream>

using namespace std;

class Node {
    int val;
    Node *next;
public:
    Node(int v = 0, Node *n = 0) {
        val = v;
        next = n;
    };
    friend class Stack;
};

class Stack {
    Node *head;
    int cap;
public:
    Stack() {
        head = 0;
        cap = 0;
    };
    void push(int val) {
        Node *p;
        p = new Node(val);
        if (!head) {
            head = p;
        } else {
            Node *q;
            q = head;
            head = p;
            head->next = q;
        };
        cap++;
        return;
    };

    void pop() {
        if (head) {
            Node *q;
            q = head;
            head = head->next;
            delete(q);
            cap--;
        }
        return;
    }

    int peek() {
        return head->val;
    }

    bool isEmpty() {
        return head == 0;
    }

    int size() {
        return cap;
    }

    void clear() {
        head = 0;
        return;
    }

    int search(int v) {
        Node *q;
        q = head;
        int n;
        while (q->next) {
            if (q->val == v) {
                return n;
            }
            q =  q->next;
            n++;
        }
        return -1;
    }
};

int main() {
    Stack s;
    s.push(5);
    s.push(6);
    s.push(7);
    s.push(8);
    cout << s.peek() << endl;
    s.pop();
    cout << s.peek() << endl;
    cout << s.search(6) << endl;
    return 0;
}
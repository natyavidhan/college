#include <iostream>
#include <string>
using namespace std;

class Node {
public:
    int val;
    Node* next;

    Node(int v = 0) : val(v), next(0) {};
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
        // free all nodes and reset size
        while (head) {
            Node* t = head;
            head = head->next;
            delete t;
        }
        cap = 0;
        return;
    }

    int search(int v) {
        Node *q = head;
        int n = 0;
        while (q) {
            if (q->val == v) return n;
            q = q->next;
            n++;
        }
        return -1;
    }

    void print() {
        Node *q = head;
        while (q) {
            cout << q->val;
            q = q->next;
        }
        cout << endl;
        return;
    }
};

int main() {
    string a, b;
    cin >> a >> b;

    Stack *s1 = new Stack;
    Stack *s2 = new Stack;
    Stack *sr = new Stack;

    for (size_t i = 0; i < a.size(); ++i) {
        if (a[i] >= '0' && a[i] <= '9') s1->push(a[i] - '0');
    }
    for (size_t i = 0; i < b.size(); ++i) {
        if (b[i] >= '0' && b[i] <= '9') s2->push(b[i] - '0');
    }

    int carry = 0;
    while (!s1->isEmpty() || !s2->isEmpty() || carry) {
        int x = 0, y = 0;
        if (!s1->isEmpty()) { x = s1->peek(); s1->pop(); }
        if (!s2->isEmpty()) { y = s2->peek(); s2->pop(); }
        int sum = x + y + carry;
        sr->push(sum % 10);
        carry = sum / 10;
    }

    sr->print();
    return 0;
}
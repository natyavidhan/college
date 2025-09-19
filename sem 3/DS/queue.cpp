// Enqueue
// Dequue
// Peeke
// IsEmpty
// Size
// Clear


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
    friend class Queue;
};

class Queue {
    Node *head;
    int cap;
public:
    Queue() {
        head = 0;
        cap = 0;
    };
    void enqueue(int val) {
        Node *p;
        p = new Node(val);
        if (!head) {
            head = p;
        } else {
            Node *q;
            q = head;
            while (q->next) {
                q = q->next;
            }
            q->next = p;
        };
        cap++;
        return;
    };

    void dequeue() {
        if (head) {
            Node *q;
            q = head;
            while (q->next->next) {
                q = q->next;
            }
            q->next = 0;
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
    Queue s;
    s.enqueue(5);
    s.enqueue(6);
    s.enqueue(7);
    s.enqueue(8);
    cout << s.peek() << endl;
    s.dequeue();
    cout << s.peek() << endl;
    cout << s.search(6) << endl;
    return 0;
}
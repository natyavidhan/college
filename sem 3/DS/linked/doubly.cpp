#include <iostream>

using namespace std;

class Node {
    Node *prev;
    Node *next;
    int val;
public:
    Node(int v = 0, Node *p = 0, Node *n = 0) {
        prev = p;
        next = n;
        val = v;
    };
    friend class DoublyLL;
};

class DoublyLL {
    Node *head;
    Node *tail;
public:
    DoublyLL(Node *h = 0, Node *t = 0) {
        head = h;
        tail = t;
    }


    bool isempty() {
        return head == 0;
    }

    void print() {
        Node *p;
        p = head;
        while (p)
        {
            cout << p->val;
            if (p->next) {
                cout << " <-> ";
            }
            p = p->next;
        }
        cout << "\n";
        return;
    }

    void add_start(int val) {
        Node *p;
        p = new Node(val);
        if (!head) {
            head = tail = p;
        } else {
            Node *q;
            q = head;
            head = p;
            head->next = q;
            q->prev = head;
        }
        return;
    }

    void add_end(int val) {
        Node *p;
        p = new Node(val);
        if (!tail) {
            tail = head = p;
        } else {
            Node *q;
            q = tail;
            tail = p;
            tail->prev = q;
            q->next = tail;
        }
        return;
    }

    void add_ith(int val, int i) {
        Node *p;
        p = new Node(val);
        int n = 0;
        Node *q;
        q = head;
        while (n < i-1) {
            q = q->next;
            n++;
        }
        p->next = q->next;
        p->prev = q;
        q->next = p;
        p->next->prev = p;
        return;
    }

    void delete_start() {
        Node *p;
        p = head;
        head = head->next;
        if (!head) {
            tail = 0;
        }
        delete(p);
        return;
    }

    void delete_end() {
        if (!tail) {
            return;
        }
        Node *p = tail;
        tail = tail->prev;
        if (!tail) {
            head = 0;
        } else {
            tail->next = 0;
        }
        delete p;
        return;
    }

    void delete_ith(int i) {
        int n = 0;
        Node *q;
        q = head;
        while (n < i-1) {
            q = q->next;
            n++;
        }
        q->next = q->next->next;
        q->next->prev = q;
        return;
    }

    int search(int val) {
        Node *curr = head;
        int index = 0;
        while (curr) {
            if (curr->val == val) {
                return index;
            }
            curr = curr->next;
            index++;
        }
        return -1;
    }

    void reverse() {
        if (!head || !head->next) {
            return;
        }
        Node *curr = head;
        while (curr) {
            Node *nextNode = curr->next;
            curr->next = curr->prev;
            curr->prev = nextNode;
            curr = nextNode;
        }
        Node *oldHead = head;
        head = tail;
        tail = oldHead;
    }
};



int main() {
    DoublyLL list;
    list.add_start(10);
    list.add_end(20);
    list.add_end(30);
    list.add_ith(25, 2);

    cout << "Initial list: ";
    list.print();

    int idx25 = list.search(25);
    cout << "Search 25: " << (idx25 != -1 ? "Found at index " + to_string(idx25) : "Not found") << "\n";
    int idx99 = list.search(99);
    cout << "Search 99: " << (idx99 != -1 ? "Found at index " + to_string(idx99) : "Not found") << "\n";

    list.delete_ith(1);
    cout << "After deleting position 1: ";
    list.print();

    list.delete_start();
    cout << "After deleting start: ";
    list.print();

    list.delete_end();
    cout << "After deleting end: ";
    list.print();

    list.add_start(5);
    list.add_end(40);
    cout << "After new insertions: ";
    list.print();

    list.reverse();
    cout << "After reversing: ";
    list.print();

    return 0;
}
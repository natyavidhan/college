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
        Node *p;
        p = tail;
        tail = tail->prev;
        if (!tail) {
            head = 0;
        }
        delete(p);
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
};



int main() {
    DoublyLL list;
    int nums[10] = {1, 3, 5, 7, 9, 2, 4, 6, 8, 0};
    for (int i=0; i<10; i++) {
        list.add_end(nums[i]);
    }
    list.add_ith(69, 2);

    list.delete_start();
    list.delete_end();
    list.delete_ith(2);
    
    list.print();
    return 0;
}
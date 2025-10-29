#include <iostream>

using namespace std;

class Node{
    int val;
    Node *next;
public:
    Node(int v) : val(v), next(0) {}
    friend class LinkedList;
};

class LinkedList {
    Node *head;
public:
    LinkedList() : head(0) {}
    void insert_end(int v) {
        Node *p, *q;
        p = new Node(v);
        if (!head) {
            head = p;
            return;
        }
        q = head;
        while (q->next)
        {
            q = q->next;
        }
        q->next = p;
        return;
    }

    void delete_end() {
        Node *p, *q;
        q = head;
        while (q->next->next)
        {
            q = q->next;
        }
        p = q->next;
        q->next = 0;
        delete(q);
        return;
    }

    int length(Node *n = 0) {
        if (!n) n = head;
        if (!n) return 0;
        if (!n->next) {
            return 1;
        }
        return 1 + length(n->next);
    }
};

int main() {
    LinkedList LL;
    int nums[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
    for (int i=0; i<10; i++) {
        LL.insert_end(nums[i]);
    }
    cout << LL.length() << endl;
    return 0;
}
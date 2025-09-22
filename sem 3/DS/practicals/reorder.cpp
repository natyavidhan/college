#include <iostream>
using namespace std;

class Node {
    int value;
    Node *next;
public:
    Node(int val=0, Node *n=0) {
        value = val;
        next = n;
    }
    int getValue() { return value; }
    friend class LinkedList;
};

class LinkedList {
    Node *head;
public:
    LinkedList() {
        head = 0;
    }

    void add_end(int val) {
        Node *p;
        p = new Node(val);
        if (head == 0) {
            head = p;
            return;
        } 
        Node *q;
        q = head;
        while (q->next)
        {
            q = q->next;
        }
        q->next = p;
        return;
    }
        void reorder_odd_even() {
        if (!head || !head->next) return;

        Node* oddHead = 0;
        Node* oddTail = 0;
        Node* evenHead = 0;
        Node* evenTail = 0;

        Node* current = head;

        while (current) {
            Node* nextNode = current->next;
            current->next = 0;

            if (current->value % 2 != 0) {
                if (!oddHead) {
                    oddHead = oddTail = current;
                } else {
                    oddTail->next = current;
                    oddTail = current;
                }
            } else {
                if (!evenHead) {
                    evenHead = evenTail = current;
                } else {
                    evenTail->next = current;
                    evenTail = current;
                }
            }

            current = nextNode;
        }
        if (oddTail) {
            oddTail->next = evenHead;
            head = oddHead;
        } else {
            head = evenHead;
        }
    }
    void print() {
        Node *p;
        p = head;
        while (p)
        {
            cout << p->value;
            if (p->next) {
                cout << " -> ";
            }
            p = p->next;
        }
        cout << "\n";
        return;
    }
};

int main() {
    LinkedList list;
    int nums[8] = {1, 4, 3, 6, 5, 8, 7, 2};
    for (int i = 0; i < 8; i++) {
        list.add_end(nums[i]);
    }

    cout << "Original list: ";
    list.print();

    list.reorder_odd_even();

    cout << "Reordered list: ";
    list.print();

    return 0;
}

#include <iostream>
using namespace std;

class Node {
public:
    int value;
    Node* next;
    Node(int val = 0, Node* n = 0) {
        value = val;
        next = n;
    }
};

class LinkedList {
    Node* head;
public:
    LinkedList() { head = 0; }

    void add_end(int val) {
        Node* p = new Node(val);
        if (!head) {
            head = p;
            return;
        }
        Node* q = head;
        while (q->next) q = q->next;
        q->next = p;
    }

    void print() {
        Node* p = head;
        while (p) {
            cout << p->value;
            if (p->next) cout << " -> ";
            p = p->next;
        }
        cout << "\n";
    }

    // Delete all nodes at odd positions (1-based)
    void delete_odd_positions() {
        if (!head) return;

        Node* current = head;
        Node* prev = 0;
        int pos = 1;

        while (current) {
            Node* nextNode = current->next;

            if (pos % 2 != 0) {
                if (prev) {
                    prev->next = nextNode;
                } else {
                    head = nextNode;
                }
                delete current;
            } else {
                prev = current;
            }

            current = nextNode;
            pos++;
        }
    }
};


int main() {
    LinkedList list;
    int nums[] = {1, 2, 3, 4, 5, 6, 7};
    for (int i = 0; i < 7; i++) {
        list.add_end(nums[i]);
    }

    cout << "Original list: ";
    list.print();

    list.delete_odd_positions();

    cout << "After deleting odd positions: ";
    list.print();

    return 0;
}

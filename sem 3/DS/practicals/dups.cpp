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
    Node* head;
public:
    LinkedList() { head = 0; }

    void add_end(int val) {
        Node* p = new Node(val);
        if (!head) { head = p; return; }
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

    void bubbleSort() {
        if (!head || !head->next) return;

        bool swapped;
        Node* ptr1;
        Node* lptr = 0;

        do {
            swapped = false;
            ptr1 = head;

            while (ptr1->next != lptr) {
                if (ptr1->value > ptr1->next->value) {
                    swap(ptr1->value, ptr1->next->value);
                    swapped = true;
                }
                ptr1 = ptr1->next;
            }
            lptr = ptr1;
        } while (swapped);
    }

    void removeDuplicatesSorted() {
        Node* current = head;
        while (current && current->next) {
            if (current->value == current->next->value) {
                Node* temp = current->next;
                current->next = temp->next;
                delete temp;
            } else {
                current = current->next;
            }
        }
    }
};

int main() {
    LinkedList list;
    int nums[] = {4, 2, 3, 2, 5, 3, 1, 4};
    for (int i = 0; i < 8; i++) {
        list.add_end(nums[i]);
    }

    cout << "Original list: ";
    list.print();

    list.bubbleSort();
    cout << "Sorted list: ";
    list.print();

    list.removeDuplicatesSorted();
    cout << "After removing duplicates: ";
    list.print();

    return 0;
}

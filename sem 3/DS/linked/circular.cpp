#include <iostream>

using namespace std;

class Node {
    int val;
    Node *next;
public:
    Node(int v = 0, Node *n = 0) : val(v), next(n) {}
    friend class CircularLL;
};

class CircularLL {
    Node *cursor;
public:
    CircularLL(Node *c = 0) : cursor(c) {}

    bool isempty() {
        return cursor == 0;
    }

    void insert_after_cursor(int val) {
        Node *p = new Node(val);
        if (!cursor) {
            p->next = p;
            cursor = p;
        } else {
            p->next = cursor->next;
            cursor->next = p;
            cursor = p;
        }
    }

    Node* search(int val) {
        if (!cursor) {
            return 0;
        }
        Node *start = cursor->next;
        Node *curr = start;
        do {
            if (curr->val == val) {
                return curr;
            }
            curr = curr->next;
        } while (curr != start);
        return 0;
    }

    void remove(int val) {
        if (!cursor) {
            return;
        }
        Node *prev = cursor;
        Node *curr = cursor->next;
        do {
            if (curr->val == val) {
                prev->next = curr->next;
                if (curr == cursor) {
                    cursor = (curr == curr->next) ? 0 : prev;
                }
                delete curr;
                return;
            }
            prev = curr;
            curr = curr->next;
        } while (curr != cursor->next);
    }

    void display() {
        if (!cursor) {
            cout << "(empty)\n";
            return;
        }
        Node *start = cursor->next;
        Node *curr = start;
        do {
            cout << curr->val;
            curr = curr->next;
            if (curr != start) {
                cout << " -> ";
            }
        } while (curr != start);
        cout << "\n";
    }
};

int main() {
    CircularLL list;
    list.insert_after_cursor(10);
    list.insert_after_cursor(20);
    list.insert_after_cursor(30);

    cout << "List after insertions: ";
    list.display();

    Node *found = list.search(20);
    cout << (found ? "Found 20\n" : "20 not found\n");

    list.remove(20);
    cout << "After removing 20: ";
    list.display();

    list.remove(99);
    cout << "After attempting to remove 99: ";
    list.display();

    list.insert_after_cursor(40);
    cout << "After inserting 40: ";
    list.display();

    return 0;
}

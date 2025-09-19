#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};
void insert_at_beginning(Node*& head, int x) {
    Node* newNode = new Node{x, head};
    head = newNode;
}
void insert_at_position(Node*& head, int x, int pos) {
    if (pos <= 1 || head == nullptr) {
        insert_at_beginning(head, x);
        return;
    }
    Node* temp = head;
    for (int i = 1; temp != nullptr && i < pos - 1; i++) {
        temp = temp->next;
    }
    if (temp == nullptr) {
        cout << "Position out of range.\n";
        return;
    }
    Node* newNode = new Node{x, temp->next};
    temp->next = newNode;
}
void insert_at_end(Node*& head, int x) {
    Node* newNode = new Node{x, nullptr};
    if (!head) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next) temp = temp->next;
    temp->next = newNode;
}
void remove_beginning(Node*& head) {
    if (!head) {
        cout << "List is empty.\n";
        return;
    }
    Node* temp = head;
    head = head->next;
    delete temp;
}
void remove_at_position(Node*& head, int pos) {
    if (!head) {
        cout << "List is empty.\n";
        return;
    }
    if (pos == 1) {
        remove_beginning(head);
        return;
    }
    Node* temp = head;
    for (int i = 1; temp && i < pos - 1; i++) {
        temp = temp->next;
    }
    if (!temp || !temp->next) {
        cout << "Position out of range.\n";
        return;
    }
    Node* del = temp->next;
    temp->next = temp->next->next;
    delete del;
}
void remove_end(Node*& head) {
    if (!head) {
        cout << "List is empty.\n";
        return;
    }
    if (!head->next) {
        delete head;
        head = nullptr;
        return;
    }
    Node* temp = head;
    while (temp->next->next) temp = temp->next;
    delete temp->next;
    temp->next = nullptr;
}
Node* search(Node* head, int x) {
    Node* temp = head;
    while (temp) {
        if (temp->data == x) return temp;
        temp = temp->next;
    }
    return nullptr;
}
void reverse_list(Node*& head) {
    Node* prev = nullptr;
    Node* curr = head;
    while (curr) {
        Node* nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }
    head = prev;
}
void insert_ordered(Node*& head, int x) {
    Node* newNode = new Node{x, nullptr};
    if (!head || head->data >= x) {
        newNode->next = head;
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next && temp->next->data < x) {
        temp = temp->next;
    }
    newNode->next = temp->next;
    temp->next = newNode;
}
Node* merge_lists(Node* head1, Node* head2) {
    Node* result = nullptr;
    Node* temp1 = head1;
    Node* temp2 = head2;
    while (temp1) {
        insert_ordered(result, temp1->data);
        temp1 = temp1->next;
    }
    while (temp2) {
        insert_ordered(result, temp2->data);
        temp2 = temp2->next;
    }
    return result;
}
void print_list(Node* head) {
    cout << "List: ";
    Node* temp = head;
    while (temp) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL\n";
}

int main() {
    Node* head = nullptr;
    int choice, x, pos;

    while (true) {
        cout << "\n=== MENU ===\n";
        cout << "1. Insert at beginning\n";
        cout << "2. Insert at ith position\n";
        cout << "3. Insert at end\n";
        cout << "4. Remove from beginning\n";
        cout << "5. Remove from ith position\n";
        cout << "6. Remove from end\n";
        cout << "7. Search element\n";
        cout << "8. Reverse list\n";
        cout << "9. Insert in ordered list\n";
        cout << "10. Merge two lists\n";
        cout << "11. Print list\n";
        cout << "12. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter element: ";
            cin >> x;
            insert_at_beginning(head, x);
        } else if (choice == 2) {
            cout << "Enter element and position: ";
            cin >> x >> pos;
            insert_at_position(head, x, pos);
        } else if (choice == 3) {
            cout << "Enter element: ";
            cin >> x;
            insert_at_end(head, x);
        } else if (choice == 4) {
            remove_beginning(head);
        } else if (choice == 5) {
            cout << "Enter position: ";
            cin >> pos;
            remove_at_position(head, pos);
        } else if (choice == 6) {
            remove_end(head);
        } else if (choice == 7) {
            cout << "Enter element to search: ";
            cin >> x;
            if (search(head, x))
                cout << "Element " << x << " found.\n";
            else
                cout << "Element not found.\n";
        } else if (choice == 8) {
            reverse_list(head);
            cout << "List reversed.\n";
        } else if (choice == 9) {
            cout << "Enter element: ";
            cin >> x;
            insert_ordered(head, x);
        } else if (choice == 10) {
            Node* head2 = nullptr;
            int n, val;
            cout << "Enter number of elements for 2nd list: ";
            cin >> n;
            cout << "Enter elements:\n";
            for (int i = 0; i < n; i++) {
                cin >> val;
                insert_ordered(head2, val);
            }
            Node* merged = merge_lists(head, head2);
            cout << "Merged Ordered List:\n";
            print_list(merged);
        } else if (choice == 11) {
            print_list(head);
        } else if (choice == 12) {
            cout << "Exiting program...\n";
            break;
        } else {
            cout << "Invalid choice! Try again.\n";
        }
    }

    return 0;
}


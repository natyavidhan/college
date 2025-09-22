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

    Node* get_ith_from_end(int i) {
        Node *main_ptr = head;
        Node *ref_ptr = head;

        int count = 0;
        if (head != 0) {
            while (count < i) {
                if (ref_ptr == 0) {
                    cout << i << " is greater than the number of nodes in list\n";
                    return 0;
                }
                ref_ptr = ref_ptr->next;
                count++;
            }

            while (ref_ptr != 0) {
                main_ptr = main_ptr->next;
                ref_ptr = ref_ptr->next;
            }
        }
        return main_ptr;
    }
};

int main() {
    LinkedList list;
    int nums[10] = {1, 3, 5, 7, 9, 2, 4, 6, 8, 0};
    for (int i = 0; i < 10; i++) {
        list.add_end(nums[i]);
    }

    int i = 3;
    Node* node = list.get_ith_from_end(i);
    if (node)
        cout << "The " << i << "th node from the end has value: " << node->getValue() << endl;
    else
        cout << "Index out of bounds." << endl;

    return 0;
}

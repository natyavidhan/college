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
    friend class LinkedList;
};

class LinkedList {
    Node *head;
public:
    LinkedList() {
        head = 0;
    }

    bool isempty() {
        return head == 0;
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

    void add_start(int val) {
        Node *p;
        p = new Node(val);
        if (head == 0) {
            head = p;
            return;
        } 
        p->next = head;
        head = p;
        return;
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

    void add_ith(int val, int i) {
        Node *p;
        p = new Node(val);
        if (head == 0) {
            head = p;
            return;
        } 
        Node *q;
        q = head;
        int j = 0;
        while (j<i-1)
        {
            q = q->next;
            j++;
        }
        p->next = q->next;
        q->next = p;
        return;
    }

    void delete_start(){
        Node *p;
        p = head;
        head = head->next;
        delete(p);
        return;
    }

    void delete_end(){
        Node *p;
        p = head;
        while (p->next->next)
        {
            p = p->next;
        }
        Node *q;
        q = p->next;
        p->next = 0;
        delete(q);
        return;
    }

    void delete_ith(int i){
        Node *p;
        p = head;
        int j = 0;
        while (j < i-1)
        {
            p = p->next;
            j++;
        }
        Node *q;
        q = p->next;
        p->next = q->next;
        delete(q);
    }

    void reverse() {
        Node *p;
        Node *q;
        Node *r;
        p = head;
        q = p->next;
        r = q->next;
        p->next = 0;
        while (r)
        {
            q->next = p;
            p = q;
            q = r;
            r = r->next;
        }
        q->next = p;
        head = q;
        return;
    }

    int search(int val) {
        Node *q;
        q = head;
        int j = 0;
        while (q) {
            if (q->value == val) 
                return j;
            q = q->next;
            j++;
        }
        return -1;
        
    }

    void concat(LinkedList ll) {
        Node *q;
        q = head;
        while (q->next)
        {
            q = q->next;
        }
        q->next = ll.head;
        return;
    }

    LinkedList merge(LinkedList ll) {
        LinkedList new_list;
        Node *h1;
        Node *h2;
        h1 = head;
        h2 = ll.head;
        while (h1 && h2) {
            if (h1->value < h2->value) {
                new_list.add_end(h1->value);
                h1 = h1->next;
            } else {
                new_list.add_end(h2->value);
                h2 = h2->next;
            }
        }
        Node *val;
        if (h1) {
            val = h1;
        } else {
            val = h2;
        }
        Node *p;
        while (p->next)
        {
            p = p->next;
        }
        p->next = val;
        return new_list;
    }
};

int main() {
    LinkedList list;
    int nums[10] = {1, 3, 5, 7, 9, 2, 4, 6, 8, 0};
    for (int i=0; i<10; i++) {
        list.add_end(nums[i]);
    }
    list.add_ith(69, 2);

    list.delete_start();
    list.delete_end();
    list.delete_ith(2);
    
    list.print();
    
    list.reverse();
    list.print();
    
    cout << list.search(7) << endl;
    
    LinkedList list2;
    int nums2[5] = {2, 4, 6, 8, 10};
    for (int i = 0; i < 5; i++)
    {
        list2.add_end(nums2[i]);
    }
    list2.print();
    // list.concat(list2);
    // list.print();
    LinkedList new_list;
    new_list = list.merge(list2);
    new_list.print();
    return 0;
}
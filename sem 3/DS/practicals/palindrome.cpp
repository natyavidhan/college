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

    Node* reverseList(Node* node) {
        Node* prev = 0;
        Node* curr = node;
        while (curr) {
            Node* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }
        return prev;
    }

    bool isPalindrome() {
        if (!head || !head->next) return true;

        Node* slow = head;
        Node* fast = head;

        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        Node* secondHalf = reverseList(slow->next);

        Node* p1 = head;
        Node* p2 = secondHalf;
        bool result = true;
        while (p2) {
            if (p1->value != p2->value) {
                result = false;
                break;
            }
            p1 = p1->next;
            p2 = p2->next;
        }

        slow->next = reverseList(secondHalf);

        return result;
    }
};

bool isPalindromeArray(int arr[], int n) {
    int left = 0, right = n - 1;
    while (left < right) {
        if (arr[left] != arr[right])
            return false;
        left++;
        right--;
    }
    return true;
}

int main() {

    int nums[] = {1, 2, 3, 2, 1};
    int nums2[] = {1, 2, 3, 4, 5};
    int n = 5;

    // ----- Array Palindrome -----
    cout << "Array 1 palindrome? " << (isPalindromeArray(nums, n) ? "Yes" : "No") << "\n";
    cout << "Array 1 elements: ";
    for (int i = 0; i < n; i++) {
        cout << nums[i] << " ";
    }
    cout << "\n";
    cout << "Array 2 palindrome? " << (isPalindromeArray(nums2, n) ? "Yes" : "No") << "\n";
    cout << "Array 2 elements: ";
    for (int i = 0; i < n; i++) {
        cout << nums2[i] << " ";
    }
    cout << "\n\n";

    // ----- Linked List Palindrome -----
    LinkedList list;
    for (int i = 0; i < n; i++) {
        list.add_end(nums[i]);
    }
    LinkedList list2;
    for (int i = 0; i < n; i++) {
        list2.add_end(nums2[i]);
    }

    cout << "Linked List 1 palindrome? " << (list.isPalindrome() ? "Yes" : "No") << "\n";
    list.print();
    cout << "Linked List 2 palindrome? " << (list2.isPalindrome() ? "Yes" : "No") << "\n";
    list2.print();

    return 0;
}

#include <iostream>
#include <iomanip>

using namespace std;

class ArrayQueue {
    static const int MAX = 32;
    int data[MAX];
    int frontIdx;
    int rearIdx;
    int count;
public:
    ArrayQueue() : frontIdx(0), rearIdx(0), count(0) {}

    bool isEmpty() const {
        return count == 0;
    }

    bool isFull() const {
        return count == MAX;
    }

    void enqueue(int val) {
        if (isFull()) {
            cout << "ArrayQueue overflow\n";
            return;
        }
        data[rearIdx] = val;
        rearIdx = (rearIdx + 1) % MAX;
        count++;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "ArrayQueue underflow\n";
            return;
        }
        frontIdx = (frontIdx + 1) % MAX;
        count--;
    }

    int peek() const {
        return isEmpty() ? 0 : data[frontIdx];
    }

    int size() const {
        return count;
    }

    void clear() {
        frontIdx = rearIdx = count = 0;
    }

    int search(int val) const {
        if (isEmpty()) {
            return -1;
        }
        for (int i = 0; i < count; ++i) {
            int idx = (frontIdx + i) % MAX;
            if (data[idx] == val) {
                return i;
            }
        }
        return -1;
    }
};

class Node {
    int val;
    Node *next;
public:
    Node(int v = 0, Node *n = 0) : val(v), next(n) {}
    friend class CircularListQueue;
};

class CircularListQueue {
    Node *tail;
    int count;
public:
    CircularListQueue(Node *t = 0, int c = 0) : tail(t), count(c) {}

    bool isEmpty() const {
        return tail == 0;
    }

    void enqueue(int val) {
        Node *node = new Node(val);
        if (!tail) {
            node->next = node;
            tail = node;
        } else {
            node->next = tail->next;
            tail->next = node;
            tail = node;
        }
        count++;
    }

    void dequeue() {
        if (!tail) {
            cout << "CircularListQueue underflow\n";
            return;
        }
        Node *head = tail->next;
        if (head == tail) {
            tail = 0;
        } else {
            tail->next = head->next;
        }
        delete head;
        count--;
    }

    int peek() const {
        return tail ? tail->next->val : 0;
    }

    int size() const {
        return count;
    }

    void clear() {
        while (!isEmpty()) {
            dequeue();
        }
    }

    int search(int val) const {
        if (!tail) {
            return -1;
        }
        Node *head = tail->next;
        Node *curr = head;
        int idx = 0;
        do {
            if (curr->val == val) {
                return idx;
            }
            curr = curr->next;
            idx++;
        } while (curr != head);
        return -1;
    }
};

void printQueueState(const char *label, int frontVal, int size, int pos) {
    cout << left << setw(28) << label
         << " front=" << frontVal
         << " size=" << size
         << " searchPos=" << pos << "\n";
}

int main() {
    ArrayQueue aq;
    CircularListQueue cq;

    for (int v : {10, 20, 30}) {
        aq.enqueue(v);
        cq.enqueue(v);
    }

    printQueueState("Initial state", aq.peek(), aq.size(), aq.search(20));
    printQueueState("Initial state (CLL)", cq.peek(), cq.size(), cq.search(20));

    aq.dequeue();
    cq.dequeue();
    printQueueState("After one dequeue", aq.peek(), aq.size(), aq.search(30));
    printQueueState("After one dequeue (CLL)", cq.peek(), cq.size(), cq.search(30));

    aq.enqueue(40);
    cq.enqueue(40);
    printQueueState("After enqueue 40", aq.peek(), aq.size(), aq.search(40));
    printQueueState("After enqueue 40 (CLL)", cq.peek(), cq.size(), cq.search(40));

    aq.clear();
    cq.clear();
    printQueueState("After clear", aq.peek(), aq.size(), aq.search(10));
    printQueueState("After clear (CLL)", cq.peek(), cq.size(), cq.search(10));

    return 0;
}
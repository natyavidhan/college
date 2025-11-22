class Node {
    int val;
    Node *next;
public:
    Node(int v) {
        val = v;
        next = 0;
    };
    friend class Stack;
    friend class Queue;
};


class Stack {
    Node *top;
public:
    Stack() {
        top = 0;
    }
    void push(Node *q) {
        // Node *q = new Node(v);
        if (!top) {
            top = q;
            return;
        }
        q->next = top;
        top = q;
        return;
    };
    Node *pop() {
        Node *q = top;
        top = top->next;
        int v = q->val;
        return q;
    };
    bool is_empty() {
        return top == 0;
    }
    Node *head() {
        return top;
    }
};

class Queue {
    Stack *main;
    Stack *temp;
public:
    void enqueue(int v) {
        Node *q = new Node(v);
        main->push(q);
    };
    void dequeue() {
        Node *p = main->pop();
        while (!main->is_empty()) {
            temp->push(p);
            p = main->pop();
        }
        delete(p);
        while (!temp->is_empty()) {
            main->push(temp->pop());
        }
        return;
    }
};
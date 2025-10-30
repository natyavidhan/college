#include <iostream>

using namespace std;

template<typename T>
class QueueNode {
    T val;
    QueueNode *next;
public:
    QueueNode(T v): val(v), next(0) {}
    template <typename u>
    friend class Queue;
};

template<typename T>
class Queue {
    QueueNode<T> *head;
public:
    Queue(): head(0) {}
    bool empty() const {return head == 0;}
    void enqueue(T v) {
        QueueNode<T> *p;
        p = new QueueNode<T>(v);
        if (!head) {
            head = p;
            return;
        }
        QueueNode<T> *q = head;
        while (q->next) {
            q = q->next;
        }
        q->next = p;
        return;
    }

    T dequeue() {
        if (!head) return T();
        QueueNode<T> *p = head;
        head = head->next;
        T val = p->val;
        delete(p);
        return val;
    }
};

template <typename T>
class Node {
    T val;
    Node *left;
    Node *right;
public:
    Node(T v): val(v), left(0), right(0) {}

    template <typename U>
    friend class BST;
};

template <typename T>
class BST {
    Node<T> *head;
public:
    BST(): head(0) {};
    void insert(T v) {
        Node<T> *p;
        p = new Node<T>(v);
        if (!head) {
            head = p;
            return;
        }
        Node<T> *q = head;
        while (true) {
            if (v < q->val) {
                if (!q->left) {
                    q->left = p;
                    return;
                } else {
                    q = q->left;
                }
            } else {
                if (!q->right) {
                    q->right = p;
                    return;
                } else {
                    q = q->right;
                }
            }
        }
    }

    void remove(T v) {
        if (!head) return;
        Node<T> *q = head;
        Node<T> *prev = 0;
        while (true) {
            if (q->val == v) {
                break;
            }
            prev = q;
            if (v < q->val && q->left) {
                q = q->left;
            } else if (v > q->val && q->right) {
                q = q->right;
            } else {
                cout << "Not Found" << endl;
                return;
            }
        }
        if (!q->left && !q->right) {
            if (!prev) head = 0;
            else if (prev->left == q) prev->left = 0;
            else prev->right = 0;
        } else if (!(q->right && q->left)) {
            if (q->right) {
                if (!prev) {
                    head = q->right;
                } else {
                    if (v < prev->val) {
                        prev->left = q->right;
                    } else {
                        prev->right = q->right;
                    }
                }
            } else if (q->left) {
                if (!prev) {
                    head = q->left;
                } else {
                    if (v < prev->val) {
                        prev->left = q->left;
                    } else {
                        prev->right = q->left;
                    }
                }
            }
        } else {
            Node<T> *right = q->right;
            Node<T> *leftmost = right;
            while (leftmost->left) {
                leftmost = leftmost->left;
            }
            leftmost->left = q->left;
            if (!prev) {
                head = right;
            } else {
                if (v < prev->val) {
                    prev->left = right;
                } else {
                    prev->right = right;
                }
            }
        }
        delete(q);
        return;
    }

    void search(T v) {
        search(v, head);
    }

    void search(T v, Node<T> *p) {
        if (p == 0) return;
        if (p->val == v) {
            cout << "Found" << endl;
            return;
        }
        if (v < p->val) {
            search(v, p->left);
        } else {
            search(v, p->right);
        }
        return;
    }

    void bft() {
        if (!head) return;
        Queue<Node<T>*> node_queue;
        node_queue.enqueue(head);
        while (!node_queue.empty()) {
            Node<T> *q = node_queue.dequeue();
            cout << q->val << " ";
            if (q->left) node_queue.enqueue(q->left);
            if (q->right) node_queue.enqueue(q->right);
        }
        cout << endl;
        return;
    }

    void preorder() {
        preorder(head);
        cout << endl;
    }

    void preorder(Node<T> *p) {
        if (p==0) return;
        cout << p->val << " ";
        preorder(p->left);
        preorder(p->right);
        return;
    }

    void inorder() {
        inorder(head);
        cout << endl;
    }

    void inorder(Node<T> *p) {
        if (p==0) return;
        inorder(p->left);
        cout << p->val << " ";
        inorder(p->right);
        return;
    }

    void postorder() {
        postorder(head);
        cout << endl;
    }

    void postorder(Node<T> *p) {
        if (p==0) return;
        postorder(p->left);
        postorder(p->right);
        cout << p->val << " ";
        return;
    }

    int height() {
        return height(head);
    }

    int height(Node<T> *p) {
        if (p==0) return 0;
        if (p->left == 0 && p->right == 0) return 1;
        return (1 + max(height(p->left), height(p->right)));
    }

    void count(int& i, int& t) {
        count(head, i, t);
    }

    void count(Node<T> *p, int& i, int& t) {
        if (p==0) return;
        if (!p->left && !p->right) {
            t = t + 1;
        } else {
            i = i + 1;
            count(p->left, i, t);
            count(p->right, i, t);
        }
        return;
    } 
};

int main() {
    BST<int> tree;
    int choice, value;
    
    int nums[13] = {50, 48, 70, 47, 49, 60, 90, 55, 65, 80, 100, 75, 85};
    for (int i = 0; i < 13; i++) {
        tree.insert(nums[i]);
    }

    while (true) {
        cout << "\n=== BST Menu ===" << endl;
        cout << "1. Insert" << endl;
        cout << "2. Remove" << endl;
        cout << "3. Search" << endl;
        cout << "4. Breadth First Traversal" << endl;
        cout << "5. Preorder Traversal" << endl;
        cout << "6. Inorder Traversal" << endl;
        cout << "7. Postorder Traversal" << endl;
        cout << "8. Height of Tree" << endl;
        cout << "9. Count Internal and Terminal Nodes" << endl;
        cout << "0. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;
        
        switch (choice) {
            case 1:
                cout << "Enter value to insert: ";
                cin >> value;
                tree.insert(value);
                cout << "Inserted " << value << endl;
                break;
                
            case 2:
                cout << "Enter value to remove: ";
                cin >> value;
                tree.remove(value);
                break;
                
            case 3:
                cout << "Enter value to search: ";
                cin >> value;
                tree.search(value);
                break;
                
            case 4:
                cout << "BFT: ";
                tree.bft();
                break;
                
            case 5:
                cout << "Preorder: ";
                tree.preorder();
                break;
                
            case 6:
                cout << "Inorder: ";
                tree.inorder();
                break;
                
            case 7:
                cout << "Postorder: ";
                tree.postorder();
                break;
                
            case 8:
                cout << "Height: " << tree.height() << endl;
                break;
                
            case 9: {
                int internal = 0, terminal = 0;
                tree.count(internal, terminal);
                cout << "Internal nodes: " << internal << endl;
                cout << "Terminal nodes: " << terminal << endl;
                cout << "Total nodes: " << (internal + terminal) << endl;
                break;
            }
                
            case 0:
                cout << "Exiting..." << endl;
                return 0;
                
            default:
                cout << "Invalid choice!" << endl;
        }
    }
    
    return 0;
}
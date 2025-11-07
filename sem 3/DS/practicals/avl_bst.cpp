#include <iostream>

using namespace std;

template <typename T>
class Node {
    T val;
    Node* left;
    Node* right;
public:
    Node(T v): val(v), left(0), right(0) {}; 
    friend class AVLTree;
};

template <typename T>
class AVLTree {
    Node<T> *root;
public:
    AVLTree(Node *r): root(r) {};
    void insert(T val) {
        Node<T> *p = new Node<T>(val);
        if (!root) {
            root = p;
            return;
        }
        Node<T> *q = root;
        while(true) {
            if (val < q->val) {
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

    };
};
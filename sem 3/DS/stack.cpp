#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Node {
    int val;
    Node *next;
public:
    Node(int v = 0, Node *n = 0) {
        val = v;
        next = n;
    };
    friend class Stack;
};

class Stack {
    Node *head;
    int cap;
public:
    Stack() {
        head = 0;
        cap = 0;
    };
    void push(int val) {
        Node *p;
        p = new Node(val);
        if (!head) {
            head = p;
        } else {
            Node *q;
            q = head;
            head = p;
            head->next = q;
        };
        cap++;
        return;
    };

    void pop() {
        if (head) {
            Node *q;
            q = head;
            head = head->next;
            delete(q);
            cap--;
        }
        return;
    }

    int peek() {
        return head->val;
    }

    bool isEmpty() {
        return head == 0;
    }

    int size() {
        return cap;
    }

    void clear() {
        head = 0;
        return;
    }

    int search(int v) {
        Node *q;
        q = head;
        int n;
        while (q->next) {
            if (q->val == v) {
                return n;
            }
            q =  q->next;
            n++;
        }
        return -1;
    }
};

int applyOp(int lhs, int rhs, char op) {
    switch (op) {
        case '+': return lhs + rhs;
        case '-': return lhs - rhs;
        case '*': return lhs * rhs;
        case '/': return rhs == 0 ? 0 : lhs / rhs;
        default:  return 0;
    }
}

bool isOp(const string &token) {
    return token.size() == 1 && (token[0] == '+' || token[0] == '-' || token[0] == '*' || token[0] == '/');
}

int evaluatePostfix(const string &expr) {
    Stack st;
    string token;
    stringstream ss(expr);
    while (ss >> token) {
        if (isOp(token)) {
            int rhs = st.peek(); st.pop();
            int lhs = st.peek(); st.pop();
            st.push(applyOp(lhs, rhs, token[0]));
        } else {
            st.push(stoi(token));
        }
    }
    int result = st.peek(); st.pop();
    return result;
}

int evaluatePrefix(const string &expr) {
    vector<string> tokens;
    string token;
    stringstream ss(expr);
    while (ss >> token) {
        tokens.push_back(token);
    }
    Stack st;
    for (int i = static_cast<int>(tokens.size()) - 1; i >= 0; --i) {
        if (isOp(tokens[i])) {
            int lhs = st.peek(); st.pop();
            int rhs = st.peek(); st.pop();
            st.push(applyOp(lhs, rhs, tokens[i][0]));
        } else {
            st.push(stoi(tokens[i]));
        }
    }
    int result = st.peek(); st.pop();
    return result;
}

int main() {
    cout << evaluatePostfix("5 1 2 + 4 * + 3 -") << "\n";
    cout << evaluatePrefix("- + 7 * 4 5 + 2 0") << "\n";
    return 0;
}

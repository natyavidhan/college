```cpp
#include <iostream>
using namespace std

class Node {
	int val;
	Node *next;
	Node(int value, Node *n) {
		val = value;
		next = n;
	}
	friend class LinkedList;
}

class LinkedList {
	Node *head;
	LinkedList() {
		head = 0;
	}
	
	void add_start(int value) {
		Node *p;
		p = new Node(value);
		if (!head) {
			head = p;
			return;
		}
		p->next = head;
		head = p;
		return;
	}
}

```
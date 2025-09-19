class Node:
    def __init__(self, value="", next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head:
            p = self.head
            while p:
                print(p.value, end="")
                p = p.next
                if p:
                    print(" -> ", end="")
            print()
    
    def is_empty(self):
        return self.head is None
    
    def add_start(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node
        
    def add_end(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = node
        
    def add_ith(self, val, i):
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        p = self.head
        j = 0
        while j < i-1:
            p = p.next
            j+=1
        node.next = p.next
        p.next = node
    
    def delete_start(self):
        self.head = self.head.next
    
    def delete_end(self):
        p = self.head
        while p.next.next:
            p = p.next
        p.next = None
        
    def delete_ith(self, i):
        p = self.head
        j = 0
        while j < i-1:
            p = p.next
            j+=1
        q = p.next
        p.next = q.next
        
    def reverse(self):
        p = self.head
        q = p.next
        r = q.next
        p.next = None
        while r:
            q.next = p
            p = q
            q = r
            r = r.next
        q.next = p
        self.head = q
        
    def search(self, val):
        p = self.head
        i = 0
        while p:
            if p.value == val:
                return i
            i+=1
            p = p.next
        return False
    
    def concat(self, llist):
        p = self.head
        while p.next:
            p = p.next
        p.next = llist.head
        
    def merge(self, llist):
        new = LinkedList()
        h1 = self.head
        h2 = llist.head
        while h1 and h2:
            if h1.value > h2.value:
                val = h2
                h2 = h2.next
            else:
                val = h1
                h1 = h1.next
            new.add_end(val.value)
        p = new.head
        while p.next:
            p = p.next

        if h1:
            p.next = h1
        else:
            p.next = h2
            
        return new

if __name__ == "__main__":
    llist = LinkedList()
    for i in [10, 12, 14, 16, 18, 20, 40]:
        llist.add_end(i)
    llist.print()
    # llist.delete_ith(2)
    llist.reverse()
    llist.print()
    
    llist2 = LinkedList()
    for i in [1, 3, 5, 7, 9]:
        llist2.add_end(i)
    new = llist.merge(llist2)
    new.print()
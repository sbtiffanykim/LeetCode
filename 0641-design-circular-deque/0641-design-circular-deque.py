class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.len = 0
        self.head = self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.k == self.len:
            return False
        if self.len == 0:
            self.head = self.tail = Node(value)
        else:
            curr = Node(value)
            self.head.prev, curr.next = curr, self.head
            self.head = curr
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.k == self.len:
            return False
        if self.len == 0:
            self.head = self.tail = Node(value)
        else:
            curr = Node(value)
            self.tail.next, curr.prev = curr, self.tail
            self.tail = curr
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.head = self.head.next
        self.len -= 1
        return True
        
    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.tail = self.tail.prev
        self.len -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.len == 0 else self.head.val

    def getRear(self) -> int:
        return -1 if self.len == 0 else self.tail.val
        
    def isEmpty(self) -> bool:
        return (self.len == 0)

    def isFull(self) -> bool:
        return (self.len == self.k)        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
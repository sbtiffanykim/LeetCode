# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            nxt = node.next
            node.next = prev
            prev, node = node, nxt
        
        return prev
            
    def toList(self, head: ListNode) -> [ListNode]:
        result = list()
        
        while head:
            result.append(head.val)
            head = head.next
        
        return result
    
    def toLinkedList(self, res: ListNode):
        prev = None
        
        for r in res:
            node = ListNode(r)
            node.val = r
            node.next = prev
            prev = node
        
        return node
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            a = self.toList(self.reverseList(l1))
            b = self.toList(self.reverseList(l2))
            res = int(''.join([str(x) for x in a])) + int(''.join([str(x) for x in b]))
            res = [n for n in str(res)]
            
            return self.toLinkedList(res)
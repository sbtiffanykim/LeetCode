# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy to store answer
        dummy = ListNode()
        node = dummy
        
        flag = 0  # 1 if sum of two digits is greater than/equal to 10
        while l1 or l2 or flag:
            # add digit
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + flag
            flag = val // 10
            val %= 10  # last digit
            node.next = ListNode(val)
            
            # update pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node = node.next
        
        return dummy.next
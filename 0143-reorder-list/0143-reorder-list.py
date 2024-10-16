# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the linked list into two halves
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # break the link between the two lists
        second = slow.next
        slow.next = prev = None

        # reverse the second linked list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two linked lists by interleaving their nodes
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
"""
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
 
Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        current = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                current.next, current, l1 = l1, l1, l1.next
            else:
                current.next, current, l2 = l2, l2, l2.next
        if l1 != None:
            current.next = l1
        if l2 != None:
            current.next = l2
        return head.next
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None
        sorted_l1 = self.sortList(head)
        sorted_l2 = self.sortList(slow)
        return self.mergeTwoLists(sorted_l1, sorted_l2)

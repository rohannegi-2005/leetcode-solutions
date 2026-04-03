# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        print(arr)

        arr.sort()

        dummy = ListNode(0)
        curr = dummy

        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next
            

            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next

        # arr = arr[::-1]
        
        # dummy = ListNode(0)
        # curr = dummy

        # for i in arr:
        #     curr.next = ListNode(i)
        #     curr = curr.next

        # return dummy.next
        prev = None 
        while head:
            next_node = head.next # save next node
            head.next = prev      # reverse node
            prev = head            
            head = next_node
        
        
        return prev

        
            # head = head.next
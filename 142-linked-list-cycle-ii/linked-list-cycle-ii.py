# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        store = {}
        while dummy:
            if dummy in store:
                return dummy
            store[dummy] = 1
            dummy = dummy.next
        
        return None


        
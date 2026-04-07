# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dictinary = {}
        
        while headA:
            dictinary[headA] = 0
            headA = headA.next

        # print(dictinary)

        while headB:
            if headB in dictinary:
                return headB
            headB = headB.next
            

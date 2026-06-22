from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        result_map = {} 
        stack = deque()

        for i in range(n):
            while stack and nums2[i] > nums2[stack[-1]]:
                index = stack.pop()
                result_map[nums2[index]] = nums2[i]
            stack.append(i)

        print(result_map)

        for i in range(len(nums1)):
            nums1[i] = result_map.get(nums1[i], -1)

        return nums1


        
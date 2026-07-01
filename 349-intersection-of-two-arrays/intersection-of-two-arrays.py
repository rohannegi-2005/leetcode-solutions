class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        # for i in nums1:
        #     if i in nums2:
        #         answer.append(i)

        # return list(set(answer))

        i = 0
        j = 0 
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j = j + 1
            elif nums1[i] < nums2[j]:
                i = i + 1
            else:
                
                answer.append(nums1[i])
                i = i + 1
                j = j + 1

        return list(set(answer))




        
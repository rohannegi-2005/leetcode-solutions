class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dictionary = {}
        count = 0
        idx = 0
        ans = 0

        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
                count = count + 1
            else:
                if dictionary[i] == k:
                    ans = max(ans, count)
                    while dictionary[i] >= k:
                        dictionary[nums[idx]] = dictionary[nums[idx]] - 1
                        idx = idx + 1
                        count = count - 1

                dictionary[i] = dictionary[i] + 1
                count = count + 1

        return max(ans, count)

                







        
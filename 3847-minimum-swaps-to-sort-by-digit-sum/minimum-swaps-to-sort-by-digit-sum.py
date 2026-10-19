class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def SumOfDigit(digit):
            total = 0
            while digit != 0:
                total = total + digit % 10
                digit = digit // 10
            return total
        
        dictionary = {}
        for i in nums:
            dictionary[i] = SumOfDigit(i)
        print(dictionary)


        nums_2 = sorted(nums, key=lambda x: (dictionary[x], x))

        position = {}
        for i in range(len(nums)):
            num = nums[i]
            position[num] = i


        length = len(dictionary)
        swap_count = 0

        for i in range(length):
            target = nums_2[i]

            if nums[i] != target:
                index = position[target]

                # swap numbers
                nums[i], nums[index] = nums[index], nums[i]

                # Update their current positions
                position[nums[i]] = i
                position[nums[index]] = index

                swap_count = swap_count + 1

        return swap_count

            

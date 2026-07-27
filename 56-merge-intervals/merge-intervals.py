class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        n = len(intervals)

        while i < n:
            if intervals[i][0] > intervals[i-1][1]:
                i = i + 1
                # print("1st")

            elif intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                del intervals[i]
                n = n - 1
                # print("2nd")

            else:
                i = i + 1
                # print("3rd")


        return intervals

            


        
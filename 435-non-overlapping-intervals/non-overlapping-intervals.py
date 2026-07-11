class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        # print(intervals)
        n = len(intervals)
        count = 0
        store = intervals[0][1]
        for i in range(n-1):
            if store > intervals[i+1][0]:
                count = count + 1
            else:
                store = intervals[i+1][1]

        return count



        
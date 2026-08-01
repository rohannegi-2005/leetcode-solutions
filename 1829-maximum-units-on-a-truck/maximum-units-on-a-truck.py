class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x: x[1], reverse=True)

        ans = 0

        for boxes, perunit in boxTypes:
            take = min(boxes, truckSize)
            truckSize = truckSize - take
            ans = ans + take * perunit

            if truckSize == 0:
                break

        return ans





        
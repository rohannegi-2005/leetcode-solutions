class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total = sum(cardPoints[0:k])
        maxPoint = total

        for i in range(k):
            total = total - cardPoints[k-1-i]
            total = total + cardPoints[len(cardPoints)-1-i]

            maxPoint = max(maxPoint, total)

        return maxPoint

        
        
        
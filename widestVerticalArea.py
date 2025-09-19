class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_cord = sorted([x for x, _ in points])

        return max(x_cord[i+1] - x_cord[i] for i in range(len(x_cord)-1))
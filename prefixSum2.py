class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # n ice cream bars
        # costs [] length = n
        # costs[i] = ith ice ceam
        # coins

        n = len(costs)
        costs.sort()
        prefix_sum = [0] * n
        prefix_sum[0] = costs[0]
        most = 0

        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + costs[i]

        for j in range(len(prefix_sum)):
            if prefix_sum[j] <= coins:
                most = j + 1
        
        return most


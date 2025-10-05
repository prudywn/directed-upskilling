class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # piles[i] = number of coins in ith pile
        # 
        sorted_pile = sorted(piles)
        size = len(piles)
        n = size // 3 # no. of triplets we'll get and no. of picks for each
        skipped = sorted_pile[n:] #remove Bob's
        reversed_skipped = skipped[::-1]
        mine = []
       
        for i in range(len(reversed_skipped) - 1, -1, -2):
            mine.append(reversed_skipped[i])

        return sum(mine)
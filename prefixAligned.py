class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_flipped = 0

        for i, f in enumerate(flips, start=1):
            max_flipped = max(max_flipped, f)
            if max_flipped == i:
                count += 1

        return count
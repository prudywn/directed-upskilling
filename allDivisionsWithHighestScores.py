class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total_ones = sum(nums)
        max_result = -1
        result = []
        zeros = 0
        ones = 0

        for i in range(len(nums) + 1):
            score = zeros + (total_ones - ones)
            if score > max_result:
                max_result = score
                result = [i]
            elif score == max_result:
                result.append(i)

            if i < len(nums):
                if nums[i] == 0:
                    zeros += 1
                elif nums[i] == 1:
                    ones += 1
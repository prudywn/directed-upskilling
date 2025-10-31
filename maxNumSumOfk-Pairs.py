class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        nums.sort()
        
        while left < right:
            sum_nums = nums[left] + nums[right]
            if sum_nums == k:
                count += 1
                left += 1
                right -= 1
            elif sum_nums < k:
                left += 1
            else:
                right -= 1
            

        return count
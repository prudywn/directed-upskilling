class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum_pair = nums[i] + nums[j] 

                if sum_pair < target:
                    count += 1
                
        return count
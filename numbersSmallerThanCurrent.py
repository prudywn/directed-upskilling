class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(n):
                if j != i and nums[j] < nums[i]:
                        count += 1
        
            answer.append(count)
               
                
        return answer

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i*j) % k ==0:
                    count += 1

        return count

""" loops through each number comparing it 
with each number after it to find a match then 
takes  the index i of the first number and the index of matching pair j and multiplies them"""
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        largest = nums[-1]
        nextLargest = 0
        n = len(nums)

        # loop from right to left
        for i in range(n -2, -1, -1):
            if nums[i] < largest: #found the next smaller number
                nextLargest = nums[i]
                operations += n - i - 1 # the number of elements strictly to the right of index i.
                largest = nextLargest
        
        return operations    
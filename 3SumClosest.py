class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(0, len(nums) - 1):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]  # Current sum of the triplet
                #Check if sum is close to target
                if abs(triplet_sum - target) < abs(closest_sum - target):
                    closest_sum = triplet_sum

                if triplet_sum == target:
                    return triplet_sum

                elif triplet_sum < target:
                    left += 1

                else:
                    right -= 1

        return closest_sum


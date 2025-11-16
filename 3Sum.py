class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()   # Sort the numbers so we can use two pointers

        triplets = []  # This will store the final list of valid triplets

        # Loop through each number, treating nums[i] as the first number of the triplet
        for i in range(0, len(nums) - 1):

            if nums[i] > 0:
                break   # Since array is sorted, no three positive numbers can sum to 0

            if i > 0 and nums[i] == nums[i - 1]:
                continue   # Skip duplicate values for the first number

            # Two-pointer setup for the remaining two numbers
            left = i + 1
            right = len(nums) - 1

            # Move left and right pointers until they cross
            while left < right:

                total = nums[i] + nums[left] + nums[right]  # Current sum of the triplet

                if total == 0:
                    # Found a valid triplet
                    triplets.append([nums[i], nums[left], nums[right]])

                    left += 1     # Move left pointer
                    right -= 1    # Move right pointer

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1   # Sum too small → move left to increase it

                else:
                    right -= 1  # Sum too big → move right to decrease it

        return triplets   # Return all found triplets that sum to zero

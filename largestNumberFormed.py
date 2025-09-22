from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
    
       #Compare to decide order of concantention
       def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0

    #convert all numbers to strings for comparison
       nums = list(map(str, nums))

       # Sort using the custom comparator
       nums.sort(key=cmp_to_key(compare))

       #Join into a single string
       result = ''.join(nums)

       # Handle edge case where the result is all zeros
       return '0' if result[0] == '0' else result


        
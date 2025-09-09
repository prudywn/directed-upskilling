class Solution:
    def reversedString(self, s: List[str])-> None:
        left, right = 0, len(s) - 1

        if left < right:
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #count of every char in s if equal to one in t
        if len(s) != len(t):
            return False

        d = {}

        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        for char in t:
            if char in d:
                d[char] -= 1
            else:
                return False
        
        for value in d.values():
            if value != 0:
                return False
        return True
            


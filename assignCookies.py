class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookieIndex = 0
        contentChildren = 0
       
        while cookieIndex < len(s) and contentChildren < len(g):
            if s[cookieIndex] >= g[contentChildren]:
                contentChildren += 1   
            cookieIndex += 1
               
        return contentChildren

       
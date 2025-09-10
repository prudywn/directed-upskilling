class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted_count = 0

        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                if strs[col][row] < str[row-1][col]:
                    deleted_count += 1

        return deleted_count
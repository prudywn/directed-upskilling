class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff_arr = [0] * (n+1)

        for start, end, direction in shifts:
            if direction == 1:
                diff_arr[start] += 1
                diff_arr[end + 1] -= 1
            
            else:
                diff_arr[start] -= 1
                diff_arr[end + 1] += 1

        # Build prefix sum
        for i in range(1, n):
            diff_arr[i] += diff_arr[i - 1]

        #apply shifts
        result = []
        for i in range(n):
            shift = (ord(s[i]) - ord('a') + diff_arr[i]) % 26
            result.append(chr(shift + ord('a')))

        return ''.join(result)

class Solution:
    def smallestNumber(self, num: int) -> int:
        # handle zero
        if num == 0:
            return 0

        if num > 0:
            digits = sorted(str(num))
            # avoid leading zero find first non-zero and swap
            if digits[0] == "0":
                for i in range(1, len(digits)):
                    if digits[i] != "0":
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return int("".join(digits))

        else:
            digits = sorted(str(-num), reverse=True)  # sort descending
            return -int("".join(digits))

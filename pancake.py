class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for size in range(n, 1, -1):
            # Find the index of the maximum number in the unsorted section
            max_idx = arr.index(max(arr[:size]))

            if max_idx == size - 1:
                continue  # already in correct place

            # Flip max number to the front if not already there
            if max_idx != 0:
                res.append(max_idx + 1)
                arr[: max_idx + 1] = reversed(arr[: max_idx + 1])

            # Flip it to its correct position
            res.append(size)
            arr[:size] = reversed(arr[:size])

        return res

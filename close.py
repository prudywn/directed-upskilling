from bisect import bisect_left

def nearest_left_tiebreak(arr, x):
    i = bisect_left(arr, x)
    candidates = []
    if i - 1 >= 0:
        candidates.append(arr[i - 1])
    if i < len(arr):
        candidates.append(arr[i])
    if len(candidates) == 1:
        return candidates[0]
    left, right = candidates
    dl, dr = abs(x - left), abs(right - x)
    return left if dl <= dr else right

def solve(base_line, query_line):
    base = list(map(int, base_line.split()))
    queries = list(map(int, query_line.split()))
    return [nearest_left_tiebreak(base, q) for q in queries]

# Example with your dataset:
base_line = "2 15 25 25 36 42 42 53 59 59 63 69 86 88 96"
query_line = "12 58 15 77 8 10 43 25 60 95 3 52 90 51 0"

result = solve(base_line, query_line)
print(" ".join(map(str, result)))

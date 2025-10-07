import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # will store (-distance, [x, y])

        for x, y in points:
            d = x**2 + y**2
            # use negative distance to simulate a max heap
            heapq.heappush(heap, (-d, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)  # remove the farthest

        # extract only the points
        return [point for (_, point) in heap]
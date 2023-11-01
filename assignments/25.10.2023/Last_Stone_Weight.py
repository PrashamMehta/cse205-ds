class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = []
        for stone in stones:
            heapq.heappush(stoneHeap, -stone)

        while len(stoneHeap) > 1:
            x = -heapq.heappop(stoneHeap)
            y = -heapq.heappop(stoneHeap)
            if x == y:
                continue

            if x > y:
                heapq.heappush(stoneHeap, -(x - y))

            else:
                heapq.heappush(stoneHeap, -(y - x))

        return 0 if len(stoneHeap) == 0 else -heapq.heappop(stoneHeap)
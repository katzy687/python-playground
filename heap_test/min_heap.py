import heapq

heap = []
heapq.heapify(heap)
heapq.heappush(heap, 9)
heapq.heappush(heap, 5)
heapq.heappush(heap, 11)
print(heap[0])
heapq.heappop()
pass
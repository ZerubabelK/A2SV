def heappeak(heap):
    smallest = heapq.heappop(heap)
    heapq.heappush(heap, smallest)
    return smallest

def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    iterations = 0
    while heappeak(A) < k:
        if len(A) <= 1 and heappeak(A) < k:
            return -1
        s1 = heapq.heappop(A)
        s2 = heapq.heappop(A)
        heapq.heappush(A, s1 + 2 * s2)
        iterations += 1
    return iterations

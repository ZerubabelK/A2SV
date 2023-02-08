class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        
        for i in range(len(routes)):
            for stop in routes[i]:
                graph[stop].add(i)

        bfs = deque([(source, 0)])
        stops = set()
        buses = set()
        while bfs:
            stop, count = bfs.popleft()
            if stop == target:
                return count
            for i in graph[stop]:
                if i not in buses:
                    buses.add(i)
                    for stop in routes[i]:
                        if stop not in stops:
                            stops.add(stop)
                            bfs.append((stop, count + 1))
        return -1
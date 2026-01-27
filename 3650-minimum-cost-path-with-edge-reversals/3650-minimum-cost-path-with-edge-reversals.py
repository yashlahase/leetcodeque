import heapq
from collections import defaultdict

class Solution(object):
    def minCost(self, n, edges):
        graph = defaultdict(list)

        # Build graph with normal and reversed edges
        for u, v, w in edges:
            graph[u].append((v, w))        # normal edge
            graph[v].append((u, 2 * w))    # reversed edge (using switch)

        # Dijkstra
        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)

        while pq:
            cost, node = heapq.heappop(pq)

            if cost > dist[node]:
                continue

            if node == n - 1:
                return cost

            for nxt, w in graph[node]:
                new_cost = cost + w
                if new_cost < dist[nxt]:
                    dist[nxt] = new_cost
                    heapq.heappush(pq, (new_cost, nxt))

        return -1

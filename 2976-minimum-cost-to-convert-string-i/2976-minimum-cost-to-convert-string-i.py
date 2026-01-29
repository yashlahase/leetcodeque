class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        N = 26

        # Distance matrix for characters a-z
        dist = [[INF] * N for _ in range(N)]
        for i in range(N):
            dist[i][i] = 0

        # Direct transformations
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)

        # Floyd-Warshall (all-pairs shortest path)
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Calculate total cost
        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]

        return total

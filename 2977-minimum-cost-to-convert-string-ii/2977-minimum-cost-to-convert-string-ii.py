class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        INF = 10**18
        n = len(source)

        from collections import defaultdict

        # Group transformations by length
        by_len = defaultdict(dict)
        for o, c, w in zip(original, changed, cost):
            L = len(o)
            if (o, c) not in by_len[L] or by_len[L][(o, c)] > w:
                by_len[L][(o, c)] = w

        # For each length, run Floyd–Warshall
        best = defaultdict(dict)

        for L, edges in by_len.items():
            nodes = set()
            for o, c in edges:
                nodes.add(o)
                nodes.add(c)

            nodes = list(nodes)
            dist = {}

            for s in nodes:
                dist[(s, s)] = 0
            for (o, c), w in edges.items():
                dist[(o, c)] = min(dist.get((o, c), INF), w)

            for k in nodes:
                for i in nodes:
                    if (i, k) not in dist:
                        continue
                    for j in nodes:
                        if (k, j) not in dist:
                            continue
                        new_cost = dist[(i, k)] + dist[(k, j)]
                        if new_cost < dist.get((i, j), INF):
                            dist[(i, j)] = new_cost

            best[L] = dist

        # DP over string
        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            # Case 1: characters already match
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            # Case 2: try all substring lengths
            for L in best:
                if i + L > n:
                    continue
                s_sub = source[i:i + L]
                t_sub = target[i:i + L]
                if (s_sub, t_sub) in best[L] and dp[i + L] != INF:
                    dp[i] = min(dp[i], best[L][(s_sub, t_sub)] + dp[i + L])

        return -1 if dp[0] == INF else dp[0]

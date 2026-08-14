class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}

        for s, d, w in flights:
            adj[s].append((d, w))

        # (cost, node, flights_taken)
        minHeap = [(0, src, 0)]

        # Cheapest cost to reach node using a given number of flights
        best = {}

        while minHeap:
            cost, node, flights = heapq.heappop(minHeap)

            if node == dst:
                return cost

            # At most k stops = k + 1 flights
            if flights == k + 1:
                continue

            for neighbor, price in adj[node]:
                new_cost = cost + price
                new_flights = flights + 1

                # Only explore if this is useful
                if (neighbor, new_flights) not in best or \
                   new_cost < best[(neighbor, new_flights)]:

                    best[(neighbor, new_flights)] = new_cost
                    heapq.heappush(
                        minHeap,
                        (new_cost, neighbor, new_flights)
                    )

        return -1
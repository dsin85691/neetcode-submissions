import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        prev = None  # holds (freq, char) that must wait one round before re-entering heap
        res = []

        while heap:
            freq, char = heapq.heappop(heap)
            res.append(char)
            freq += 1  # move toward 0 (freq stored negative)

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if freq != 0:
                prev = (freq, char)  # can't push back yet — would be adjacent

        if len(res) != len(s):
            return ""
        return "".join(res)
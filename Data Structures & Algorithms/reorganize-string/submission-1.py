class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter()
        for char in s:
            count[char] = count.get(char, 0) + 1

        heap = []
        for key in count:
            heapq.heappush(heap, (-1 * count[key], key))

        res, last_char = [], None
        wait = None          # <-- NEW: holds the blocked (freq, char) for one round
        idx = 0

        while len(heap) > 0 and idx <= len(s):
            freq, char = heapq.heappop(heap)
            adjacent = (last_char == char)

            if adjacent:
                # Can't use this char yet — set it aside and grab the next-best instead
                wait = (freq, char)
                if len(heap) == 0:
                    break            # nothing else available -> impossible to continue
                freq, char = heapq.heappop(heap)

            res.append(char)         # always append now — we resolved the clash above
            freq = -1 * freq
            if freq - 1 > 0:
                heapq.heappush(heap, (-1 * (freq - 1), char))

            if wait is not None:      # release the held-back char now that a round passed
                heapq.heappush(heap, wait)
                wait = None

            last_char = char
            idx += 1

        return "".join(res) if len(res) == len(s) else ""
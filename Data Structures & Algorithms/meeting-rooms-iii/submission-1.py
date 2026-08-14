class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n)) # Available rooms
        heapq.heapify(available)
        busy = []  # (end_time, room_number)
        counter = Counter()

        for start, end in meetings:
            duration = end - start

            # Free all rooms available by the meeting's start time
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            # There is an available room
            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))

            # All rooms are busy -> delay meeting
            else:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (end_time + duration, room))

            counter[room] += 1

        return max(range(n), key=lambda room: counter[room])
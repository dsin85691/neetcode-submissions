"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        resource = defaultdict(int)
        for i in intervals:
            resource[i.start] += 1
            resource[i.end] -= 1
        prev = 0
        res = 0
        for i in sorted(resource.keys()):
            prev += resource[i]
            res = max(res, prev)
        return res
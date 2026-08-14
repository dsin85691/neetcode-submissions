"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: 
            return True
        intervals.sort(key=lambda x: x.start)
        target = intervals[0]
        for i in range(1, len(intervals)): 
            if target.end > intervals[i].start: 
                return False
            target = intervals[i]
        return True
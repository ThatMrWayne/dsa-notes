from typing import List
#57


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        s1_idx = None
        for i in range(len(intervals)-1):
            if intervals[i][0]<=newInterval[0]<=intervals[i+1][0]:
                s1_idx = i+1
                break
        if s1_idx is None:
            if newInterval[0]>=intervals[-1][0]:
                s1_idx = len(intervals)
            else:
                s1_idx = 0
        if s1_idx == len(intervals):
            intervals.append(newInterval)
        else:
            intervals.insert(s1_idx, newInterval)

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = result[-1]
            if curr[-1]>=intervals[i][0] and intervals[i][-1]>=curr[-1]:
                result[-1] = [curr[0], intervals[i][-1]]
            elif curr[-1]>=intervals[i][0] and curr[-1]>intervals[i][-1]:
                continue
            else:
                result.append(intervals[i])
        return result

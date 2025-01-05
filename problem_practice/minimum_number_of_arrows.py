from typing import List
#452


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        curr_min = points[0][0]
        curr_max = points[0][-1]
        res = 1
        for i in range(1, len(points)):
            if curr_min<=points[i][0]<=curr_max:
                curr_min = curr_min if curr_min>points[i][0] else points[i][0]
                curr_max = curr_max if curr_max<points[i][1] else points[i][1]
            else:
                res+=1
                curr_min = points[i][0]
                curr_max = points[i][1]
        return res

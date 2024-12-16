# 11
#TC: O(n)
#SC: O(1)



def maxArea(height) -> int:
    p1, p2 = 0, len(height)-1
    max_area = 0
    x = len(height)-1
    while p1!=p2:
        area = x*min(height[p1], height[p2])
        max_area = area if area > max_area else max_area
        x-=1
        if height[p1]>=height[p2]:
            p2-=1
        else:
            p1+=1
    print(max_area)

maxArea([1,1])
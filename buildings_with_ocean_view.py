from collections import deque

def findBuildings(heights):
    max_height = -1 
    result = deque([])

    for i in range(len(heights) -1, -1,-1):
        cur_height = heights[i]
        if cur_height > max_height:
            result.appendleft(i)
            max_height = cur_height
    return result

print(findBuildings([4,2,3,1]))
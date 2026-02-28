from typing import List
def findMinArrowShots(points: List[List[int]]) -> int:
    if not points:
        return 0
    points.sort(key=lambda x:x[1])

    i = 0
    n = len(points)
    arrows = 0
    while i < n:
        arrows += 1
        arrow_x = points[i][1]
        while  i < n and arrow_x>= points[i][0]:
            i += 1
        
    return arrows


if __name__ == "__main__":
    points = [[1,2],[3,4],[5,6],[7,8]]
    print(findMinArrowShots(points))

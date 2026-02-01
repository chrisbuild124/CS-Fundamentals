# Detect squares in a 2D grid
# Link: https://leetcode.com/problems/detect-squares/

# Tricks: Use diagonal as a point and detect if two other 
# points are there. Then multiply the amount of points in those
# three points. 
class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0

        for x2 in self.points:
            for y2 in self.points[x2]:
                # Check not same x or y coordinate
                if x1 == x2 or y1 == y2:
                    continue
                # Check square
                if abs(x1 - x2) != abs(y1 - y2):
                    continue 
                # Prevent modification to dictionary
                if x1 not in self.points or y1 not in self.points[x2]:
                    continue
                res += self.points[x2][y2] * self.points[x1][y2] * self.points[x2][y1]
        
        return res

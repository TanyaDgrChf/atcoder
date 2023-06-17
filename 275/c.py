import sys
import math
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    def point_distance(self, Point):
        distance = math.sqrt((self.x - Point.x)^2 + (self.y - Point.y)^2)
        return distance
    def is_lower_right(self, point):
        if point.x > self.x:
            if point.y >= self.y:
                return True
        return False
    def forms_square(self, point, grids):
        dx = point.x - self.x
        dy = point.y - self.y
        p = Point(point.x - dy, point.y + dx)
        q = Point(self.x - dy, self.y + dx)
        exist = p.exists(grids) and q.exists(grids)
        if exist:
            #print('is square', self.x, self.y, point.x, point.y)
            a = 'a'
        return exist
    def exists(self, grids):
        exists = False
        if self.x <= 8 and self.x >= 0:
            if self.y <= 8 and self.y >= 0:
                exists =  grids[self.y][self.x] == '#'
        #print(exists, 'exist', self.x, self.y)
        return exists

'''
def find_coords(grid):
    points = []
    for i in range(0, 9):
        for j in range(0, len(grid[i])):
            if grid[i][j] == '#':
                x = j + 1
                y = i + 1
                points.append(Point(x, y))
    return points
'''

def find_squares(points, grids):
    count = 0
    for p in points:
        for q in points:
            #print('pair', p.x, p.y, q.x, q.y)
            if p.is_lower_right(q):
                #print('lower right', p.x, p.y, q.x, q.y)
                if p.forms_square(q, grids):
                    count += 1
    return count





if __name__ == '__main__':
    grid_input = []
    grids = []
    for i in range(0, 9):
        line = input()
        grids.append(line)
        for j in range(0,9):
            if line[j] == '#':
                grid_input.append(Point(j, i))
    print(find_squares(grid_input, grids))


    
    

#   #   #   #   #   #   #
#  Author phantomhive   #
#      31-07-2019       #
#   #   #   #   #   #   #

from collections import Counter, deque, defaultdict
from math import ceil, floor, sqrt, log, factorial
from fractions import Fraction, gcd
from sys import stdin, stdout
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from time import time
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write
# Start time
START = time()
class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
ORIGIN = coordinate(0, 0)
class triangle:
    def __init__(self, points):
        self.a = coordinate(points[0], points[1])
        self.b = coordinate(points[2], points[3])
        self.c = coordinate(points[4], points[5])
    
    def to_points(self, a, b, c):
        return [a.x, a.y, b.x, b.y, c.x, c.y]

    def area(self):
        area_2 = sum([
            (self.a).x * ((self.b).y-(self.c).y),
            (self.b).x * ((self.c).y-(self.a).y),
            (self.c).x * ((self.a).y-(self.b).y),
        ])
        area = area_2/2.0
        return abs(area)

    def check_origin_inside(self):
        triangle1 = triangle(self.to_points(self.a, self.b, ORIGIN))
        triangle2 = triangle(self.to_points(self.b, self.c, ORIGIN))
        triangle3 = triangle(self.to_points(self.a, self.c, ORIGIN))
        return (triangle1.area() + triangle2.area() + triangle3.area()) == self.area()
    
    def __str__(self):
        return (
            str(self.a.x) + ' ' + str(self.a.y) + '; '+
            str(self.b.x) + ' ' + str(self.b.y) + '; '+
            str(self.c.x) + ' ' + str(self.c.y) + ';'
        )
    


with open('input102.txt', 'r') as my_file:
    triangles = [ triangle(map(int, t_point.split(','))) for t_point in my_file]

count = 0
for triangle_ob in triangles:
    if triangle_ob.check_origin_inside():
        count+=1
cout('Total triangles : %d\n'%count)


# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))
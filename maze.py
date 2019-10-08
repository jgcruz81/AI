import numpy as num
from numpy import zeros
import random
from operator import attrgetter

class Node:
    def __init__(self, x, y, g, h, f, direction):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f
        # this direction attribute is for me to see which direction that check is using
        # will be removed later
        self.direction = direction
        return
# initializes the positions of start and end
endrow = random.randint(0,3)
endcolumn = random.randint(0,9)
startrow = random.randint(7,9)
startcolumn = random.randint(0,9)

# we'll start with a small 10 x 10 maze to visualize
a = zeros([10,10])
for x in range(10):
    for y in range(3):
        wall = random.randint(0, 9)
        a[x][wall] = 1
a[endrow][endcolumn] = 3
a[startrow][startcolumn] = 2
print(a)


#def begin(a, startx, starty, endx, endy):


# function to check neighbors for lowest f value(done)
# if there's a tie then resort to h value (not done)
# if there's a tie then random (not done)
# if all directions are impassable (not done)   perhaps return no value
def checkneighbors(x,y,a,i,j,g):
    neighbors = []
    # check up
    if x != 0 and a[x-1][y] == 0:
        h = abs(x-i-1) + abs(y-j)
        f = g + h
        neighbors.append(Node(x-1,y,g+1,h,f,"up"))
    # check left
    if y != 0 and a[x][y-1] == 0:
        h = abs(x-i) + abs(y-j-1)
        f = g + h
        neighbors.append(Node(x-1,y,g,h, f,"left"))
    # check down
    if x != 9 and a[x+1][y] == 0:
        h = abs(x-i+1) + abs(y-j)
        f = g + h
        neighbors.append(Node(x-1,y,g,h,f,"down"))
    #check right
    if y != 9 and a[x][y+1] == 0:
        h = abs(x-i) + abs(y-j+1)
        f = g + h
        neighbors.append(Node(x-1,y,g,h,f,"right"))

    me = min(neighbors, key=attrgetter('f'))

    c = len(neighbors)
    print(c)
    for i in range(c):
        print(neighbors[i].f, neighbors[i].direction)
    print(me.direction)
print(startrow, startcolumn)
print(endrow, endcolumn)
checkneighbors(startrow,startcolumn,a,endrow,endcolumn,1)
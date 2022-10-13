import queue
import pygame
from binaryHeap import BinaryHeap
import time, pickle, copy

# BLACK = (0, 0, 0)
# WHITE = (200, 200, 200)
# GREEN = (0, 255, 0,)
# BLUE = (0, 0, 255)
# RED = (255, 0, 0)
# YELLOW = (255 ,255 ,0)
# WINDOW_HEIGHT = 300
# WINDOW_WIDTH = 300

# WIDTH = 20
# HEIGHT = 20
# MARGIN = 5
# FPS = 30

# pygame.init()
# pygame.mixer.init()
time_start = time.time()
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255 ,255 ,0)
WINDOW_HEIGHT = 850
WINDOW_WIDTH = 850

WIDTH = 10
HEIGHT = WIDTH
MARGIN = 5
FPS = 30

pygame.init()
pygame.mixer.init()

# Change maze here
MAZE_NUMBER = 0

class Step:

    def __init__(self, x, y, previous) -> None:
        self.x = x
        self.y = y
        self.previous = previous

    def __str__(self) -> str:
        out = "x = " + str(self.x) + ", y= " + str(self.y)
        return out

    def getPrevious(self):
        #print("called")
        return self.previous

'''
a = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '*', ' ', ' '],
    [' ', ' ', '*', '*', ' '],
    [' ', ' ', '*', '*', ' '],
    [' ', ' ', 'S', '*', 'T']
    ]   

'''
# a = [
#     ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
#     ['*', 'S', '*', '*', '*', '*', '*', '*', '*', '*'],
#     ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', '*'],
#     ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', '*'],
#     ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
#     ['*', ' ', '*', '*', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', ' ', ' ', ' ', '*', '*', 'T', '*'],
#     ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*']
# ] 
'''
f = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '*', ' ', ' '],
    [' ', ' ', '*', '*', ' '],
    [' ', ' ', '*', '*', ' '],
    [' ', ' ', 'S', '*', 'T']
    ] 

'''
# f = [
#     ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
#     ['*', 'S', '*', '*', '*', '*', '*', '*', '*', '*'],
#     ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', '*'],
#     ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', '*'],
#     ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
#     ['*', ' ', '*', '*', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', '*', '*', ' ', ' ', ' ', '*', '*', 'T', '*'],
#     ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*']
#     ] 


# h = [['*', ' ', ' ', '*', '*', '*', '*', '*', '*', '*'],
#     ['*', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', ' ', '*', '*', '*', ' ', '*', '*', ' ', '*'],
#     ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
#     ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
#     ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
#     ['*', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*'],
#     ['*', '*', '*', ' ', ' ', '*', '*', '*', 'T', '*'],
#     ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

# start = (1,1)
# end = (7,8)

# start = (4,2)
# end = (4,4)

#print(a[7][8])

# mazes = pickle.load(open("mazes.pkl", "rb"))
# mazes = [pickle.load(open("maze_test.pkl", "rb"))]
mazes = [pickle.load(open("maze_test_60.pkl", "rb"))]
a, start, end = mazes[MAZE_NUMBER][0], mazes[MAZE_NUMBER][1], mazes[MAZE_NUMBER][2]

f = copy.deepcopy(a)

block = {}
closed = {}
hval = {}
seen = {}
gval = {}
finalPath = []

for i in a:
    for j in i:
        print(j,end="")
    print("\n",end='')


def isClear(x, y):
    #print("here at : ",x,y)
    if ((y >= 0 and y < len(a[0])) and (x >= 0 and x < len(a))):
        #print("in if here")
        #print(block)
        if ( (not block.get((x,y))) and not closed.get((x,y))) :
            #print("in if if here")
            return True
    #print("false")
    return False

def getBlockers(it):

    if ((it.y >= 0 and it.y < len(a[0])) and (it.x+1 >= 0 and it.x+1 < len(a))):
        if(a[it.x+1][it.y] == "*"):
            block[(it.x+1,it.y)] = True

    if ((it.y >= 0 and it.y < len(a[0])) and (it.x-1 >= 0 and it.x-1 < len(a))):
        if(a[it.x-1][it.y] == "*"):
            block[(it.x-1,it.y)] = True

    if ((it.y+1 >= 0 and it.y+1 < len(a[0])) and (it.x >= 0 and it.x < len(a))):
        if(a[it.x][it.y+1] == "*"):
            block[(it.x,it.y+1)] = True

    if ((it.y-1 >= 0 and it.y-1 < len(a[0])) and (it.x >= 0 and it.x < len(a))):
        if(a[it.x][it.y-1] == "*"):
            block[(it.x,it.y-1)] = True

    #print(block)

def calcHeuristic():
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            h[i][j] = abs(end[0]-i) + abs(end[1]-j)
    
    return 

def calcHval(point):
    #print("h calc: ",point.x, point.y)
    if(hval.get((point.x, point.y))):
        return hval.get((point.x, point.y))

    #print("hval")
    hval[(point.x, point.y)] = abs(end[0]-point.x) + abs(end[1]-point.y)
    return hval[(point.x, point.y)]

def findAstar(point):

    closed.clear()
    getBlockers(point)
    q1 = BinaryHeap()
    # q1 = queue.PriorityQueue()
    hval = calcHval(point)
    cost = hval + gval[(point.x,point.y)]
    #print("cost: ",cost)
    q1.push((cost, time.time(), point))

    while q1.size > 0:
        # print("A star iteration start")
        #print("new queue")
        current = q1.pop()[2]
        closed[(current.x,current.y)] = True
        if a[current.x][current.y] == 'T' :
            print("target found")
            return current
        
        #a[current.x][current.y] = 'R'
        #print("cord: ",current.x, " ", current.y)
        if(isClear(current.x+1, current.y)):
            s1 = Step(current.x+1, current.y, current)
            hval = calcHval(s1)
            #print(hval)
            cost = hval + gval[(current.x,current.y)]+1
            gval[(current.x+1,current.y)] = gval[(current.x,current.y)]+1
            #print("cost at ",current.x+1,", ",current.y, " : ",cost)
            q1.push((cost,time.time(), Step(current.x+1, current.y, current)))
            seen[(current.x+1,current.y)] = True

        if(isClear(current.x-1, current.y)):
            s1 = Step(current.x-1, current.y, current)
            hval = calcHval(s1)
            cost = hval + gval[(current.x,current.y)]+1
            gval[(current.x-1,current.y)] = gval[(current.x,current.y)]+1
            #print("cost at ",current.x-1,", ",current.y, " : ",cost)
            q1.push((cost,time.time(), Step(current.x-1, current.y, current)))
            seen[(current.x-1,current.y)] = True

        if(isClear(current.x, current.y+1)):
            s1 = Step(current.x, current.y+1, current)
            hval = calcHval(s1)
            cost = hval + gval[(current.x,current.y)]+1
            gval[(current.x,current.y+1)] = gval[(current.x,current.y)]+1
            #print("cost at ",current.x,", ",current.y+1, " : ",cost)
            q1.push((cost,time.time(), Step(current.x, current.y+1, current)))
            seen[(current.x,current.y+1)] = True
        
        if(isClear(current.x, current.y-1)):
            s1 = Step(current.x, current.y-1, current)
            hval = calcHval(s1)
            cost = hval + gval[(current.x,current.y)]+1
            gval[(current.x,current.y-1)] = gval[(current.x,current.y)]+1
            #print("cost at ",current.x,", ",current.y-1, " : ",cost)
            q1.push((cost,time.time(), Step(current.x, current.y-1, current)))
            seen[(current.x,current.y-1)] = True
    
    return

def printprog(res):
    li = []
    while (res.getPrevious()) :
        #print('works')
        #print(res)
        li.append((res.x,res.y))
        #f[res.x][res.y] = ""
        res = res.getPrevious()
    #print(res)
    li.append((res.x,res.y))
    li.reverse()      
    print(li)
    # time.sleep(0.1)
    for i in li:
      pygame.draw.rect(SCREEN,
                      GREEN,
                      [(MARGIN + WIDTH) * i[1] + MARGIN + MARGIN-2,
                      (MARGIN + HEIGHT) * i[0] + MARGIN + MARGIN-2,
                      WIDTH-8,
                      HEIGHT-8])
    pygame.display.update()

    ci = 0
    #print(li)
    for i in li:
        x = i[0]
        y = i[1]
        #print(x," ",y)
        if(f[x][y]) != "*":
            f[x][y] = "\033[1;32;43mS"
            tu = (x,y)
            if(ci > 0):
                f[prevx][prevy] = "\033[1;32;43m "
            prevx = x
            prevy = y
        else:
            break
        ci = ci+1

    countx = 0
    print(seen)
    for e in f:
        county = 0
        for r in e:
            if((countx, county) in block or (countx, county) in seen):
                print("\033[1;34;40m",r,end="")

            else:
                print("\033[0;37;41m",r,end="")
            county = county+1
        print("\033[0;37;40m\n",end='')
        countx = countx+1
    
    
    for i in li:
      pygame.draw.rect(SCREEN,
                          BLUE,
                          [(MARGIN + WIDTH) * i[1] + MARGIN + MARGIN-2,
                          (MARGIN + HEIGHT) * i[0] + MARGIN + MARGIN-2,
                          WIDTH-8,
                          HEIGHT-8])
      
      pygame.display.update()
    #   time.sleep(0.1)
      if(i[0] == tu[0] and i[1] == tu[1]):
        break
      finalPath.append(i)
    
    a[new[0]][new[1]] = " "
    a[tu[0]][tu[1]] = "S"
    return tu



# pygame.init()
# pygame.mixer.init()
# SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# SCREEN.fill(BLACK)
# drawGrid()
# pygame.display.update()
# print("here")


def drawGrid():

    for row in range(len(a)):
        for column in range(len(a[0])):
            color = WHITE
            if a[row][column] == '*':
                color = RED
            if a[row][column] == 'S':
                color = BLUE
            if a[row][column] == 'T':
                color = YELLOW
            pygame.draw.rect(SCREEN,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
        


SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()
SCREEN.fill(BLACK)
# drawGrid()
# pygame.display.update()
# print("here")

out = Step(start[0],start[1], None)
new = start
while(out != end):
    drawGrid()
    pygame.display.update()
    print("here")
    it = Step(new[0],new[1], None)
    gval[(it.x,it.y)] = 0
    res = findAstar(it)
    new  = printprog(res)
    print(new)
    out = new

drawGrid()
pygame.display.update()
finalPath.append(out)
for i in finalPath:
    pygame.draw.rect(SCREEN,
                          GREEN,
                          [(MARGIN + WIDTH) * i[1] + MARGIN + 3,
                          (MARGIN + HEIGHT) * i[0] + MARGIN + 3,
                          WIDTH-8,
                          HEIGHT-8])
    pygame.display.update()
pygame.display.update()
print(finalPath)

# ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


print("time taken: ",time.time()-start_time)
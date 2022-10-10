import queue
from re import S
from time import time

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
a = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', 'S', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', '*'],
    ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', '*'],
    ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
    ['*', ' ', '*', '*', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', '*', '*', ' ', ' ', ' ', '*', '*', 'T', '*'],
    ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*']
]

f = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', 'S', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', '*'],
    ['*', ' ', '*', '*', '*', '*', '*', '*', ' ', '*'],
    ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
    ['*', ' ', '*', '*', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', '*', '*', ' ', ' ', ' ', '*', '*', 'T', '*'],
    ['*', '*', '*', '*', ' ', ' ', ' ', ' ', ' ', '*']
    ] 

'''

h = [['*', ' ', ' ', '*', '*', '*', '*', '*', '*', '*'],
    ['*', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', '*', '*', '*', ' ', '*', '*', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
    ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*'],
    ['*', '*', '*', ' ', ' ', '*', '*', '*', 'T', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

f = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '*', ' ', ' '],
    [' ', ' ', '*', '*', ' '],
    [' ', ' ', '*', '*', ' '],
    [' ', ' ', 'S', '*', 'T']
    ] 
'''

start = (1,1)
end = (7,8)
#start = (4,2)
#end = (4,4)

#print(a[7][8])

block = {}
closed = {}
hval = {}
seen = {}
gval = {}

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
    q1 = queue.PriorityQueue()
    hval = calcHval(point)
    cost = hval + gval[(point.x,point.y)]
    #print("cost: ",cost)
    q1.put((cost, time(), point))

    while q1:
        #print("new queue")
        current = q1.get()[2]
        closed[(current.x,current.y)] = True
        #print(current.x, current.y, len(a), len(a[0]))
        if a[current.x][current.y] == 'T' :
            print("target found")
            return current
        
        #a[current.x][current.y] = 'R'
        #print("cord: ",current.x, " ", current.y)
        if(isClear(current.x+1, current.y)):
            #a[current.x+1][current.y] = 'R'
            s1 = Step(current.x+1, current.y, current)
            hval = calcHval(s1)
            #print(hval)
            cost = hval + gval[(current.x,current.y)]+1
            gval[(current.x+1,current.y)] = gval[(current.x,current.y)]+1
            #print("cost at ",current.x+1,", ",current.y, " : ",cost)
            q1.put((cost,time(), Step(current.x+1, current.y, current)))
            seen[(current.x+1,current.y)] = True

        if(isClear(current.x-1, current.y)):
            s1 = Step(current.x-1, current.y, current)
            hval = calcHval(s1)
            cost = hval + gval[(current.x,current.y)]+1
            gval[(current.x-1,current.y)] = gval[(current.x,current.y)]+1
            #print("cost at ",current.x-1,", ",current.y, " : ",cost)
            q1.put((cost,time(), Step(current.x-1, current.y, current)))
            seen[(current.x-1,current.y)] = True

        if(isClear(current.x, current.y+1)):
            s1 = Step(current.x, current.y+1, current)
            hval = calcHval(s1)
            cost = hval + gval[(current.x,current.y)]+1
            gval[(current.x,current.y+1)] = gval[(current.x,current.y)]+1
            #print("cost at ",current.x,", ",current.y+1, " : ",cost)
            q1.put((cost,time(), Step(current.x, current.y+1, current)))
            seen[(current.x,current.y+1)] = True
        
        if(isClear(current.x, current.y-1)):
            s1 = Step(current.x, current.y-1, current)
            hval = calcHval(s1)
            cost = hval + gval[(current.x,current.y)]+1
            gval[(current.x,current.y-1)] = gval[(current.x,current.y)]+1
            #print("cost at ",current.x,", ",current.y-1, " : ",cost)
            q1.put((cost,time(), Step(current.x, current.y-1, current)))
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
    ggoal = len(li) - 1
    print(hval)
    for key in hval.keys():
        hval[key] = abs(ggoal - gval[key])
    print("new h val: ", ggoal)
    print(hval)
    li.reverse()
    ci = 0
    #print(li)
    for i in li:
        x = i[0]
        y = i[1]
        #print(x," ",y)
        if(f[x][y]) != "*":
            f[x][y] = "\033[1;32;43mB"
            tu = (x,y)
            if(ci > 0):
                f[prevx][prevy] = "\033[1;32;43m "
            prevx = x
            prevy = y
        else:
            break
        ci = ci+1

    countx = 0
    #print(seen)
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
    
    return tu
        


#print(id(a))
#print(id(f))
#print(id(h))
out = Step(start[0],start[1], None)
new = start
while(out != end):
    it = Step(new[0],new[1], None)
    gval[(it.x,it.y)] = 0
    res = findAstar(it)
    new  = printprog(res)
    print(new)
    out = new
'''
it = Step(new[0],new[1], None)
res = findAstar(it)
new  = printprog(res)
print(new)
out = new
it = Step(new[0],new[1], None)
res = findAstar(it)
new  = printprog(res)
print(new)
out = new
it = Step(new[0],new[1], None)
res = findAstar(it)
new  = printprog(res)
print(new)
out = new
it = Step(new[0],new[1], None)
res = findAstar(it)
new  = printprog(res)
print(new)
out = new
it = Step(new[0],new[1], None)
res = findAstar(it)
new  = printprog(res)
print(new)
out = new

# it = Step(new[0],new[1], None)
# res = findAstar(it)
# new = printprog(res)
# print(new)
# it = Step(new[0],new[1], None)
# res = findAstar(it)
# new = printprog(res)
# print(new)
# it = Step(new[0],new[1], None)
# res = findAstar(it)
# new = printprog(res)
# print(new)
# it = Step(new[0],new[1], None)
# res = findAstar(it)
# new = printprog(res)
# print(new)

'''

'''

li = []

while (res.getPrevious()) :
    #print('works')
    print(res)
    li.append((res.x,res.y))
    #f[res.x][res.y] = 'B'
    res = res.getPrevious()
print(res)
li.append((res.x,res.y))
li.reverse()
        '''



import queue

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


a = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', 'S', '*', '*', '*', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', '*', '*', '*', ' ', '*', ' ', ' ', '*'],
    ['*', ' ', '*', '*', '*', ' ', '*', '*', ' ', '*'],
    ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
    ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*'],
    ['*', '*', '*', ' ', ' ', '*', '*', '*', 'T', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
]

h = a

start = (1,1)
end = (7,8)

print(a[7][8])

for i in a:
    for j in i:
        print(j,end="")
    print("\n",end='')

def isClear(x, y):
    if ((y >= 0 and y < len(a)) and (x >= 0 and x < len(a[0]))):
        if (a[x][y] == ' ' or a[x][y] == 'T') :
            return True

    return False


def findPath(path):

    q1 = queue.Queue()
    q1.put(path)
    #visited = []
    #visited.append(path)
    #neighbours = ['u', 'd', 'l', 'r']

    while queue:
        #print("new queue")
        current = q1.get()
        if a[current.x][current.y] == 'T' :
            print("target found")
            return current;

        if(isClear(current.x+1, current.y)):
            a[current.x][current.y] = 'R'
            q1.put(Step(current.x+1, current.y, current))

        if(isClear(current.x-1, current.y)):
            a[current.x][current.y] = 'R'
            q1.put(Step(current.x-1, current.y, current))

        if(isClear(current.x, current.y+1)):
            a[current.x][current.y] = 'R'
            q1.put(Step(current.x, current.y+1, current))
        
        if(isClear(current.x, current.y-1)):
            a[current.x][current.y] = 'R'
            q1.put(Step(current.x, current.y-1, current))

    return

def calcHeuristic():
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            h[i][j] = abs(end[0]-i) + abs(end[1]-j)
    
    return 
            

'''
def findAstar(point):

    calcHeuristic() '''


begin = Step(start[0],start[1], None)
out = findPath(begin)
#calcHeuristic()

for i in a:
    for j in i:
        print(j,end="")
    print("\n",end='')

calcHeuristic()
for i in h:
    for j in i:
        print(j,end=", ")
    print("\n",end='')

#print(out) 
'''
if(out.getPrevious() == None):
    print("working")
while (out.getPrevious()) :
    #print('works')
    print(out)
    out = out.getPrevious()'''




    






# Function for A star algorithm in gridworld
# %%
import queue, pygame, time, copy
import math, pickle

# %%
pygame.quit()
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

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()
SCREEN.fill(BLACK)

def drawGrid(a):

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
    pygame.display.update()

# %%
# function to calculate the manhattan distance

def manhattanDistance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def getNeighbours(grid_dim, pos):
    neighbours = []
    
    if pos[0] > 0:
        neighbours.append((pos[0] - 1, pos[1]))
    if pos[0] < grid_dim[0]:
        neighbours.append((pos[0], pos[1] + 1))
    if pos[1] > 0:
        neighbours.append((pos[0], pos[1] - 1))
    if pos[1] < grid_dim[1]:
        neighbours.append((pos[0] + 1, pos[1]))
    
    return neighbours

# %%

# Function to implement A* search algorithm


class aStar:
    def __init__(self, grid, known, start, goal, seen):
        """
            Function that calculates the shortest path from start to goal given a grid and the known world
            known contains h value for each cell
            If a cell is an obstacle, the h value becomes infinity, 

            Args:
                grid (list): grid 
                known (list): known grid
                start (tuple): start coordinates
                goal (tuple): goal coordinates
        """    
        self.grid_dim = (len(grid[0]), len(grid))
        self.openList = queue.PriorityQueue()   
        self.closedList = []
        self.known = known
        self.grid = grid
        self.openList.put((0, start, []))
        self.path = []
        self.seen = seen
        # self.block = block
        # g Values
        

    def run(self):    
        gMatrix = [[0 for i in range(len(self.grid[0]))] for j in range(len(self.grid))]
        while self.openList.empty() == False:
        # for i in range(20):
            # print("Open List is", self.openList.queue)
            # print("Closed List is", self.closedList)
            _, current, history = self.openList.get()
            # print("Agent is at", current)
            neighbours = getNeighbours(self.grid_dim, current)
            self.seen.extend(neighbours)
            # Observe surroundings
            for i in range(len(neighbours)):
                # print(neighbours[i])
                if neighbours[i] == goal:
                    # print("Found goal")
                    #TODO: Return path
                    history.extend([current, goal])
                    self.path = history
                    return sorted(set(self.path), key=self.path.index)
                    # return self.path
                
                # # update obstacle values
                # if self.grid[neighbours[i][0]][neighbours[i][1]] == "*":
                #     self.known[neighbours[i][0]][neighbours[i][1]] = math.inf
                g = gMatrix[current[0]][current[1]] + 1
                h = known[neighbours[i][0]][neighbours[i][1]]
                f = g + h
                if f == math.inf:
                    continue
                present, f_check = self.checkCellInOpenList(neighbours[i])
                # print("Checking open list")
                if present:
                    if f >= f_check:
                        continue
                
                present, f_check = self.checkCellInClosedList(neighbours[i])
                # print("Checking closed list")
                if present:
                    # print(neighbours[i], "present in closed list", f, f_check)
                    if f >= f_check:
                        # print("Adding ", neighbours[i], "with f =", f_check, f,"to open list")
                        continue    
                # print("Adding ", neighbours[i], "with f =", f,"to open list")
                history.append(current)
                self.openList.put((f, neighbours[i], history))
                gMatrix[neighbours[i][0]][neighbours[i][1]] = g    
                
            self.closedList.append((gMatrix[current[0]][current[1]], current))

    
    def checkCellInOpenList(self, pos):
        for i in self.openList.queue:
            if i[1] == pos:
                return True, i[0]
        return False, 0
    
    def checkCellInClosedList(self, pos):
        for i in self.closedList:
            if i[1] == pos:
                return True, i[0]
        return False, 0
    
    
    

# %%
class RepeatedAstar:
    
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.current = start
        self.goal = goal
        self.known = [[manhattanDistance((j, i), goal) for i in range(len(grid[0]))] for j in range(len(grid))]
        # self.path = [start]
        self.currAstarPath = None
        self.path = []
        self.new_grid = copy.deepcopy(grid)
        self.seen = []
        self.block = []
        self.final_path = []
        # self.stop_points = []
    
    def runAstar(self):
        
        neighbours = getNeighbours((len(self.grid), len(self.grid[0])), self.current)
        print(neighbours)
        for i in range(len(neighbours)):    
            if self.grid[neighbours[i][0]][neighbours[i][1]] == "*":
                self.known[neighbours[i][0]][neighbours[i][1]] = math.inf
                self.block.append(neighbours[i])
            
        while self.current != self.goal:
            drawGrid(self.grid)
            pygame.display.update()
            print("Agent is at", self.current)
            self.path.append(self.current)
            # print(known)
            pathFinder = aStar(self.grid, self.known, self.current, self.goal, self.seen)
            self.seen = pathFinder.seen
            self.currAstarPath = pathFinder.run()
            self.current = self.currAstarPath[1]
            self.display()
            # return
            
        print("Reached goal")
        
    def display(self):

        drawGrid(self.grid)
        li = self.currAstarPath
        print(li)
        for i in li:
            pygame.draw.rect(SCREEN,
                             GREEN,
                             [(MARGIN + WIDTH) * i[1] + MARGIN,
                              (MARGIN + HEIGHT) * i[0] + MARGIN,
                              WIDTH-3,
                              HEIGHT-3])
            # pygame.draw.rect(SCREEN,
            #                 GREEN,
            #                 [(MARGIN + WIDTH) * i[1] + MARGIN + MARGIN-2,
            #                 (MARGIN + HEIGHT) * i[0] + MARGIN + MARGIN-2,
            #                 WIDTH-8,
            #                 HEIGHT-8])
        pygame.display.update()
        ci = 0
        print(li)
        for i in li:
            x = i[0]
            y = i[1]
            print(x," ",y)
            if(self.new_grid[x][y]) != "*":
                self.new_grid[x][y] = "\033[1;32;43mS"
                tu = (x,y)
                if(ci > 0):
                    self.new_grid[prevx][prevy] = "\033[1;32;43m "
                prevx = x
                prevy = y
            else:
                break
            ci = ci+1
        print(tu)
        countx = 0
        seen = self.seen
        block = self.block
        final_path = self.path
        print(seen)
        for e in self.new_grid:
            county = 0
            for r in e:
                if((countx, county) in block or (countx, county) in seen):
                    print("\033[1;34;40m",r,end="")

                else:
                    print("\033[0;37;41m",r,end="")
                county = county+1
            print("\033[0;37;40m\n",end='')
            countx = countx+1
        print(li)
        for i in li:
            pygame.draw.rect(SCREEN,
                                BLUE,
                                [(MARGIN + WIDTH) * i[1] + MARGIN,
                                (MARGIN + HEIGHT) * i[0] + MARGIN,
                                WIDTH,
                                HEIGHT])
            
            pygame.display.update()
            #   time.sleep(0.1)
            if(i[0] == tu[0] and i[1] == tu[1]):
                break
            
        self.grid[self.current[0]][self.current[1]] = " "
        self.grid[tu[0]][tu[1]] = "S"
        return tu
    

# %%
# a = [
#     ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
#     ['*', 'S', '*', '*', '*', ' ', ' ', ' ', ' ', '*'],
#     ['*', ' ', '*', '*', '*', ' ', '*', ' ', ' ', '*'],
#     ['*', ' ', '*', '*', '*', ' ', '*', '*', ' ', '*'],
#     ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
#     ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*'],
#     ['*', ' ', ' ', ' ', ' ', '*', '*', '*', ' ', '*'],
#     ['*', '*', '*', ' ', ' ', '*', '*', '*', 'T', '*'],
#     ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
# ]
# start = (1, 1)
# goal = (7, 8)

mazes = pickle.load(open('mazes.pkl', 'rb'))
mazes = [pickle.load(open('maze_test.pkl', 'rb'))]
a, start, goal = mazes[0]

known = [[manhattanDistance((j, i), goal) for i in range(len(a[0]))] for j in range(len(a))]
# known

# %%
# start, goal

# %%
# # Test A star
# known = [[manhattanDistance((j, i), goal) for i in range(len(a[0]))] for j in range(len(a))]
# test = aStar(a, known, start, goal)
# test.run()

# %%
x = RepeatedAstar(a, start, goal)
x.runAstar()



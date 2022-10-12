import math

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


class BinaryHeap:
    def __init__(self):
        self.size = 0
        self.heap = [0]
        # self.heap[0] = -1 * math.inf
        
    def push(self, k):
        self.heap.append(k)
        self.size += 1
        self.percUp(self.size)
        
    def remove(self, i):
        for item in self.heap:
            if i == item:
                self.heap.remove(i)
                self.size -= 1
                self.percDown(1)
                
        
    def peek(self):
        return self.heap[1]
        
    def pop(self):
        root = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.percDown(1)
        return root
        
    def percUp(self, i):
        while i//2 > 0:
            # print(i)
            parent_index = i//2
            # print(self.heap, self.heap[parent_index], self.heap[i])
            if self.heap[i] < self.heap[parent_index]:
                self.heap[i], self.heap[parent_index] = self.heap[parent_index], self.heap[i]
            i = parent_index
            
    def percDown(self, i):
        while (i * 2) <= self.size:
            child = i*2
            if child + 1 <= self.size and self.heap[child + 1] < self.heap[child]:
                child = 2*i + 1
            if self.heap[i] > self.heap[child]:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child
            
            

from collections import defaultdict
import copy

class Vertex:
    def __init__(self, id):
        self.ID = id
        self.distance = -1
        self.neighbors = []
        self.path = [id]

class Graph:
    def __init__(self, length):
        self.V = length - 1
        self.graph = [None]*length

    def addVertex(self, id):
        self.graph[id] = Vertex(id)

    def addEdge(self, curr, next):
        self.graph[curr].neighbors.append(self.graph[next])

    def BFS(self, start):
        queue = []
        queue.append(self.graph[start])
        self.graph[start].distance = 0
        while len(queue) != 0:
            currentVertex = queue.pop(0)
            for neighbor in currentVertex.neighbors:
                if neighbor.distance == -1:
                    neighbor.distance = currentVertex.distance + 1
                    neighbor.path += currentVertex.path
                    queue.append(neighbor)
        return 'No path'

    def DFS(self, current):
        currentVertex = self.graph[current]
        currentVertex.distance = 0
        for neighbor in currentVertex.neighbors:
            if neighbor.distance == -1:
                neighbor.distance = currentVertex.distance + 1
                neighbor.path += currentVertex.path
                self.DFS(neighbor.ID)

    def printPath(self, end):
        for i in reversed(self.graph[end].path):
            print i

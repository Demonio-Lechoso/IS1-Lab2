from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}
    
    def add_edge(self, vertex1, vertex2, cost):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = cost
            self.vertices[vertex2][vertex1] = cost
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            del self.vertices[vertex1][vertex2]
            del self.vertices[vertex2][vertex1]
    
    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            for v in self.vertices:
                if vertex in self.vertices[v]:
                    del self.vertices[v][vertex]
    
    def __str__(self):
        result = ""
        for vertex in self.vertices:
            result += str(vertex) + " -> " + str(self.vertices[vertex]) + "\n"
        return result

    def dfs(self, start_vertex, goal_vertex):
        explored = set()
        stack = [(start_vertex, None)]

        while stack:
            current_vertex, parent_vertex = stack.pop()

            if current_vertex in explored:
                continue

            explored.add(current_vertex)

            if current_vertex == goal_vertex:
                return self.construct_path(start_vertex, goal_vertex, {start_vertex: None, goal_vertex: parent_vertex})
            
            for neighbor in self.vertices[current_vertex]:
                if neighbor not in explored:
                    stack.append((neighbor, current_vertex))

        return None
    
    def bfs(self, start_vertex, goal_vertex):
        explored = set()
        queue = deque([(start_vertex, None)])

        while queue:
            current_vertex, parent_vertex = queue.popleft()

            if current_vertex in explored:
                continue

            explored.add(current_vertex)

            if current_vertex == goal_vertex:
                return self.construct_path(start_vertex, goal_vertex, {start_vertex: None, goal_vertex: parent_vertex})
            
            for neighbor in self.vertices[current_vertex]:
                if neighbor not in explored:
                    queue.append((neighbor, current_vertex))
                    
        return None
    
    def construct_path(self, start_vertex, goal_vertex, parents):
        path = []
        current_vertex = goal_vertex
        while current_vertex != start_vertex:
            path.append(current_vertex)
            current_vertex = parents[current_vertex]
        path.append(start_vertex)
        path.reverse()
        return path
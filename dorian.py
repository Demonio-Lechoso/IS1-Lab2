from PriorityQueue import PriorityQueue
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
        stack = [start_vertex]
        parents = {start_vertex: None}

        while stack:
            current_vertex = stack.pop()
            print(current_vertex)

            if current_vertex in explored:
                continue

            explored.add(current_vertex)

            if current_vertex == goal_vertex:
                return self.construct_path(start_vertex, goal_vertex, parents)
            
            for neighbor in self.vertices[current_vertex]:
                if neighbor not in explored:
                    parents[neighbor] = current_vertex
                    stack.append(neighbor)

        return None
    
    def bfs(self, start_vertex, goal_vertex):
        explored = set()
        queue = deque([start_vertex])
        parents = {start_vertex: None}

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)

            if current_vertex in explored:
                continue

            explored.add(current_vertex)

            if current_vertex == goal_vertex:
                return self.construct_path(start_vertex, goal_vertex, parents)
            
            for neighbor in self.vertices[current_vertex]:
                if neighbor not in explored:
                    parents[neighbor] = current_vertex
                    queue.append(neighbor)
                    
        return None

    def greedy_search(self, start_vertex, goal_vertex, heuristic):
        explored = set()
        priorityQueue = PriorityQueue()
        priorityQueue.put((heuristic[start_vertex], start_vertex))
        parents = {start_vertex: None}
        while not priorityQueue.empty():
            current_vertex = priorityQueue.get()[1]
            print(current_vertex)
            if current_vertex in explored:
                continue

            explored.add(current_vertex)

            if current_vertex == goal_vertex:
                return self.construct_path(start_vertex, goal_vertex, parents)

            for neighbor in self.vertices[current_vertex]:
                if neighbor not in explored:
                    parents[neighbor] = current_vertex
                    priorityQueue.put((heuristic[neighbor], neighbor))

        return None

    def a_star_search(self, start_vertex, goal_vertex, heuristic):
        explored = set()
        priorityQueue = PriorityQueue()
        priorityQueue.put((0, start_vertex))
        g_scores = {start_vertex: 0}
        parents = {start_vertex: None}

        while not priorityQueue.empty():
            current_vertex = priorityQueue.get()[1]

            if current_vertex == goal_vertex:
                return self.construct_path(start_vertex, goal_vertex, parents)
            
            explored.add(current_vertex)

            for neighbor in self.vertices[current_vertex]:
                if neighbor in explored:
                    continue

                tentative_g_score = g_scores[current_vertex] + self.vertices[current_vertex][neighbor]
                if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                    parents[neighbor] = current_vertex
                    g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic[neighbor]
                    priorityQueue.put((f_score, neighbor))
        
        return None
    
    def construct_path(self, start_vertex, goal_vertex, parents):
        print(parents)
        path = []
        current_vertex = goal_vertex
        while current_vertex != start_vertex:
            path.append(current_vertex)
            current_vertex = parents[current_vertex]
        path.append(start_vertex)
        path.reverse()
        return path
    
def test_dfs():    
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 1)
    graph.add_edge("B", "D", 1)
    graph.add_edge("C", "E", 1)
    graph.add_edge("D", "F", 1)
    #graph.add_edge("E", "F", 1)

    path = graph.dfs("A", "F")
    print(path)
    assert path == ["A", "B", "D", "F"]

def test_bfs():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 1)
    graph.add_edge("B", "D", 1)
    graph.add_edge("C", "E", 1)
    graph.add_edge("D", "F", 1)
    graph.add_edge("E", "F", 1)

    path = graph.bfs("A", "F")
    print(path)
    assert path == ["A", "C", "E", "F"]

def test_greedy_search():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 1)
    graph.add_edge("B", "D", 1)
    graph.add_edge("C", "E", 5)
    graph.add_edge("D", "F", 1)
    graph.add_edge("E", "F", 1)

    heuristics = {
        "A": 3,
        "B": 2,
        "C": 6,
        "D": 1,
        "E": 1,
        "F": 0
    }

    path = graph.greedy_search("A", "F", heuristics)
    print(path)
    assert path == ["A", "B", "D", "F"]

def test_a_star():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 1)
    graph.add_edge("B", "D", 1)
    graph.add_edge("C", "E", 5)
    graph.add_edge("D", "F", 1)
    graph.add_edge("E", "F", 1)

    heuristics = {
        "A": 3,
        "B": 2,
        "C": 6,
        "D": 1,
        "E": 1,
        "F": 0
    }

    path = graph.a_star_search("A", "F", heuristics)
    print(path)
    assert path == ["A", "B", "D", "F"]

#test_dfs()
test_bfs()
#test_greedy_search()
#test_a_star()
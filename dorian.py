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
        i = 0
        while stack:
            current_vertex = stack.pop()

            i+=1
            print(i, ": ", current_vertex)

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
        i = 0
        while queue:
            current_vertex = queue.popleft()

            i+=1
            print(i, ": ", current_vertex)

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
        i = 0

        while not priorityQueue.empty():
            current_vertex = priorityQueue.get()[1]

            i+=1
            print(i, ": ", current_vertex)

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
        i = 0

        while not priorityQueue.empty():
            current_vertex = priorityQueue.get()[1]

            i+=1
            print(i, ": ", current_vertex)

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
        path = []
        total_cost = 0
        current_vertex = goal_vertex
        while current_vertex != start_vertex:
            path.append(current_vertex)
            parent_vertex = parents[current_vertex]
            total_cost+= self.vertices[current_vertex][parent_vertex]
            current_vertex = parent_vertex
        path.append(start_vertex)
        path.reverse()
        return path, total_cost

def luxembourg_railway():
    graph = Graph()

    cities = [
        "Luxembourg", "Ettelbruck", "Diekirch", "Wasserbillig", "Differdange", "Esch-sur-Alzette",
        "Rodange", "Pétange", "Schifflange", "Bettembourg", "Mersch", "Troisvierges"
    ]

    for city in cities:
        graph.add_vertex(city)

    connections = [
        ("Luxembourg", "Ettelbruck", 37),
        ("Luxembourg", "Wasserbillig", 34),
        ("Luxembourg", "Bettembourg", 17),
        ("Ettelbruck", "Diekirch", 10),
        ("Ettelbruck", "Mersch", 24),
        ("Mersch", "Luxembourg", 19),
        ("Wasserbillig", "Diekirch", 35),
        ("Wasserbillig", "Bettembourg", 31),
        ("Diekirch", "Troisvierges", 46),
        ("Bettembourg", "Esch-sur-Alzette", 13),
        ("Esch-sur-Alzette", "Schifflange", 4),
        ("Esch-sur-Alzette", "Differdange", 16),
        ("Esch-sur-Alzette", "Pétange", 17),
        ("Pétange", "Rodange", 4),
        ("Differdange", "Rodange", 12),
        ("Differdange", "Pétange", 13),
        ("Schifflange", "Bettembourg", 11),
    ]

    for connection in connections:
        graph.add_edge(connection[0], connection[1], connection[2])

    heuristics = {
        "Luxembourg": 93,
        "Ettelbruck": 56,
        "Diekirch": 46,
        "Wasserbillig": 81,
        "Differdange": 141,
        "Esch-sur-Alzette": 125,
        "Rodange": 146,
        "Pétange": 142,
        "Schifflange": 123,
        "Bettembourg": 112,
        "Mersch": 80,
        "Troisvierges": 0,
    }

    return graph, heuristics

def test1_luxembourg_railway():
    graph, heuristics = luxembourg_railway()
    start_station = "Esch-sur-Alzette"

    print("\nLuxembourg Railway Test\nEsch-sur-Alzette to Troisvierges")
    print("\nDFS:")
    path_dfs, total_cost = graph.dfs(start_station, "Troisvierges")
    print("Path: ", path_dfs)
    print("Total cost:", total_cost)

    print("\nBFS:")
    path_bfs, total_cost = graph.bfs(start_station, "Troisvierges")
    print("Path: ", path_bfs)
    print("Total cost:", total_cost)

    print("\nGreedy Search:")
    path_greedy, total_cost = graph.greedy_search(start_station, "Troisvierges", heuristics)
    print("Path: ", path_greedy)
    print("Total cost:", total_cost)

    print("\nA* Search:")
    path_a_star, total_cost = graph.a_star_search(start_station, "Troisvierges", heuristics)
    print("Path: ", path_a_star)
    print("Total cost:", total_cost)

def test2_luxembourg_railway():
    graph, heuristics = luxembourg_railway()
    start_station = "Luxembourg"

    print("\nLuxembourg Railway Test 2\nLuxembourg to Troisvierges")
    print("\nDFS:")
    path_dfs, total_cost = graph.dfs(start_station, "Troisvierges")
    print("Path: ", path_dfs)
    print("Total cost:", total_cost)

    print("\nBFS:")
    path_bfs, total_cost = graph.bfs(start_station, "Troisvierges")
    print("Path: ", path_bfs)
    print("Total cost:", total_cost)

    print("\nGreedy Search:")
    path_greedy, total_cost = graph.greedy_search(start_station, "Troisvierges", heuristics)
    print("Path: ", path_greedy)
    print("Total cost:", total_cost)

    print("\nA* Search:")
    path_a_star, total_cost = graph.a_star_search(start_station, "Troisvierges", heuristics)
    print("Path: ", path_a_star)
    print("Total cost:", total_cost)

def test3_luxembourg_railway():
    graph, heuristics = luxembourg_railway()
    start_station = "Bettembourg"

    print("\nLuxembourg Railway Test 3\nBettembourg to Troisvierges")
    print("\nDFS:")
    path_dfs, total_cost = graph.dfs(start_station, "Troisvierges")
    print("Path: ", path_dfs)
    print("Total cost:", total_cost)

    print("\nBFS:")
    path_bfs, total_cost = graph.bfs(start_station, "Troisvierges")
    print("Path: ", path_bfs)
    print("Total cost:", total_cost)

    print("\nGreedy Search:")
    path_greedy, total_cost = graph.greedy_search(start_station, "Troisvierges", heuristics)
    print("Path: ", path_greedy)
    print("Total cost:", total_cost)

    print("\nA* Search:")
    path_a_star, total_cost = graph.a_star_search(start_station, "Troisvierges", heuristics)
    print("Path: ", path_a_star)
    print("Total cost:", total_cost)


test1_luxembourg_railway()
test2_luxembourg_railway()
test3_luxembourg_railway()

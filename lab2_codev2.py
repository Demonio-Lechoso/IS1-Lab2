graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': []
}

# DFS with generator function for DFS that yields paths as they are found.
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        node, path = stack.pop()
        if node == goal:
            yield path
        for neighbor in graph[node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

def dfs(graph, start, goal):
    return next(dfs_paths(graph, start, goal), None)


# BFS with generator function for BFS that yields paths as they are found.
from collections import deque

def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == goal:
            yield path
        for neighbor in graph[node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

def bfs(graph, start, goal):
    return next(bfs_paths(graph, start, goal), None)


# A* heapq library to handle the priority queue,
# but we will store a dictionary of visited nodes to avoid visiting the same node multiple times.
import heapq

def a_star(graph, start, goal, heuristic):
    open_set = [(heuristic[start], start, [start])]
    visited = set()

    while open_set:
        cost, node, path = heapq.heappop(open_set)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(open_set, (heuristic[neighbor] + len(path), neighbor, path + [neighbor]))

    return None


# Greedy Search can be implemented using the A* search implementation,
# but we will set the cost of each node in the path to zero.
def greedy(graph, start, goal, heuristic):
    zero_cost_heuristic = {node: 0 for node in graph}
    return a_star(graph, start, goal, zero_cost_heuristic)


# For A* search and Greedy search, we need a heuristic function.
# Here's a simple heuristic function for the sample graph
heuristic = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 2,
    'E': 1,
    'F': 1,
    'G': 1,
    'H': 0,
    'I': 0
}

start, goal = 'A', 'I'
print("DFS:", dfs(graph, start, goal))
print("BFS:", bfs(graph, start, goal))
print("A*:", a_star(graph, start, goal, heuristic))
print("Greedy:", greedy(graph, start, goal, heuristic))

## These implementations improve upon the previous ones by using generator functions
#  for DFS and BFS, which allows for more efficient memory usage when multiple solutions are required, 
#  and by using a visited set for A* search to avoid revisiting nodes.
#  The complexities remain the same, but the implementations are more efficient in practice,
#  especially for large graphs.
## simple graph traversal problem where we need to find a path between two nodes in a given graph.
# Sample Graph
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

## Depth First Search (DFS)
# Time complexity: O(b^m), where b is the branching factor and m is the maximum depth of the search tree.
# Space complexity: O(bm), as we need to store the path in memory.
# Completeness: Not complete, as it might get stuck in an infinite loop if the goal is not in the explored path.
# Optimality: Not optimal, as it does not guarantee the shortest path.
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))


## Breadth First Search (BFS)
# Time complexity: O(b^d), where b is the branching factor and d is the depth of the solution.
# Space complexity: O(b^d), as it needs to store all the nodes at a given depth.
# Completeness: Complete, as it always finds a solution if one exists.
# Optimality: Optimal if the cost of moving between nodes is constant.
from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))


## A Search*
# Time complexity: O(b^d), where b is the branching factor and d is the depth of the solution. However, it can be much better if the heuristic is well-designed.
# Space complexity: O(b^d), as it needs to store all the nodes at a given depth. Again, it can be better if the heuristic is well-designed.
# Completeness: Complete, as long as the heuristic is admissible (never overestimates the cost to reach the goal) and consistent (satisfies the triangle inequality).
# Optimality: Optimal if the heuristic is admissible and consistent.
import heapq
from functools import total_ordering

@total_ordering
class PriorityNode:
    def __init__(self, priority, node, path):
        self.priority = priority
        self.node = node
        self.path = path

    def __lt__(self, other):
        return self.priority < other.priority

def a_star(graph, start, goal, heuristic):
    open_set = [PriorityNode(heuristic[start], start, [start])]

    while open_set:
        current = heapq.heappop(open_set)
        if current.node == goal:
            return current.path
        for neighbor in graph[current.node]:
            if neighbor not in current.path:
                heapq.heappush(open_set, PriorityNode(heuristic[neighbor], neighbor, current.path + [neighbor]))


## Greedy Search
# Time complexity: O(b^m), where b is the branching factor and m is the maximum depth of the search tree. It can be better if the heuristic is well-designed.
# Space complexity: O(bm), as we need to store the path in memory. Again, it can be better if the heuristic is well-designed.
# Completeness: Not complete, as it might get stuck in an infinite loop if the goal is not in the explored path. However, it can be complete under certain conditions with a well-designed heuristic.
# Optimality: Not optimal, as it does not guarantee the shortest path. It can be optimal if the heuristic is perfect (returns the exact cost to reach the goal).
def greedy(graph, start, goal, heuristic):
    return a_star(graph, start, goal, {node: 0 for node in graph})


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
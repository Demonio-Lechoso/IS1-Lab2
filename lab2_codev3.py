# Given an MxN grid with some cells blocked by obstacles,
# find the shortest path from the top-left corner to the bottom-right corner.
grid = [    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

#0: Free cell
#1: Blocked cell (obstacle)

# help functions
# We need some helper functions to get the neighbors of a cell, 
# calculate the heuristic distance (Manhattan distance in this case), 
# and reconstruct the path from the goal to the start.
def neighbors(grid, cell):
    row, col = cell
    candidates = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]

    result = []
    for r, c in candidates:
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 1:
            result.append((r, c))

    return result

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from, start, goal):
    path = [goal]
    current = goal
    while current != start:
        current = came_from[current][0]
        path.append(current)
    return path[::-1]

# DFS
def dfs(grid, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in neighbors(grid, node):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

# BFS
from collections import deque

def bfs(grid, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in neighbors(grid, node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None


# A*
import heapq

def a_star(grid, start, goal):
    open_set = [(manhattan_distance(start, goal), start, 0)]
    # came_from dict stores both the predecessor node and the tentative cost
    came_from = dict()

    while open_set:
        _, current, g = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in neighbors(grid, current):
            tentative_g = g + 1
            if neighbor not in came_from or tentative_g < came_from[neighbor][1]:
                heapq.heappush(open_set, (tentative_g + manhattan_distance(neighbor, goal), neighbor, tentative_g))
                came_from[neighbor] = (current, tentative_g)

    return None

# greedy search
def greedy(grid, start, goal):
    zero_cost_heuristic = {(i, j): 0 for i in range(len(grid)) for j in range(len(grid[0]))}
    return a_star(grid, start, goal)



start, goal = (0, 0), (4, 4)
print("DFS:", dfs(grid, start, goal))
print("BFS:", bfs(grid, start, goal))
print("A*:", a_star(grid, start, goal))
print("Greedy:", greedy(grid, start, goal))

## note that DFS and BFS are not guaranteed to find the shortest path in this problem,
# as they do not consider the heuristic distance to the goal.
# The A* search algorithm and Greedy search algorithm are more suitable
# for this type of problem, as they are guided by a heuristic function to efficiently explore the grid.
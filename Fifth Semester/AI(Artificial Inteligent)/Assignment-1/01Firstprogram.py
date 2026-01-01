#  i. Depth First Search (DFS) & Breadth First Search (BFS)
from collections import deque
graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': [],
 'E': ['F'],
 'F': []
}
def dfs(graph, start, visited=None):
 if visited is None:
 visited = set()
 print(start, end=" ")
 visited.add(start)
 for neighbor in graph[start]:
 if neighbor not in visited:
 dfs(graph, neighbor, visited)
def bfs(graph, start):
 visited = set()
 queue = deque([start])
 while queue:
 vertex = queue.popleft()
 if vertex not in visited:
 print(vertex, end=" ")
 visited.add(vertex)
 for neighbor in graph[vertex]:
 if neighbor not in visited:
 queue.append(neighbor)
print("DFS Traversal:")
dfs(graph, 'A')
print("\nBFS Traversal:")
bfs(graph, 'A')
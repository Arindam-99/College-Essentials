# ii. Depth-Limited Search (DLS) & Iterative Deepening Search (IDS)
def dls(graph, node, goal, limit):
 print(f"Visiting: {node}, Depth Limit: {limit}")
 if node == goal:
 return True
 if limit <= 0:
 return False
 for child in graph.get(node, []):
 if dls(graph, child, goal, limit - 1):
 return True
 return False
def dls_ids(graph, node, goal, limit):
 if node == goal:
 return True
 if limit == 0:
 return False
 for child in graph.get(node, []):
 if dls_ids(graph, child, goal, limit - 1):
 return True
 return False
def ids(graph, start, goal, max_depth):
 for depth in range(max_depth + 1):
 print(f"Searching at Depth Limit: {depth}")
 if dls_ids(graph, start, goal, depth):
 print("Goal Found at depth:", depth)
 return True
 return False
graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': [],
 'E': [],
 'F': []
}
print("Depth Limited Search Result:")
found = dls(graph, 'A', 'E', 2)
print("Goal Found:", found)
print("\nIterative Deepening Search Result:")
ids(graph, 'A', 'E', max_depth=5)

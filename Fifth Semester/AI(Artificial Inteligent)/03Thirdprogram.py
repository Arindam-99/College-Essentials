#iii. Uniform Cost Search (UCS)
import heapq
def uniform_cost_search(graph, start, goal):
 pq = [(0, start, [start])]
 visited = set()
 while pq:
 cost, node, path = heapq.heappop(pq)
 if node in visited:
 continue
 print(f"Visiting: {node} with cost: {cost}")
 visited.add(node)
 if node == goal:
 return cost, path
 for neighbor, weight in graph.get(node, []):
 if neighbor not in visited:
 heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
 return None, None
graph = {
 'A': [('B', 2), ('C', 5)],
 'B': [('D', 4), ('E', 1)],
 'C': [('F', 2)],
 'D': [],
 'E': [('F', 3)],
 'F': []
}
start = 'A'; goal = 'F'
print("\nUniform Cost Search Result:")
total_cost, best_path = uniform_cost_search(graph, start, goal)
print("\nShortest Path:", best_path)
print("Total Cost:", total_cost)

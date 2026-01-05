# ii. Dijkstra's Algorithm for Shortest Path
import heapq
def dijkstra(graph, start):
 pq = [(0, start)]
 distances = {node: float('inf') for node in graph}
 distances[start] = 0
 while pq:
 current_dist, node = heapq.heappop(pq)
 if current_dist > distances[node]: continue
 for neighbor, weight in graph[node]:
 distance = current_dist + weight
 if distance < distances[neighbor]:
 distances[neighbor] = distance
 heapq.heappush(pq, (distance, neighbor))
 return distances
graph = {
 'A': [('B', 4), ('C', 2)],
 'B': [('C', 5), ('D', 10)],
 'C': [('E', 3)],
 'D': [('F', 11)],
 'E': [('D', 4)],
 'F': []
}
result = dijkstra(graph, 'A')
print('Shortest distances from node A')
for node in sorted(result):
 print(f"A -> {node}: {result[node]}")
# iv. Travelling Salesman Problem (Greedy Approximation)
def tsp_greedy(distance_matrix, start=0):
 n = len(distance_matrix)
 visited = [False]*n; path=[start]; visited[start]=True
 total_cost = 0; current_city = start
 for _ in range(n-1):
 next_city=None; min_dist=float('inf')
 for city in range(n):
 if not visited[city] and distance_matrix[current_city][city] < min_dist:
 min_dist = distance_matrix[current_city][city]; next_city=city
 path.append(next_city); visited[next_city]=True; total_cost+=min_dist; current_city=next_city
 total_cost += distance_matrix[current_city][start]; path.append(start)
 return path, total_cost
distance_matrix = [
 [0,10,15,20],
 [10,0,35,25],
 [15,35,0,30],
 [20,25,30,0]
]
path, cost = tsp_greedy(distance_matrix, start=0)
print('Greedy TSP Path:', path); print('Total Cost:', cost)
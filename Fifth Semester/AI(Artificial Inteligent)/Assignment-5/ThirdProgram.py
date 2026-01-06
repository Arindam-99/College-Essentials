# iii. A* Search Algorithm on Grid
import heapq
def astar(grid, start, goal):
 rows, cols = len(grid), len(grid[0])
 moves = [(1,0),(-1,0),(0,1),(0,-1)]
 pq = [(0,0,start)]
 visited = set()
 g_score = {start:0}
 parent = {start: None}
 def heuristic(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])
 while pq:
 f, cost, node = heapq.heappop(pq)
 if node in visited: continue
 visited.add(node)
 if node == goal: break
 for move in moves:
 nr, nc = node[0]+move[0], node[1]+move[1]
 if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==0:
 new_cost = cost+1; neighbor=(nr,nc)
 if neighbor not in g_score or new_cost<g_score[neighbor]:
 g_score[neighbor]=new_cost
 f_score=new_cost+heuristic(neighbor, goal)
 parent[neighbor]=node
 heapq.heappush(pq,(f_score,new_cost,neighbor))
 path=[]
 node=goal
 while node:
 path.append(node); node=parent.get(node)
 return path[::-1]
grid=[
 [0,0,0,0,0],
 [0,1,1,1,0],
 [0,0,0,1,0],
 [0,1,0,0,0],
]
start=(0,0); goal=(3,4)
path = astar(grid, start, goal)
print('Shortest Path using A*:'); print(path)
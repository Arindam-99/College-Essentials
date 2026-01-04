# ii. Minimax with Alpha-Beta Pruning

import math
tree = [
 [3, 5, 2],
 [9, 1]
]
def alphabeta(node, depth, alpha, beta, isMax):
 if isinstance(node, int): return node
 if isMax:
 best = -math.inf
 for child in node:
 val = alphabeta(child, depth + 1, alpha, beta, False)
 best = max(best, val)
 alpha = max(alpha, best)
 if beta <= alpha: break
 return best
 else:
 best = math.inf
 for child in node:
 val = alphabeta(child, depth + 1, alpha, beta, True)
 best = min(best, val)
 beta = min(beta, best)
 if beta <= alpha: break
 return best
best_value = alphabeta(tree, 0, -math.inf, math.inf, True)
print("Best Value (with Alpha-Beta Pruning):", best_value)
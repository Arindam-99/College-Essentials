#i. Minimax Algorithm for Tic-Tac-Toe
import math
player, ai = 'O', 'X'
def print_board(board):
 for i in range(3):
 print(board[i][0], board[i][1], board[i][2])
 print()
def evaluate(board):
 win_states = [
 [board[0][0], board[0][1], board[0][2]],
 [board[1][0], board[1][1], board[1][2]],
 [board[2][0], board[2][1], board[2][2]],
 [board[0][0], board[1][0], board[2][0]],
 [board[0][1], board[1][1], board[2][1]],
 [board[0][2], board[1][2], board[2][2]],
 [board[0][0], board[1][1], board[2][2]],
 [board[2][0], board[1][1], board[0][2]],
 ]
 if [ai, ai, ai] in win_states: return 10
 if [player, player, player] in win_states: return -10
 return 0
def moves_left(board):
 for row in board:
 if '_' in row: return True
 return False
def minimax(board, depth, isMax):
 score = evaluate(board)
 if score == 10: return score - depth
 if score == -10: return score + depth
 if not moves_left(board): return 0
 if isMax:
 best = -math.inf
 for i in range(3):
 for j in range(3):
 if board[i][j] == '_':
 board[i][j] = ai
 best = max(best, minimax(board, depth + 1, False))
 board[i][j] = '_'
 return best
 else:
 best = math.inf
 for i in range(3):
 for j in range(3):
 if board[i][j] == '_':
 board[i][j] = player
 best = min(best, minimax(board, depth + 1, True))
 board[i][j] = '_'
 return best
def find_best_move(board):
 best_val = -math.inf
 best_move = (-1, -1)
 for i in range(3):
 for j in range(3):
 if board[i][j] == '_':
 board[i][j] = ai
 move_val = minimax(board, 0, False)
 board[i][j] = '_'
 if move_val > best_val:
 best_val = move_val; best_move = (i, j)
 return best_move
board = [
 ['X', 'O', 'X'],
 ['_', 'O', '_'],
 ['_', '_', '_']
]
print("Current Board:")
print_board(board)
best_move = find_best_move(board)
print("Best Move for AI (X):", best_move)

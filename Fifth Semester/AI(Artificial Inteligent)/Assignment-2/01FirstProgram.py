#Assignment 2 - i. Fuzzy Set Operations
A = {'x1': 0.2, 'x2': 0.7, 'x3': 0.4}
B = {'x1': 0.6, 'x2': 0.3, 'x3': 0.8}
def fuzzy_union(A, B):
 return {x: max(A[x], B[x]) for x in A}
def fuzzy_intersection(A, B):
 return {x: min(A[x], B[x]) for x in A}
def fuzzy_complement(A):
 return {x: 1 - A[x] for x in A}
def algebraic_sum(A, B):
 return {x: A[x] + B[x] - (A[x] * B[x]) for x in A}
def algebraic_product(A, B):
 return {x: A[x] * B[x] for x in A}
def cartesian_product(A, B):
 cart_prod = {}
 for x in A:
 for y in B:
 cart_prod[(x, y)] = min(A[x], B[y])
 return cart_prod
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("\nUnion:")
print(fuzzy_union(A, B))
print("\nIntersection:")
print(fuzzy_intersection(A, B))
print("\nComplement of A:")
print(fuzzy_complement(A))
print("\nAlgebraic Sum:")
print(algebraic_sum(A, B))
print("\nAlgebraic Product:")
print(algebraic_product(A, B))
print("\nCartesian Product A × B:")
for pair, val in cartesian_product(A, B).items():
 print(pair, ":", val)


'''Task 1 : Write a Python program to implement the Beam Search algorithm
to find the lowest-cost path from a start node to a goal node in a given
graph. The algorithm should keep only the top k best paths at each level
based on cumulative cost. Test the algorithm with different beam widths (k
= 1, 2, 3) and display the path and total cost found in each case.
S → A (2)
S → B (5)
S → C (4)
A → D (7)
A → E (3)
B → F (6)
C → G (2)
D → T (4)
E → T (6)
F → T (5)

G → T (3)
Task 2 Implement the Hill Climbing algorithm to maximize the function

f(x)=−x*2+10x+5 where 0 ≤ x ≤ 100

Start from a random value of x, check neighbors (x–1 and x+1), and move
to a better neighbor until no improvement is possible. Run it multiple times.'''

import heapq

# Graph definition (costs)
graph = {
    'S': [('A', 2), ('B', 5), ('C', 4)],
    'A': [('D', 7), ('E', 3)],
    'B': [('F', 6)],
    'C': [('G', 2)],
    'D': [('T', 4)],
    'E': [('T', 6)],
    'F': [('T', 5)],
    'G': [('T', 3)],
    'T': []
}

# Beam Search Function
def beam_search(start, goal, k):
    beam = [(0, [start])]  # (cost, path)

    while beam:
        candidates = []

        for cost, path in beam:
            node = path[-1]

            if node == goal:
                return path, cost

            for neighbor, edge_cost in graph.get(node, []):
                new_path = path + [neighbor]
                new_cost = cost + edge_cost
                candidates.append((new_cost, new_path))

        # Keep top k lowest-cost paths
        beam = heapq.nsmallest(k, candidates, key=lambda x: x[0])

    return None, float('inf')


# Run for k = 1, 2, 3
for k in [1, 2, 3]:
    path, cost = beam_search('S', 'T', k)
    print(f"\nBeam Width = {k}")
    print("Path:", path)
    print("Cost:", cost)

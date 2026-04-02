
def hill_climbing(graph, start, goal, h):
    current = start
    path = [start]

    while current != goal:
        neighbors = graph[current]

        # if no neighbors, stop
        if not neighbors:
            return None

        best = current
        best_h = h[current]

        # find neighbor with smallest heuristic
        for child in neighbors:
            if h[child] < best_h:
                best = child
                best_h = h[child]

        # if no better node found, stuck at local optimum
        if best == current:
            return path

        current = best
        path.append(current)

    return path

def beam_search(graph, start, goal, h, width):
    beam = [(start, [start])]   # current level nodes

    while beam:
        new_beam = []

        for node, path in beam:
            if node == goal:
                return path

            # add children
            for child in graph[node]:
                new_beam.append((child, path + [child]))

        # sort by heuristic
        new_beam.sort(key=lambda x: h[x[0]])

        # keep only best k nodes
        beam = new_beam[:width]

    return None

import random

def fitness(x):
    return x * x   # maximize x²


def genetic_algorithm():
    population = [1, 2, 3, 4]   # initial population

    for _ in range(5):   # run 5 generations
        # sort by fitness
        population.sort(key=fitness, reverse=True)

        # select best 2
        parent1 = population[0]
        parent2 = population[1]

        # crossover
        child = (parent1 + parent2) // 2

        # mutation
        child += random.randint(-1, 1)

        # replace worst
        population[-1] = child

    return max(population, key=fitness)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 1,
    'F': 3,
    'G': 0
}

print(hill_climbing(graph, 'A', 'G', h))
print(beam_search(graph, 'A', 'G', h, 2))
print(genetic_algorithm())


'''Task 3: Implement a Genetic Algorithm to minimize assignment cost
for 10 tasks and 5 machines using this 10×5 cost matrix:
cost_matrix = [
[4, 6, 8, 7, 5],
[7, 5, 6, 8, 4],
[6, 4, 7, 5, 8],
[5, 8, 6, 4, 7],
[8, 6, 5, 7, 4],
[7, 4, 8, 6, 5],
[6, 7, 4, 5, 8],
[5, 6, 7, 8, 4],
[4, 7, 5, 6, 8],
[8, 5, 6, 4, 7]
]
Each chromosome is a list of length 10, where each index represents
a task and the value is the assigned machine. Include random
population initialization, fitness = 1/total cost, top-50% selection,
crossover, mutation, and 100 generations. Print the best
chromosome, total cost, fitness, and generation. Run with population
sizes 10 and 30 and compare results.'''

import random

cost_matrix = [
    [4,6,8,7,5],
    [7,5,6,8,4],
    [6,4,7,5,8],
    [5,8,6,4,7],
    [8,6,5,7,4],
    [7,4,8,6,5],
    [6,7,4,5,8],
    [5,6,7,8,4],
    [4,7,5,6,8],
    [8,5,6,4,7]
]

# -------------------------
# random chromosome
# -------------------------
def create():
    return [random.randint(0, 4) for _ in range(10)]


# -------------------------
# total cost
# -------------------------
def cost(chrom):
    total = 0
    for i in range(10):
        total += cost_matrix[i][chrom[i]]
    return total


# -------------------------
# genetic algorithm
# -------------------------
def ga(pop_size):
    population = [create() for _ in range(pop_size)]

    for gen in range(100):
        population.sort(key=cost)

        parents = population[:pop_size//2]   # top 50%
        new_pop = []

        while len(new_pop) < pop_size:
            p1, p2 = random.sample(parents, 2)

            # crossover
            point = random.randint(1, 8)
            child = p1[:point] + p2[point:]

            # mutation
            if random.random() < 0.1:
                idx = random.randint(0, 9)
                child[idx] = random.randint(0, 4)

            new_pop.append(child)

        population = new_pop

    best = min(population, key=cost)

    print("\nPopulation =", pop_size)
    print("Best chromosome:", best)
    print("Total cost:", cost(best))
    print("Fitness:", 1/cost(best))


ga(10)
ga(30)



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

NUM_TASKS = 10
NUM_MACHINES = 5

# Create random chromosome
def create_individual():
    return [random.randint(0, 4) for _ in range(NUM_TASKS)]

# Fitness = 1 / cost
def fitness(individual):
    total_cost = 0
    for task in range(NUM_TASKS):
        machine = individual[task]
        total_cost += cost_matrix[task][machine]
    return 1 / total_cost, total_cost


# Selection (top 50%)
def select(population):
    population.sort(key=lambda x: fitness(x)[0], reverse=True)
    return population[:len(population)//2]


# Crossover
def crossover(p1, p2):
    point = random.randint(1, NUM_TASKS - 2)
    return p1[:point] + p2[point:]


# Mutation
def mutate(individual):
    idx = random.randint(0, NUM_TASKS - 1)
    individual[idx] = random.randint(0, 4)
    return individual


# Genetic Algorithm
def run_ga(pop_size):
    population = [create_individual() for _ in range(pop_size)]

    for generation in range(100):
        population = sorted(population, key=lambda x: fitness(x)[0], reverse=True)

        best_fit, best_cost = fitness(population[0])

        # Selection
        parents = select(population)

        # New population
        new_population = []

        while len(new_population) < pop_size:
            p1, p2 = random.sample(parents, 2)
            child = crossover(p1, p2)

            if random.random() < 0.1:
                child = mutate(child)

            new_population.append(child)

        population = new_population

    # Final best
    best = max(population, key=lambda x: fitness(x)[0])
    best_fit, best_cost = fitness(best)

    print(f"\nPopulation Size = {pop_size}")
    print("Best Chromosome:", best)
    print("Total Cost:", best_cost)
    print("Fitness:", best_fit)


# Run for both sizes
run_ga(10)
run_ga(30)
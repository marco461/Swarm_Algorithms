import time
import numpy as np
from copy import deepcopy
from PSO import PSO
from TLBO import TLBO
from ACO import ACO
from ABC import *
from GWO import *

# Define the parameters
lb = -10
ub = 10
num_particles = 5  # Number of particles (rows)
num_dimensions = 4  # Number of dimensions (columns)
iterations = 50
w = 0.5
c1 = 1.5
c2 = 1.5

# Generate the matrix
population = np.random.uniform(lb, ub, (num_particles, num_dimensions))


def fitness_function(x):
    return np.sum(np.square(x))


# Function to run and time each algorithm
def run_algorithm(algorithm_func, algo_name, *args):
    start_time = time.time()
    best_solution, best_fitness = algorithm_func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return {
        "Algorithm": algo_name,
        "Best Solution": best_solution,
        "Best Fitness": best_fitness,
        "Time (s)": elapsed_time
    }

# Run and time each algorithm
results = []

# Create a deep copy of the population for each algorithm to ensure it remains unchanged
results.append(run_algorithm(PSO, "PSO", fitness_function, deepcopy(population), iterations, lb, ub, w, c1, c2))
results.append(run_algorithm(TLBO, "TLBO", fitness_function, deepcopy(population), iterations, lb, ub))

abc_min = ABC_Min(fitness_function, deepcopy(population), iterations, lb, ub)
results.append(run_algorithm(abc_min.run, "ABC_Min"))

abc_max = ABC_Max(fitness_function, deepcopy(population), iterations, lb, ub)
results.append(run_algorithm(abc_max.run, "ABC_Max"))

results.append(run_algorithm(GWO_Min, "GWO_Min", deepcopy(population), fitness_function, iterations, lb, ub))
results.append(run_algorithm(GWO_Max, "GWO_Max", deepcopy(population), fitness_function, iterations, lb, ub))

# Separate results into minimum-based and maximum-based algorithms
min_algos = ["PSO", "TLBO","ABC_Min", "GWO_Min"]
max_algos = ["ABC_Max", "GWO_Max"]

min_results = [result for result in results if result['Algorithm'] in min_algos]
max_results = [result for result in results if result['Algorithm'] in max_algos]

# Display the results
print("============= Minimum-Based Algorithms =============")
for result in results:
    if result['Algorithm'] in min_algos:
        print(f"Algorithm: {result['Algorithm']}")
        print(f"Best Solution: {result['Best Solution']}")
        print(f"Best Fitness: {result['Best Fitness']}")
        print(f"Time (s): {result['Time (s)']}\n")
        

print("============= Maximum-Based Algorithms =============")
for result in results:
    if result['Algorithm'] in max_algos:
        print(f"Algorithm: {result['Algorithm']}")
        print(f"Best Solution: {result['Best Solution']}")
        print(f"Best Fitness: {result['Best Fitness']}")
        print(f"Time (s): {result['Time (s)']}\n")

# Find the best algorithm in terms of time and fitness for minimum-based algorithms
best_min_time_result = min(min_results, key=lambda x: x['Time (s)'])
best_min_fitness_result = min(min_results, key=lambda x: x['Best Fitness'])

print("---------------------------------------------------------------------------------")

print(f"Best Minimum-Based Algorithm (Time): {best_min_time_result['Algorithm']}, Time: {best_min_time_result['Time (s)']}s")
print(f"Best Minimum-Based Algorithm (Fitness): {best_min_fitness_result['Algorithm']}, Fitness: {best_min_fitness_result['Best Fitness']}")

print("---------------------------------------------------------------------------------")

# Find the best algorithm in terms of time and fitness for maximum-based algorithms
best_max_time_result = min(max_results, key=lambda x: x['Time (s)'])
best_max_fitness_result = min(max_results, key=lambda x: x['Best Fitness'])

print(f"Best Maximum-Based Algorithm (Time): {best_max_time_result['Algorithm']}, Time: {best_max_time_result['Time (s)']}s")
print(f"Best Maximum-Based Algorithm (Fitness): {best_max_fitness_result['Algorithm']}, Fitness: {best_max_fitness_result['Best Fitness']}")

print("---------------------------------------------------------------------------------")

# Find the overall minimum time and fitness and the corresponding algorithm
min_time_result = min(results, key=lambda x: x['Time (s)'])
min_fitness_result = min(results, key=lambda x: x['Best Fitness'])

print(f"Overall Minimum Time: {min_time_result['Time (s)']}s, Algorithm: {min_time_result['Algorithm']}")
print(f"Overall Minimum Fitness: {min_fitness_result['Best Fitness']}, Algorithm: {min_fitness_result['Algorithm']}")

print("---------------------------------------------------------------------------------")


import time
import numpy as np
from PSO import PSO
from TLBO import TLBO
from ACO import ACO
from ABC import *
from GWO import *

# Define the parameters
lb = -100
ub = 100
num_particles = 5  # Number of particles (rows)
num_dimensions = 4  # Number of dimensions (columns)
iterations = 2
w = 0.5
c1 = 1.5
c2 = 1.5

# Generate the matrix
population = np.random.uniform(lb, ub, (num_particles, num_dimensions))

def fitness_function(x):
    return np.sum(x)

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

# Note: Passing the class instance and calling the run method separately
abc_min = ABC_Min(fitness_function, population, iterations, lb, ub)
abc_max = ABC_Max(fitness_function, population, iterations, lb, ub)

results.append(run_algorithm(PSO, "PSO", fitness_function, population, iterations, lb, ub, w, c1, c2))
results.append(run_algorithm(TLBO, "TLBO", fitness_function, population, iterations, lb, ub))
results.append(run_algorithm(abc_min.run, "ABC_Min"))
results.append(run_algorithm(abc_max.run, "ABC_Max"))
results.append(run_algorithm(GWO_Min, "GWO_Min", population, fitness_function, iterations, lb, ub))
results.append(run_algorithm(GWO_Max, "GWO_Max", population, fitness_function, iterations, lb, ub))

# Display the results
for result in results:
    print(f"Algorithm: {result['Algorithm']}")
    print(f"Best Solution: {result['Best Solution']}")
    print(f"Best Fitness: {result['Best Fitness']}")
    print(f"Time (s): {result['Time (s)']}\n")

# Find the minimum time and the corresponding algorithm
min_time_result = min(results, key=lambda x: x['Time (s)'])
print(f"Minimum Time: {min_time_result['Time (s)']}s, Algorithm: {min_time_result['Algorithm']}")

# Find the minimum fitness and the corresponding algorithm
min_fitness_result = min(results, key=lambda x: x['Best Fitness'])
print(f"Minimum Fitness: {min_fitness_result['Best Fitness']}, Algorithm: {min_fitness_result['Algorithm']}")


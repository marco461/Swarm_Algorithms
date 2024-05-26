import time
import numpy as np
from PSO import PSO
from TLBO import TLBO
from ACO import ACO
from ABC import *

class Swarm_Algorithms():
    def __init__(self, fitness_function, population, iterations, lb, ub, c1, c2, w, ant_n=5):
        self.fitness_function = fitness_function
        self.population = population
        self.iterations = iterations
        self.lb = lb
        self.ub = ub
        self.c1 = c1
        self.c2 = c2
        self.w = w
        self.ant_n = ant_n

    def PSO(self):
        return PSO(self.fitness_function, self.population, self.iterations, self.lb, self.ub, self.w, self.c1, self.c2)
    
    def TLBO(self):
        return TLBO(self.fitness_function, self.population, self.iterations, self.lb, self.ub)

    def ACO(self): 
        aco = ACO(self.fitness_function, self.population, self.ant_n, self.iterations, self.lb, self.ub)
        best_solution, best_fitness = aco.run()
        return best_solution, best_fitness
    
    def ABC(self):
        abc_min = ABC_Min(self.fitness_function, self.population, self.iterations, self.lb, self.ub)
        abc_max = ABC_Max(self.fitness_function, self.population, self.iterations, self.lb, self.ub)
        best_solution_min, best_fitness_min = abc_min.run()
        best_solution_max, best_fitness_max = abc_max.run()
        return (best_solution_min, best_fitness_min), (best_solution_max, best_fitness_max)


# Example usage -----------------------------------------------------------------------
# Define the parameters
lower_bound = -10
upper_bound = 10
num_particles = 5  # Number of particles (rows)
num_dimensions = 3  # Number of dimensions (columns)
iterations = 10
w = 0.5
c1 = 1.5
c2 = 1.5

# Generate the matrix
population = np.random.uniform(lower_bound, upper_bound, (num_particles, num_dimensions))

def fitness_function(x):
    return np.sum(x**2)

swarm = Swarm_Algorithms(fitness_function, population, iterations, lower_bound, upper_bound, c1, c2, w)

# Function to run and time each algorithm
def run_algorithm(algorithm_func, algo_name):
    start_time = time.time()
    best_solution, best_fitness = algorithm_func()
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

results.append(run_algorithm(swarm.PSO, "PSO"))
results.append(run_algorithm(swarm.TLBO, "TLBO"))

abc_results_min = run_algorithm(lambda: swarm.ABC()[0], "ABC_Min")
results.append(abc_results_min)

abc_results_max = run_algorithm(lambda: swarm.ABC()[1], "ABC_Max")
results.append(abc_results_max)

# Display the results
for result in results:
    print(f"Algorithm: {result['Algorithm']}")
    print(f"Best Solution: {result['Best Solution']}")
    print(f"Best Fitness: {result['Best Fitness']}")
    print(f"Time (s): {result['Time (s)']}\n")

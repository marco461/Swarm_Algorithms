# Swarm Algorithms Library

This repository contains the implementation of several swarm intelligence algorithms for optimization. The implemented algorithms include Particle Swarm Optimization (PSO), Teaching-Learning-Based Optimization (TLBO), Ant Colony Optimization (ACO), and Artificial Bee Colony (ABC).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Algorithms](#algorithms)
  - [Particle Swarm Optimization (PSO)](#particle-swarm-optimization-pso)
  - [Teaching-Learning-Based Optimization (TLBO)](#teaching-learning-based-optimization-tlbo)
  - [Ant Colony Optimization (ACO)](#ant-colony-optimization-aco)
  - [Artificial Bee Colony (ABC)](#artificial-bee-colony-abc)
- [Example](#example)
- [License](#license)

## Installation

To use this library, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/swarm-algorithms.git
cd swarm-algorithms
pip install -r requirements.txt
```

## Usage

First, import the necessary modules and define your fitness function. Then, create an instance of the `Swarm_Algorithms` class with the required parameters and call the desired algorithm.

```python
import time
import numpy as np
from PSO import PSO
from TLBO import TLBO
from ACO import ACO
from ABC import *

class Swarm_Algorithms:
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
```

## Algorithms

### Particle Swarm Optimization (PSO)

PSO is a computational method that optimizes a problem by iteratively improving a candidate solution with regard to a given measure of quality. It solves a problem by having a population of candidate solutions, here dubbed particles, and moving these particles around in the search-space according to simple mathematical formulae over the particle's position and velocity.

### Teaching-Learning-Based Optimization (TLBO)

TLBO is a population-based method inspired by the teaching-learning process in a classroom. The algorithm simulates the influence of a teacher on learners' output in a class and the interaction among learners.

### Ant Colony Optimization (ACO)

ACO is a probabilistic technique for solving computational problems which can be reduced to finding good paths through graphs. It is inspired by the behavior of ants in finding paths from the colony to food.

### Artificial Bee Colony (ABC)

ABC is an optimization algorithm based on the intelligent foraging behavior of honey bee swarm. It is inspired by the foraging behavior of honey bees.

## Example

Below is an example usage of the `Swarm_Algorithms` class to run and time each algorithm.

```python
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
```
## Example Output

## License
![Screenshot 2024-05-28 114438](https://github.com/marco461/Swarm_Algorithms/assets/121636645/4a5b2f88-508e-4066-861e-0375325f7cc4)
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

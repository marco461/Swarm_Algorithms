# Swarm Algorithms Comparison

This repository contains a Python script that implements and compares various swarm intelligence algorithms for optimization. The algorithms included are Particle Swarm Optimization (PSO), Teaching-Learning-Based Optimization (TLBO), Ant Colony Optimization algorithm (ACO), Artificial Bee Colony (ABC) for both minimization and maximization, and Grey Wolf Optimizer (GWO) for both minimization and maximization. The script evaluates these algorithms based on their ability to find the optimal solution and the time taken for the optimization process.

## Repository Contents

- **`PSO.py`**: Contains the implementation of the Particle Swarm Optimization algorithm.
- **`TLBO.py`**: Contains the implementation of the Teaching-Learning-Based Optimization algorithm.
- **`ACO.py`**: Contains the implementation of the Ant Colony Optimization algorithm.
- **`ABC.py`**: Contains the implementation of the Artificial Bee Colony algorithm, including both minimization and maximization variants.
- **`GWO.py`**: Contains the implementation of the Grey Wolf Optimizer algorithm, including both minimization and maximization variants.
- **`Swarm_Algorithms.py`**: The main script that runs and times each algorithm, compares their performance, and prints the results.

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/swarm-algorithms-comparison.git
   cd swarm-algorithms-comparison
   ```

2. **Install required dependencies**:
   Ensure you have the necessary Python libraries installed. You can use `pip` to install any missing libraries.

3. **Run the main script**:
   ```bash
   python Swarm_Algorithms.py
   ```
   This will execute the comparison and print the results to the console.

## Algorithms Included

1. **Particle Swarm Optimization (PSO)**
2. **Teaching-Learning-Based Optimization (TLBO)**
3. **Artificial Bee Colony (ABC)**
   - Minimization (`ABC_Min`)
   - Maximization (`ABC_Max`)
4. **Grey Wolf Optimizer (GWO)**
   - Minimization (`GWO_Min`)
   - Maximization (`GWO_Max`)

## Parameters

- **Lower Bound (`lb`)**: -10
- **Upper Bound (`ub`)**: 10
- **Number of Particles**: 5
- **Number of Dimensions**: 4
- **Iterations**: 50
- **PSO Parameters**: `w` (inertia weight), `c1` (cognitive coefficient), `c2` (social coefficient)

## Fitness Function

The fitness function used in the script is the sum of squares of the input vector:

```python
def fitness_function(x):
    return np.sum(np.square(x))
```

## Results

The script runs each algorithm with the same initial population and prints the best solution, best fitness, and execution time for each algorithm. It also identifies the best-performing algorithms in terms of time and fitness.

## Example Output

```plaintext
============= Minimum-Based Algorithms =============
Algorithm: PSO
Best Solution: [ 0.00038826  0.00013539 -0.0003896  -0.0003565 ]
Best Fitness: 4.479469777117293e-07
Time (s): 0.0049936771392822266

Algorithm: TLBO
Best Solution: [ 2.21576034e-09 -3.26967128e-09 -1.10184297e-08 -1.20762278e-08]
Best Fitness: 2.828414153322774e-16
Time (s): 0.008859395980834961

Algorithm: ABC_Min
Best Solution: [-5.6192385  -2.16361609 -1.90861489 -5.16317425]
Best Fitness: 0.014802040076999156
Time (s): 0.004006624221801758

Algorithm: GWO_Min
Best Solution: [-1.09888329 -4.94674773 -3.53200937  4.76503822]
Best Fitness: 60.85853706337849
Time (s): 0.009610652923583984

============= Maximum-Based Algorithms =============
Algorithm: ABC_Max
Best Solution: [ -2.62159106 -10.           6.91890891  -4.27649209]
Best Fitness: 0.004732535384112649
Time (s): 0.0045833587646484375

Algorithm: GWO_Max
Best Solution: [-10. -10. -10. -10.]
Best Fitness: 400.0
Time (s): 0.010488748550415039

---------------------------------------------------------------------------------
Best Minimum-Based Algorithm (Time): ABC_Min, Time: 0.004006624221801758s
Best Minimum-Based Algorithm (Fitness): TLBO, Fitness: 2.828414153322774e-16
---------------------------------------------------------------------------------
Best Maximum-Based Algorithm (Time): ABC_Max, Time: 0.0045833587646484375s
Best Maximum-Based Algorithm (Fitness): ABC_Max, Fitness: 0.004732535384112649
---------------------------------------------------------------------------------
Overall Minimum Time: 0.004006624221801758s, Algorithm: ABC_Min
Overall Minimum Fitness: 2.828414153322774e-16, Algorithm: TLBO
---------------------------------------------------------------------------------
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss your changes or suggestions.

## Acknowledgements

This project was developed to provide a comparative study of different swarm intelligence algorithms and their performance on a given optimization problem.

---

Feel free to reach out if you have any questions or need further assistance. Happy coding!

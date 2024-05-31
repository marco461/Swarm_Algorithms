import numpy as np
def GWO_Min(populations,fitness_function,iterations, lower_bound ,upper_bound):
    # print(populations)
    population = populations
    population_size = len(population)
    num_variables = len(population[0])

    for i in range(iterations):
        fitness_value = np.apply_along_axis(fitness_function, 1, population)
        # Sort the population based on the fitness function to find Xbest
        sorted_population = sorted(population, key=lambda x: fitness_function(x))
        
        # Find the best solution
        X = []
        a = 2*(1-(i/iterations))
        for j in range(population_size):# wolf loop    

            for k in range(3): # Xs loop

                r = np.random.uniform(0, 1)  # Random value for r between 0 and 1
                A = (2 * a * r) - a
                C = 2 * r
                temp = (C * sorted_population[k]) - population[j]
                D = abs(temp)
                
                temp = sorted_population[k] - (A * D)
                X.append(temp) # X1, X2, X3
            
            new_pos = []
            for k in range(num_variables):  # new position loop
                temp = sum(sublist[k] for sublist in X)
                new_pos.append(temp)
            
            # Check bound  
            new_pos = np.clip(new_pos, lower_bound, upper_bound)

            # Check Who are the minimum
            if fitness_function(new_pos) < fitness_function(population[j]): 
                population[j] = new_pos
                fitness_value[j] = fitness_function(new_pos)
        
    return population[np.argmin(fitness_value)] , min(fitness_value)

def GWO_Max(populations, fitness_function, iterations, lower_bound, upper_bound):
    # print(populations)
    population = populations
    population_size = len(population)
    num_variables = len(population[0])
 
    for i in range(iterations):
        fitness_value = np.apply_along_axis(fitness_function, 1, population)

        # Sort the population based on the fitness function
        sorted_population = sorted(population, key=lambda x: fitness_function(x), reverse=True)

        X = []
        a = 2 * (1 - (i / iterations))
        for j in range(population_size):  # wolf loop

            for k in range(3):  # Xs loop

                r = np.random.uniform(0, 1)  # Random value for r between 0 and 1
                A = (2 * a * r) - a
                C = 2 * r
                temp = (C * sorted_population[k]) - population[j]
                D = abs(temp)

                temp = sorted_population[k] - (A * D)
                X.append(temp)

            new_pos = []
            for k in range(num_variables):  # new position loop
                temp = sum(sublist[k] for sublist in X)
                new_pos.append(temp)

            # Check bound
            new_pos = np.clip(new_pos, lower_bound, upper_bound)

            # Check who has the maximum fitness
            if fitness_function(new_pos) > fitness_function(population[j]):
                population[j] = new_pos
                fitness_value[j] = fitness_function(new_pos)
            
    return population[np.argmax(fitness_value)], max(fitness_value)


# Example usage -----------------------------------------------------------------------
# def fitness_function(x):
#     # Example fitness function: sum of squares
#     return np.sum(x)


# # Define bounds
# lower_bound = -60
# upper_bound = 60

# # Define initial population
# population = np.random.uniform(lower_bound, upper_bound, size=(5, 3))  # Example: 10 individuals, 2 variables

# # Call GWO_Min
# result_position, result_fitness = GWO_Min(population, fitness_function, iterations=1, lower_bound=lower_bound, upper_bound=upper_bound)

# # Print the result
# print("Optimal Position:", result_position)
# print("Optimal Fitness:", result_fitness)
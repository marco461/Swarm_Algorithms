import numpy as np

''' 
TLBO (Teaching-Learning-Based Optimization) algorithm is designed to minimize the fitness function.
'''
def TLBO(fitness_function, populations, iterations , lower_bound ,upper_bound):
    population = populations
    population_size = len(population)
    # num_variables = len(population[0])

    for i in range(iterations):
        # print("Iteration:", i+1)
        # print("Population and Fitness Values:")
        # for j in range(population_size):
        #     print(population[j], "Fitness:", fitness_function(population[j]))
        
        # Find XBest
        sorted_population = sorted(population, key=lambda x: fitness_function(x))
        teacher = sorted_population[0]
        # print("Teacher:", teacher, "Fitness:", fitness_function(teacher))
        
        # Calculate mean of population
        Xmean = np.mean(population, axis=0)
        # print("Xmean:", Xmean)
        
        # Teaching phase
        for j in range(population_size):
            # Xnew = Xold + r (Xbest - Tf * Xmean)
            r = np.random.uniform(0, 1)  # Random value for r between 0 and 1
            Tf = np.random.uniform(1, 2)  # Random value for Tf between 1 and 2
            # Update the population (Xnew)
            new_individual = population[j] + r * (teacher - Tf * Xmean)
            # Ensure the new individual stays within bounds
            new_individual = np.clip(new_individual, lower_bound, upper_bound)

            new_fitness = fitness_function(new_individual)
            if new_fitness < fitness_function(population[j]):
                population[j] = new_individual          
        
        # Learning phase
            rand_partner_index = np.random.randint(0, population_size)
            if rand_partner_index != j:
                random_partner = population[rand_partner_index]
                # Xnew = X + r(X − Xp)
                r = np.random.uniform(0, 1) # Random value for r between 0 and 1
                new_individual = population[j] + r * (random_partner - population[j])
                
                # Ensure the new individual stays within bounds
                new_individual = np.clip(new_individual, lower_bound, upper_bound)
                new_fitness = fitness_function(new_individual)
                if new_fitness < fitness_function(population[j]):
                    population[j] = new_individual
        
        # print("Population after Teaching Phase:")
        # for j in range(population_size):
        #     print(population[j])
        
        # print("Learning Phase Random Partner:", random_partner)
        # print("Population after Learning Phase:")
        # for j in range(population_size):
        #     print(population[j])
        # print("\n")
    
    # Find best solution after all iterations
    best_solution = sorted(population, key=lambda x: fitness_function(x))[0]
    best_fitness = fitness_function(best_solution)
    # print("Best Fitness:", best_fitness)
    # print("Best Solution:", best_solution)
    return best_solution ,best_fitness

# Example usage -----------------------------------------------------------------------
# num_dimensions = 3
# num_particles = 5
# max_iter = 20
# lower_bound = -10
# upper_bound = 10

# def fitness_function(x):
#     return np.sum(x**2) 
# population = np.random.uniform(lower_bound, upper_bound, (num_particles, num_dimensions))
# print(population)
# import time
# start_time_pso = time.time()
# best_solution_tlbo, best_fitness_tlbo = TLBO(fitness_function, population, max_iter, lower_bound, upper_bound)
# end_time_pso = time.time()

# print(best_solution_tlbo, best_fitness_tlbo)


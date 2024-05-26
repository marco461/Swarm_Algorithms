import numpy as np
'''
The Artificial Bee Colony (ABC) algorithm is a nature-inspired optimization algorithm that mimics
the foraging behavior of honey bees. 
The algorithm, proposed by Dervis Karaboga in 2005,
divides the bee colony into three groups:
    -   employed bees
    -   onlooker bees 
    -   scout bees.
Each group has a specific role in the optimization process.
'''
class ABC_Max:
    def __init__(self, fitness_function, population, iteration, lower_bound, upper_bound):
        self.food_source = population
        self.fitness_function_eq = fitness_function
        self.fitness_function_val = np.apply_along_axis(fitness_function, 1, self.food_source)
        self.fitness = [1 / (1 + val) if val >= 0 else 1 + abs(val) for val in self.fitness_function_val]
        self.trial = [0 for _ in range(len(self.food_source))]
        self.iteration = iteration
        self.max_trials = 4
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.best_solution = None
        self.best_fitness = None
        self.prob = []
    
    def run(self):
        for i in range(self.iteration):
            self.Employed_Bee_Phase()
            self.Onlooker_Bee_Phase()
            self.Scout_Bee_Phase()
            # print("Best Solution - iteration:",i+1,":", self.best_solution)
            # print("Best Fitness  - iteration:",i+1,":", self.best_fitness)
            # print("---------------------------------------------------------------------------------------------")
        # print("Best Solution (Maximization):", self.best_golobal_solution[np.argmin(self.best_golobal_fitness)])
        # print("Best Fitness (Maximization):", np.min(self.best_golobal_fitness))
        # return self.food_source[np.argmin(self.best_fitness)], np.min(self.best_fitness)
        return self.best_solution , self.best_fitness

    def Employed_Bee_Phase(self):

        '''The number of Employed Bee must be equal to the food sources.'''           
        
        for i in range(len(self.food_source)): # Bees loop
            ''' Xold = Xnew if fit(Xnew) > fit(Xold)'''
            alpha = np.random.uniform(-1, 1)
            p = np.random.randint(0, len(self.food_source))
            j = np.random.randint(0, len(self.food_source[0]))
            Xp = self.food_source[p][j]
            old = self.food_source[i][j]
            new = old + (alpha * (old - Xp))
            temp = self.food_source[i]
            temp[j] = new 
            new_fitness_value = self.fitness_function_eq(temp)
            new_fitness = 1 / (1 + new_fitness_value) if new_fitness_value >= 0 else 1 + abs(new_fitness_value)

            if new_fitness < self.fitness[i]:   # maximum
                self.food_source[i][j] = new
                self.food_source[i] = np.clip(self.food_source[i], self.lower_bound, self.upper_bound)
                self.fitness[i] = new_fitness
                self.trial[i] = 0
            else:
                self.trial[i] += 1
            
    def Onlooker_Bee_Phase(self):
        for i in range(len(self.food_source)): 
            self.prob.append((0.9 * (self.fitness[i]/max(self.fitness))) + 0.1)
        
        i = 0
        bee = 0
        r = np.random.uniform(self.lower_bound, self.upper_bound)  
        while bee == (len(self.food_source)-1): 
            if r < self.prob[i]:
                r = np.random.uniform(self.lower_bound, self.upper_bound)
                alpha = np.random.uniform(-1, 1)
                p = np.random.randint(0, len(self.food_source))
                j = np.random.randint(0, len(self.food_source[0]))
                Xp = self.food_source[p][j]
                old = self.food_source[i][j]
                new = old + (alpha * (old - Xp))
                temp = self.food_source[i]
                temp[j] = new
                new_fitness_value = self.fitness_function_eq(temp)
                new_fitness = 1 / (1 + new_fitness_value) if new_fitness_value >= 0 else 1 + abs(new_fitness_value)

                if new_fitness < self.fitness[i]:
                    self.food_source[i][j] = new
                    self.food_source[i] = np.clip(self.food_source[i], self.lower_bound, self.upper_bound)
                    self.fitness[i] = new_fitness
                    self.trial[i] = 0
                else:
                    self.trial[i] += 1
                bee += 1
                
            i += 1
            if i == (len(self.prob)-1):
                i = 0
            
        self.prob = []

    def Scout_Bee_Phase(self):
        for i in range(len(self.trial)):
            if self.trial[i] >= self.max_trials:
                self.trial[i] = 0
                self.food_source[i] = np.random.uniform(self.lower_bound, self.upper_bound, len(self.food_source[i]))
                fitness_value = self.fitness_function_eq(self.food_source[i])
                self.fitness[i] = 1 / (1 + fitness_value) if fitness_value >= 0 else 1 + abs(fitness_value)
        self.best_solution = self.food_source[np.argmin(self.fitness)]
        self.best_fitness = np.min(self.fitness)

class ABC_Min:
    def __init__(self, fitness_function, population, iteration, lower_bound, upper_bound):
        self.food_source = population
        self.fitness_function_eq = fitness_function
        self.fitness_function_val = np.apply_along_axis(fitness_function, 1, self.food_source)
        self.fitness = [1 / (1 + val) if val >= 0 else 1 + abs(val) for val in self.fitness_function_val]
        self.trial = [0 for _ in range(len(self.food_source))]
        self.iteration = iteration
        self.max_trials = 4
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.best_solution = None
        self.best_fitness = None
        self.prob = []
    
    def run(self):
        for i in range(self.iteration):
            self.Employed_Bee_Phase()
            self.Onlooker_Bee_Phase()
            self.Scout_Bee_Phase()
            # print("Best Solution - iteration:",i+1,":", self.best_solution)
            # print("Best Fitness  - iteration:",i+1,":", self.best_fitness)
            # print("---------------------------------------------------------------------------------------------")
        # print("Best Solution (Minimization):", self.best_golobal_solution[np.argmax(self.best_golobal_fitness)])
        # print("Best Fitness (Minimization):", np.max(self.best_golobal_fitness))
        # return self.food_source[np.argmax(self.best_fitness)] , np.max(self.best_fitness)
        return self.best_solution , self.best_fitness

    def Employed_Bee_Phase(self):

        '''The number of Employed Bee must be equal to the food sources.'''           
        
        for i in range(len(self.food_source)): # Bees loop
            ''' Xold = Xnew if fit(Xnew) > fit(Xold)'''
            alpha = np.random.uniform(-1, 1)
            p = np.random.randint(0, len(self.food_source))
            j = np.random.randint(0, len(self.food_source[0]))
            Xp = self.food_source[p][j]
            old = self.food_source[i][j]
            new = old + (alpha * (old - Xp))
            temp = self.food_source[i]
            temp[j] = new 
            new_fitness_value = self.fitness_function_eq(temp)
            new_fitness = 1 / (1 + new_fitness_value) if new_fitness_value >= 0 else 1 + abs(new_fitness_value)

            if new_fitness > self.fitness[i]:   # minimum
                self.food_source[i][j] = new
                self.food_source[i] = np.clip(self.food_source[i], self.lower_bound, self.upper_bound)
                self.fitness[i] = new_fitness
                self.trial[i] = 0
            else:
                self.trial[i] += 1
            
    def Onlooker_Bee_Phase(self):
        for i in range(len(self.food_source)): 
            self.prob.append((0.9 * (self.fitness[i]/max(self.fitness))) + 0.1)
        
        i = 0
        bee = 0
        r = np.random.uniform(self.lower_bound, self.upper_bound)  
        while bee == (len(self.food_source)-1): 
            if r < self.prob[i]:
                r = np.random.uniform(self.lower_bound, self.upper_bound)
                alpha = np.random.uniform(-1, 1)
                p = np.random.randint(0, len(self.food_source))
                j = np.random.randint(0, len(self.food_source[0]))
                Xp = self.food_source[p][j]
                old = self.food_source[i][j]
                new = old + (alpha * (old - Xp))
                temp = self.food_source[i]
                temp[j] = new
                new_fitness_value = self.fitness_function_eq(temp)
                new_fitness = 1 / (1 + new_fitness_value) if new_fitness_value >= 0 else 1 + abs(new_fitness_value)

                if new_fitness > self.fitness[i]:
                    self.food_source[i][j] = new
                    self.food_source[i] = np.clip(self.food_source[i], self.lower_bound, self.upper_bound)
                    self.fitness[i] = new_fitness
                    self.trial[i] = 0
                else:
                    self.trial[i] += 1
                bee += 1
                
            i += 1
            if i == (len(self.prob)-1):
                i = 0
            
        self.prob = []

    def Scout_Bee_Phase(self):
        for i in range(len(self.trial)):
            if self.trial[i] >= self.max_trials:
                self.trial[i] = 0
                self.food_source[i] = np.random.uniform(self.lower_bound, self.upper_bound, len(self.food_source[i]))
                fitness_value = self.fitness_function_eq(self.food_source[i])
                self.fitness[i] = 1 / (1 + fitness_value) if fitness_value >= 0 else 1 + abs(fitness_value)
        self.best_solution = self.food_source[np.argmax(self.fitness)]
        self.best_fitness = np.max(self.fitness)


# Example usage -----------------------------------------------------------------------
        
# def fitness_function(x):
#     return np.sum(x) 

# population =   [[8.449, 7.757, 8.016],
#                 [8.077, 8.54 , 5.51 ],
#                 [8.573, 2.812, 5.901],
#                 [5.012, 4.503, 8.037],
#                 [4.95,  8.105, 4.743]]

# abc = ABC_Min(fitness_function,population,10,0,5)

# abc.run()





    


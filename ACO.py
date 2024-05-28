import math
import numpy as np
'''
Ant Colony Optimization (ACO) is a nature-inspired optimization algorithm based 
on the foraging behavior of ants. Introduced by Marco Dorigo in the early 1990s,
ACO is particularly effective for solving combinatorial optimization problems,
such as the Traveling Salesman Problem (TSP).
'''
class ACO:
    def __init__(self, graph, n_ants, n_iterations, evaporation_rate=0.5, pheromone_deposit=1.0):
        self.graph = graph
        self.pheromone = [1 for _ in range(len(graph)) for _ in range(len(graph))]
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.evaporation_rate = evaporation_rate
        self.pheromone_deposit = pheromone_deposit
        self.path = []
        self.index_to_letter = {i: chr(65 + i) for i in range(len(graph))}
        self.letter_to_index = {v: k for k, v in self.index_to_letter.items()}

    def run(self):
        for _ in range(self.n_iterations):
            all_paths = []
            for ant_id in range(self.n_ants):
                path_letters, total_distance = self.get_path()
                all_paths.append((path_letters, total_distance))
                print(f"Ant {ant_id + 1}: Path: {path_letters}, Distance: {total_distance}")

            self.update_pheromone(all_paths)
            
            shortest_path = min(all_paths, key=lambda x: x[1])
            print(f"Iteration {_ + 1}: Shortest Path: {shortest_path[0]}, Distance: {shortest_path[1]}")
            
            self.path.append(shortest_path)

    def get_path(self):
        points_n = int(math.sqrt(len(self.graph)))
        random_start_point = np.random.randint(0, points_n)
        start_row_index = random_start_point * points_n
        
        path = [random_start_point]
        visited = set(path)
        total_distance = 0
        
        while len(visited) < points_n:
            probability_of_paths = []
            indices = []
            
            total = sum(self.pheromone[i] * (1 / self.graph[i]) for i in range(start_row_index, start_row_index + points_n) if self.graph[i] != 0 and (i % points_n) not in visited)
            
            for i in range(start_row_index, start_row_index + points_n):
                if self.graph[i] != 0 and (i % points_n) not in visited:
                    indices.append(i)
                    probability_of_paths.append((self.pheromone[i] * (1 / self.graph[i])) / total)
            
            if not indices:
                break
            
            next_index = np.random.choice(indices, p=probability_of_paths)
            next_point = next_index % points_n
            total_distance += self.graph[next_index]
            path.append(next_point)
            visited.add(next_point)
            start_row_index = next_point * points_n
            
        path.append(random_start_point)
        total_distance += self.graph[path[-2] * points_n + random_start_point]
        
        path_letters = [self.index_to_letter[i] for i in path]
        
        return path_letters, total_distance

    def update_pheromone(self, all_paths):
        for i in range(len(self.graph)):
            self.pheromone[i] *= (1 - self.evaporation_rate)
        
        for path, distance in all_paths:
            pheromone_to_add = self.pheromone_deposit / distance
            for j in range(len(path) - 1):
                start = self.letter_to_index[path[j]]
                end = self.letter_to_index[path[j + 1]]
                graph_index = start * int(math.sqrt(len(self.graph))) + end
                self.pheromone[graph_index] += pheromone_to_add

# Example usage

# graph= [ 0, 5, 8, 4,
#          5, 0, 4, 15,
#          8, 4, 0, 1,
#          4, 15,1, 0 ]

# a = ACO(graph,5, 2)
# a.run()

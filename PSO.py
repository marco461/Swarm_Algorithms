import numpy as np

'''
Particle Swarm Optimization (PSO) algorithm,
PSO algorithm is designed to minimize the fitness function (Max).
'''
def PSO(fitness_function, population, max_iter, lower_bound, upper_bound, w, c1, c2):
    # print(population)
    # Initialize the particles
    particles = population
    num_particles, num_dimensions = particles.shape
    velocities = np.random.uniform(0, 1, (num_particles, num_dimensions))
    personal_best_scores = np.array([fitness_function(p) for p in particles])
    personal_best_positions = particles.copy()
    
    global_best_index = np.argmin(personal_best_scores)
    global_best_position = personal_best_positions[global_best_index]
    global_best_score = personal_best_scores[global_best_index]
    
    # Main loop
    for i in range(max_iter):
        for j in range(num_particles):
            # Update velocity
            r1 = np.random.uniform(0, 1, num_dimensions)
            r2 = np.random.uniform(0, 1, num_dimensions)
            velocities[j] = (w * velocities[j] +
                             c1 * r1 * (personal_best_positions[j] - particles[j]) +
                             c2 * r2 * (global_best_position - particles[j]))
            
            # Update position
            particles[j] += velocities[j]
            
            # Clip to boundaries
            particles[j] = np.clip(particles[j], lower_bound, upper_bound)
            
            # Update personal best
            score = fitness_function(particles[j])
            if score < personal_best_scores[j]:
                personal_best_scores[j] = score
                personal_best_positions[j] = particles[j].copy()
                
                # Update global best
                if score < global_best_score:
                    global_best_score = score
                    global_best_position = particles[j].copy()

        # Optionally print progress
        # print(f"Iteration {i+1}: Global Best Value: {global_best_position}, Score: {global_best_score}")

    return global_best_position, global_best_score

# Example usage -----------------------------------------------------------------------

# # Define the fitness function (example for a 4-dimensional problem)
# def fitness_function(x):
#     return np.sum(x**2)
# # Parameters
# num_particles = 5
# num_dimensions = 3
# lower_bound = -10
# upper_bound = 10
# population = np.random.uniform(lower_bound, upper_bound, (num_particles, num_dimensions))

# # Set the PSO parameters
# max_iter = 10
# w = 0.5
# c1 = 1.5
# c2 = 1.5
# # Run the PSO algorithm
# best_position, best_score = PSO(fitness_function, population, max_iter, lower_bound, upper_bound, w, c1, c2)

# print("Best Position:", best_position)
# print("Best Score:", best_score)


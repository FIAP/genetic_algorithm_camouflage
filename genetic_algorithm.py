import random
import numpy as np

# Define the target background color (you can change these values as needed)
target_color = (100, 150, 200)

# Define parameters for the genetic algorithm
population_size = 25
num_generations = 100

mutation_intensity = 0.001  # Mutation intensity as a percentage
mutation_rate = 0.01 # Mutation Probability


# Function to calculate the fitness of an individual color
def calculate_fitness(color):
    # Fitness is the sum of the absolute differences from the target color
    return sum(abs(color[i] - target_color[i]) for i in range(3))

# Generate a random population of colors
def generate_random_population(size):
    return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(size)]

# Perform one-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, 2)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


# Perform mutation by changing colors with a specified intensity
def mutate(color, intensity=mutation_intensity, sigma=1):

    mutated_color = list(color)

    for i in range(3):
        if random.random() < mutation_rate:
            # mutated_color[i] = int(color[i] * (1 + (random.choice([-1, 1])) * mutation_intensity)) ## percentage mutation
            mutated_color[i] += round(np.random.normal(0, sigma)) # Gaussian mutation
    return tuple(mutated_color)


if __name__ == '__main__':
    # Main genetic algorithm loop
    population = generate_random_population(population_size)
    
    # Lists to store best fitness and generation for plotting
    best_fitness_values = []
    best_colors = []
    
    for generation in range(num_generations):
        population = sorted(population, key=calculate_fitness)
    
        best_fitness = calculate_fitness(population[0])
        best_color = population[0]
        best_fitness_values.append(best_fitness)
        best_colors.append(best_color)
    
        print(f"Generation {generation}: Best fitness = {best_fitness}, Best color = {best_color}, Target = {target_color}")
    
    
    
        new_population = [population[0]]  # Keep the best individual
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population[:10], k=2)  # Select parents from the top 10 individuals
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])
    
        population = new_population
    
    # Print the best color found
    best_color = population[0]
    print(f"Best Color: {best_color}")




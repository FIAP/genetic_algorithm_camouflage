# Matrix of Squares Genetic Algorithm

This repository contains a simple interactive Python program that demonstrates a genetic algorithm optimizing a matrix of colored squares to match a target color, simulating the camouflage effect on nature.

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3
- Pygame library: `pip install pygame`
- Matplotlib library: `pip install matplotlib`
- Numpy library: `pip install numpy`

## How to Run

Execute the following command in your terminal to run the program:

```bash
python run.py
```

## Instructions

- **Quit the Program:** Press the 'q' key to quit the program.

## Genetic Algorithm Parameters

The genetic algorithm is configured with the following parameters:

- **Population Size:** 25
- **Number of Generations:** 100
- **Mutation Intensity:** 0.001 (Percentage mutation intensity)
- **Mutation Rate:** 0.01 (Mutation probability)

You can change these values and see what happens to the execution. 

## Code Structure

- **run.py:** The main script containing the Pygame loop and genetic algorithm logic.
- **genetic_algorithm.py:** Module with genetic algorithm functions (crossover, mutation, fitness calculation).

## Genetic Algorithm Process

1. **Initialization:** Randomly generates a population of colored matrices.
2. **Evaluation:** Calculates the fitness of each individual in the population based on the color difference from the target color.
3. **Selection:** Sorts the population based on fitness and selects the top individuals.
4. **Crossover:** Performs one-point crossover on selected parents to create new individuals.
5. **Mutation:** Introduces random mutations in the color values of individuals.
6. **Next Generation:** Forms a new population using the best individuals from the previous generation and the newly created ones.
7. **Repeat:** Iterates through the specified number of generations.

## Visualization

The program visualizes the optimization process by displaying the best fitness value and the corresponding matrix of colored squares at each generation. The target color and the best color found are also displayed for comparison.

Feel free to explore and modify the code to experiment with different genetic algorithm configurations and applications.


## How to Contribute

We welcome contributions to improve and enhance the functionality of this genetic algorithm demonstration. If you're interested in contributing, follow these steps:

1. Fork the repository to your GitHub account.
2. Clone the forked repository to your local machine.
3. Make your desired changes and improvements.
4. Test your changes to ensure they work as expected.
5. Commit your changes with clear and concise commit messages.
6. Push the changes to your GitHub repository.
7. Create a pull request from your repository to the original repository.

Contributions can include bug fixes, feature additions, documentation improvements, or any other enhancements that can benefit the project. Feel free to open an issue for discussions before making significant changes.

## How to Cite

If you use or refer to this genetic algorithm demonstration in your research or work, please consider citing it. You can use the following BibTeX entry as a reference:

```bibtex
@misc{camouflage-genetic-algorithm,
  author       = {Polimante, Sergio},
  title        = {Camouflage Genetic Algorithm},
  howpublished = {\url{https://github.com/yourusername/matrix-genetic-algorithm}},
  year         = {2024},
}
```

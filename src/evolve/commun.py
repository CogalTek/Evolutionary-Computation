import random
from src.score import getScore

# Evolve a generation by crossover and mutation
def evolve(generation, arraySize):
    mutationRate = min(0.1, 1 / arraySize)
    populationSize = max(10, arraySize * 2)

    # Sort the generation based on score, select the best parents
    sortedGeneration = sorted(generation, key=lambda x: x[1], reverse=True)
    bestParents = sortedGeneration[:min(5, len(sortedGeneration))]

    if len(bestParents) < 2:
        return generation  # Return the same generation if not enough parents

    newGeneration = []

    while len(newGeneration) < populationSize:
        parent1, parent2 = random.sample(bestParents, 2)

        # Crossover: Combine elements from both parents
        child = []
        for i in range(arraySize):
            if random.random() < 0.5:
                child.append(parent1[0][i])
            else:
                child.append(parent2[0][i])

        # Mutation: Randomly change an element
        if random.random() < mutationRate:
            mutationIndex = random.randint(0, arraySize - 1)
            child[mutationIndex] = random.randint(-1, arraySize - 1)

        # Calculate the score of the child
        child_score = getScore([child], arraySize)[0][1]
        newGeneration.append((child, child_score))

    return newGeneration
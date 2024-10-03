import sys
import math
import random
from src.score import getScore  # Import the scoring function
from src.evolve.commun import evolve
from src.evolve.one_point import evolve_one_point_crossover
from src.evolve.two_point import evolve_two_point_crossover

evolveType = 'commun'

# Check if two points are on the same diagonal
def areOnSameDiagonal(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # If any point is out of bounds, return False
    if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
        return False

    return abs(x2 - x1) == abs(y2 - y1)

# Remove elements on the same diagonal
def correctionDiagonal(validArrays, discardedArrays):
    validArraysCopy = validArrays[:]

    for value in validArraysCopy:
        positions = [(i, val) for i, val in enumerate(value)]
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                if areOnSameDiagonal(positions[i], positions[j]):
                    discardedArrays.append(value)
                    if value in validArrays:
                        validArrays.remove(value)
                    break
    return validArrays

# Validate and correct the array (remove invalid or redundant elements)
def correction(array):
    validArrays = []
    discardedArrays = []
    for subArray in array:
        isValid = True
        for value in subArray:
            # Check if the value is an integer and if it's unique in the subArray
            if not isinstance(value, int) or (value >= 0 and subArray.count(value) > 1):
                isValid = False
        if isValid:
            validArrays.append(subArray)
        else:
            discardedArrays.append(subArray)

    if not validArrays:
        return None
    return correctionDiagonal(validArrays, discardedArrays)

# Generate an initial population of arrays
def genArray(arraySize):
    population_size = max(10, arraySize * 2)
    array = []
    for _ in range(population_size):
        subArray = [random.randrange(-1, arraySize) for _ in range(arraySize)]
        array.append(subArray)
    return array



# Estimate the expected number of generations needed to solve the N-queens problem
def expected_generations(population_size, mutation_rate, success_probability, n):
    initial_prob = 1 / (n ** n)  # Very low initial probability
    effective_prob = initial_prob * success_probability  # Probability with genetic improvement

    # Average number of generations to find a solution
    generations = math.log(1 - success_probability) / math.log(1 - effective_prob)
    return generations

# Main process to solve the N-queens problem using evolutionary computation
def processCreate(arraySize):
    array = genArray(arraySize)
    generation = []
    max_generations = 10000000

    population_size = max(10, arraySize * 2)
    mutation_rate = 0.1
    success_probability = 0.5

    estimated_generations = expected_generations(population_size, mutation_rate, success_probability, arraySize)
    print(f"Expected number of generations to solve N-queens with N={arraySize}: {estimated_generations:.2f}")

    for i in range(max_generations):
        array = correction(array)
        if array is not None and len(array) > 0:
            generation = getScore(array, arraySize)
            print(i + 1, ":", generation)

            best_score = max(generation, key=lambda x: x[1])[1]
            if best_score == arraySize:
                return  # Stop if solution found

            match evolveType:
                case 'commun':
                    array = evolve(generation, arraySize)
                case 'one':
                    array = evolve_one_point_crossover(generation, arraySize)
                case 'two':
                    array = evolve_two_point_crossover(generation, arraySize)
        else:
            # print(i + 1, ":", "[]") # Display empty array
            array = genArray(arraySize)

    if i == max_generations - 1:
        print("Maximum generations reached without finding a solution")

# Start the process, handling the command-line arguments
def processStart():
    try:
        if "-n" not in sys.argv:
            raise ValueError("The '-n' option is missing from the arguments.")

        if "-s" not in sys.argv:
            raise ValueError("The '-s' option is missing from the arguments.")

        if len(sys.argv) <= (sys.argv.index("-n") + 1):
            raise IndexError("No argument provided after '-n'.")

        if len(sys.argv) <= (sys.argv.index("-s") + 1):
            raise IndexError("No argument provided after '-s'.")

        index = sys.argv.index("-n") + 1
        evolveTypeIndex = sys.argv.index("-s") + 1

        if not sys.argv[index].isnumeric() or int(sys.argv[index]) < 1:
            raise ValueError("The argument after '-n' must be an integer >= 1.")

        if sys.argv[evolveTypeIndex] != "commun" and sys.argv[evolveTypeIndex] != "one" and sys.argv[evolveTypeIndex] != "two":
            raise ValueError("The argument after '-s' is not good.")
        else:
            evolveType = sys.argv[evolveTypeIndex]

        return processCreate(int(sys.argv[index]))

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except IndexError as ie:
        print(f"Index Error: {ie}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

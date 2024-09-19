import sys
import random
from src.score import getScore

def howManyPossibilities(arraySize):
    return arraySize * arraySize

def areOnSameDiagonal(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
        return False
    return abs(x2 - x1) == abs(y2 - y1)

def correctionDiagonal(arrayVerifier, arrayPoubelle):
    arrayVerifierCopy = arrayVerifier[:]

    for value in arrayVerifierCopy:
        inter = [(i, val) for i, val in enumerate(value)]
        for i in range(len(inter)):
            for j in range(i + 1, len(inter)):
                if areOnSameDiagonal(inter[i], inter[j]):
                    arrayPoubelle.append(value)
                    if value in arrayVerifier:
                        arrayVerifier.remove(value)
                    break
    return arrayVerifier

def correction(array):
    arrayVerifier = []
    arrayPoubelle = []
    for n in array:
        valide = True
        for value in n:
            if not isinstance(value, int) or (value >= 0 and n.count(value) > 1):
                valide = False
        if valide:
            arrayVerifier.append(n)
        else:
            arrayPoubelle.append(n)
    
    if not arrayVerifier:
        return None
    return correctionDiagonal(arrayVerifier, arrayPoubelle)

def genArray(arraySize):
    population_size = max(10, arraySize * 2) 
    array = []
    for _ in range(population_size):
        subArray = [random.randrange(-1, arraySize) for _ in range(arraySize)]
        array.append(subArray)
    return array

def evolve(generation, arraySize, mutationRate=None, populationSize=None):
    if mutationRate is None:
        mutationRate = min(0.1, 1 / arraySize)  
    if populationSize is None:
        populationSize = max(10, arraySize * 2) 

    sortedArray = sorted(generation, key=lambda x: x[1], reverse=True)
    bestParents = sortedArray[:min(5, len(sortedArray))] 

    if len(bestParents) < 2:
        print(f"Pas assez de parents pour générer la nouvelle population, taille : {len(bestParents)}")
        return generation  

    newGeneration = []

    while len(newGeneration) < populationSize:
        parent1, parent2 = random.sample(bestParents, 2)

        # Croisement : combine les éléments des deux parents
        child = []
        for i in range(arraySize):
            if random.random() < 0.5:
                child.append(parent1[0][i])
            else:
                child.append(parent2[0][i])

        # Mutation
        if random.random() < mutationRate:
            mutationIndex = random.randint(0, arraySize - 1)
            child[mutationIndex] = random.randint(-1, arraySize - 1)

        # Calculer le score de l'enfant
        child_score = getScore([child], arraySize)[0][1]
        newGeneration.append((child, child_score))

    return newGeneration

def displayGeneration(generation, genNumber):
    print(f"\033[36mGénération {genNumber} :\033[0m")
    
    max_score = max(generation, key=lambda x: x[1])[1] if generation else 0
    
    for i, (array, score) in enumerate(generation):
        color = "\033[32m" if score == max_score else "\033[31m"
        print(f"{color}Score {i + 1} : {score}\033[0m")
        displayBoard(array)

def displayBoard(array):
    """Affiche le tableau 2D des reines."""
    n = len(array)
    for row in range(n):
        line = ""
        for col in range(n):
            if array[row] == col:
                line += " Q "
            else:
                line += " . " 
        print(line)
    print("\n")

def processCreate(arraySize):
    array = genArray(arraySize)
    generation = []
    max_generations = 1000

    for i in range(max_generations):
        array = correction(array)
        if array is not None and len(array) > 0:
            generation = getScore(array, arraySize)
            displayGeneration(generation, i + 1)
            
            # Check if we've found a solution
            best_score = max(generation, key=lambda x: x[1])[1]
            if best_score == arraySize:
                print(f"Solution found in generation {i+1}")
                break
            
            array = evolve(generation, arraySize)
        else:
            array = genArray(arraySize)
    
    if i == max_generations - 1:
        print("Maximum generations reached without finding a solution")

def processStart():
    try:
        if "-n" not in sys.argv:
            raise ValueError("L'option '-n' est manquante dans les arguments.")

        if len(sys.argv) <= (sys.argv.index("-n") + 1):
            raise IndexError("Aucun argument après '-n'.")

        index = sys.argv.index("-n") + 1

        if not sys.argv[index].isnumeric() or int(sys.argv[index]) < 1:
            raise ValueError("L'argument après '-n' doit être un entier supérieur ou égal à 1.")

        processCreate(int(sys.argv[index]))

    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
    except IndexError as ie:
        print(f"Erreur d'index : {ie}")
    except Exception as e:
        print(f"Une exception s'est produite : {e}")
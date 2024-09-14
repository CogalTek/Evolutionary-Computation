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
            if value >= 0 and n.count(value) > 1:
                valide = False
        if valide:
            arrayVerifier.append(n)
        else:
            arrayPoubelle.append(n)
    return correctionDiagonal(arrayVerifier, arrayPoubelle) if arrayVerifier else None

def genArray(arraySize):
    array = []
    for _ in range(howManyPossibilities(arraySize)):
        subArray = [random.randrange(-1, arraySize) for _ in range(arraySize)]
        array.append(subArray)
    return array

def evolve(array, arraySize, mutationRate=0.1, populationSize=10):
    # On trie les tableaux par score, du meilleur au pire
    sortedArray = sorted(array, key=lambda x: x[1], reverse=True)
    bestParents = sortedArray[:5]

    newGeneration = []

    while len(newGeneration) < populationSize:
        parent1, parent2 = random.sample(bestParents, 2)  # a revoir

        # Croisement : combine les éléments des deux parents
        child = []
        for i in range(arraySize):
            if random.random() < 0.5:
                child.append(parent1[0][i])
            else:
                child.append(parent2[0][i])

        # Mutation
        if random.random() < mutationRate:
            mutationIndex = random.randint(0, arraySize) # revoir arraySize
            child[mutationIndex] = random.randint(-1, arraySize)

        newGeneration.append(child)

    return newGeneration


# Fonction pour afficher la génération avec des couleurs
def displayGeneration(generation, genNumber):
    print(f"\033[36mGénération {genNumber} :\033[0m")  # Bleu pour le numéro de génération
    for i, (score, array) in enumerate(generation):
        color = "\033[32m" if score == max(generation, key=lambda x: x[0])[0] else "\033[31m"
        print(f"{color}Score {i + 1} : {score}, Tableau : {array}\033[0m")  # Vert si meilleur score, Rouge sinon

def processCreate(arraySize):
    array = genArray(arraySize)
    generation = []

    for i in range(10):
        array = correction(array)
        if array is not None:
            score = getScore(array, arraySize)
            generation.append((i, score))
            array = evolve(score, arraySize)
            displayGeneration(score, i + 1)  # Affichage de l'évolution avec couleurs
        else:
            array = genArray(arraySize)

def processStart():
    try:
        if "-x" not in sys.argv:
            raise ValueError("L'option '-x' est manquante dans les arguments.")

        if len(sys.argv) <= (sys.argv.index("-x") + 1):
            raise IndexError("Aucun argument après '-x'.")

        index = sys.argv.index("-x") + 1

        if not sys.argv[index].isnumeric() or int(sys.argv[index]) < 1:
            raise ValueError("L'argument après '-x' doit être un entier supérieur ou égal à 1.")

        processCreate(int(sys.argv[index]))

    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
    except IndexError as ie:
        print(f"Erreur d'index : {ie}")
    except Exception as e:
        print(f"Une exception s'est produite : {e}")

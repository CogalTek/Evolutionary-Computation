import sys
import random
from src.score import getScore

def howManyPossibilities (arraySize):
    return arraySize * arraySize

def areOnSameDiagonal (p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
        return False
    if abs(x2 - x1) == abs(y2 - y1):
        return True
    return False

def correctionDiagonal(arrayVerifier, arrayPoubelle):
    arrayVerifierCopy = arrayVerifier[:]

    for index, value in enumerate(arrayVerifierCopy):
        inter = []

        for i, val in enumerate(value):
            inter.append((i, val))
        for i, val in enumerate(inter):
            j = i + 1
            while j < (len(inter)):
                if areOnSameDiagonal(inter[i], inter[j]):
                    arrayPoubelle.append(value)
                    if value in arrayVerifier:
                        arrayVerifier.remove(value)
                    break
                j += 1

    print("\033[32mValide\033[0m")
    for n in arrayVerifier:
        print(n)
    print("\033[31mInvalide\033[0m")
    for n in arrayPoubelle:
        print(n)
    return arrayVerifier


def correction (array):
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
    if len(arrayVerifier):
        return correctionDiagonal(arrayVerifier, arrayPoubelle)

def processCreate (arraySize):
    array = []
    for i in range(howManyPossibilities(arraySize)):
        subArray = []
        for n in range(arraySize):
            subArray.append(random.randrange(-1, arraySize))
        array.append(subArray)

    # Prise des score
    getScore(correction(array), arraySize)
    # on prend ce qu'il y a
    # si il y en a beaucoup on prend les n meilleur
    # on les fait evoluer
    # on relance


def processStart ():
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

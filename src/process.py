import sys
import random

def howManyPossibilities (arraySize):
    return arraySize * arraySize

def areOnSameDiagonal (p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # Diagonales de gauche à droite
    if abs(x1 - y1) == abs(x2 - y2):
        return True

    # Diagonales de droite à gauche
    if (x1 + y1) == (x2 + y2):
        return True

    return False

def correction (array):
    # print("\033[32mCeci est en vert\033[0m")
    # print("\033[31mCeci est en rouge\033[0m")

    for n in array:
        valide = True
        for value in n:
            if value >= 0 and n.count(value) > 1:
                valide = False
        if valide:
            print(f"\033[32m{n}\033[0m")
        else:
            print(f"\033[31m{n}\033[0m")

def processCreate (arraySize):
    # Calculer le nombre de possibilité
    array = []
    # Generation des tableau
    for i in range(howManyPossibilities(arraySize)):
        subArray = []
        for n in range(arraySize):
            subArray.append(random.randrange(-1, arraySize - 1))
        array.append(subArray)
    # print(array)
    # Verification du score
    correction(array)


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

import sys
import random

def howManyPossibilities (arraySize):
    return arraySize * arraySize

def areOnSameDiagonal (p1, p2):
    # print("\033[36mareOnSameDiagonal:\033[0m")
    # print(p1, p2)
    x1, y1 = p1
    x2, y2 = p2

    if abs(x1 - y1) == abs(x2 - y2):
        return True
    if (x1 + y1) == (x2 + y2):
        return True
    return False

def correctionDiagonal (arrayVerifier, arrayPoubelle):
    print("\033[35mCorrectionDiagonal:\033[0m")
    for index, value in enumerate(arrayVerifier):
        print("", value)
        inter = []
        for i, val in enumerate(value):
            inter.append(((i), (val)))
            # print(inter[len(inter) - 1])
        for i, val in enumerate(inter):
            print("----", inter[i])
            j = i
            while j < (len(inter) - 1):
                print("--------", inter[j], areOnSameDiagonal(inter[i], inter[j]))
                if areOnSameDiagonal(inter[i], inter[j]):
                    arrayPoubelle.append(value)
                    arrayVerifier.pop(index)
                    break
                j += 1
    print("\033[32mValide\033[0m")
    for n in arrayVerifier:
        print(n)
    print("\033[31mInvalide\033[0m")
    for n in arrayPoubelle:
        print(n)


def correction (array):
    print("\033[35mCorrectionPerpendiculaire:\033[0m")
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

    print("\033[32mValide\033[0m")
    for n in arrayVerifier:
        print(n)
    print("\033[31mInvalide\033[0m")
    for n in arrayPoubelle:
        print(n)
    if len(arrayVerifier):
        correctionDiagonal(arrayVerifier, arrayPoubelle)

def processCreate (arraySize):
    # Calculer le nombre de possibilité
    array = []
    # Generation des tableau
    for i in range(howManyPossibilities(arraySize)):
        subArray = []
        for n in range(arraySize):
            subArray.append(random.randrange(-1, arraySize))
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

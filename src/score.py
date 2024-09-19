def getScore(array, maxSize):
    scoredArray = []

    for n in array:
        if not all(isinstance(x, int) for x in n):
            raise ValueError(f"Tous les éléments doivent être des entiers : {n}")

        score = maxSize - n.count(-1)
        scoredArray.append((n, score))

    return scoredArray

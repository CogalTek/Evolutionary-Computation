def getScore(array, max):
    scoredArray = []
    for n in array:
        scoredArray.append((n, max - n.count(-1)))
    return scoredArray

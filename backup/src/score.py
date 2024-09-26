def getScore(array, maxSize):
    scoredArray = []
    
    for n in array:
        # Vérification que tous les éléments de 'n' sont des entiers
        if not all(isinstance(x, int) for x in n):
            raise ValueError(f"Tous les éléments doivent être des entiers : {n}")
        
        # Calcul du score, en pénalisant les -1
        score = maxSize - n.count(-1)
        scoredArray.append((n, score))
    
    return scoredArray

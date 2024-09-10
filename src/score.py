def getScore (array, max):
    print("------- getScore")
    for n in array :
        print(n, ":", (max - n.count(-1)))
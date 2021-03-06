import random


def randomList(n):
    iList = []
    for i in range(n):
        iList.append(random.randrange(1000))
    return iList


def bubbleSort(iList):
    if len(iList) <= 1:
        return iList
    for i in range(1, len(iList)):
        for j in range(0, len(iList) - i):
            if iList[j] >= iList[j + 1]:
                iList[j], iList[j + 1] = iList[j + 1], iList[j]
    return iList


if __name__ == "__main__":
    iList = randomList(10)
    print(iList)
    bubbleSort(iList)
    print(bubbleSort(iList))

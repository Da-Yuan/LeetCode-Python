import random
import numpy as np


def generator(maxSize, maxNum):
    # size = random.randint(1, maxSize)
    # return random.sample(range(maxNum), size)
    return np.random.randint(1, maxNum, maxSize).tolist()


def flat(m, tR, tC, dR, dC):
    print(tR, tC, dR, dC)
    re = []
    if tR == dR:
        print('here')
        for i in range(tC, dC+1):
            re.append(m[tR][i])
    elif tC == dC:
        for i in range(tR, dR+1):
            re.append(m[i][tC])
    else:
        curR, curC = tR, tC
        while curC != dC:
            re.append(m[tR][curC])
            curC += 1
        while curR != dR:
            re.append(m[curR][dC])
            curR += 1
        while curC != tC:
            re.append(m[dR][curC])
            curC -= 1
        while curR != tR:
            re.append(m[curR][tC])
            curR -= 1
    return re


def spiralOrder(matrix):
    if not matrix:
        return matrix
    rem = []
    tR, tC = 0, 0
    dR, dC = len(matrix)-1, len(matrix[0])-1
    while tR <= dR and tC <= dC:
        rem.extend(flat(matrix, tR, tC, dR, dC))
        tR += 1
        tC += 1
        dR -= 1
        dC -= 1
        print(rem)
    return rem


# matrix = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]]
print(spiralOrder(matrix))
# print(flat(matrix, 0, 0, 2, 2))


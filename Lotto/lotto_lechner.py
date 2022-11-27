import random as rnd

import numpy as np


def lotto():
    counter = 0
    arr = (np.arange(1, 46))
    while counter < 6:
        x = rnd.randint(arr[0], arr[44 - counter])
        print(arr)
        arr[x - 1], arr[44 - counter] = arr[44 - counter], arr[x - 1]
        print(arr)
        print()
        print(x)
        counter = counter + 1


def lotto_dict():
    #arr = (np.arange(1, 46))
    dictionary = {}
    for i in range(1, 46):
        dictionary [i] = 0
    for i in range(0, 1000):
        dictionary[int(rnd.random()*45+1)] += 1
    print(dictionary)


lotto()
print("-----------------------------------------------------")
lotto_dict()

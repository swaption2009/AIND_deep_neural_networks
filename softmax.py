import numpy as np


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    output = []
    for i in expL:
        output.append(i * 1.0 / sumExpL)

    return output
import numpy as np
import string


def change2coordinates(node):
    letter = node[0]
    letter = letter.capitalize()
    x = float(
        string.ascii_uppercase.index(
            letter
        )
    )
    y = float(node[1])
    return np.array([x, y])

def change2name(x, y):
    x_s = string.ascii_uppercase[int(x)]
    y_s = str(int(y))
    return x_s + y_s

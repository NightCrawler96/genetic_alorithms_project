import numpy as np
import string


def letters():
    alphabet = string.ascii_uppercase.replace('V', "")
    return alphabet


def change2coordinates(node):
    letter = node[0]
    letter = letter.capitalize()
    alphabet = letters()
    x = float(
        alphabet.index(
            letter
        )
    )
    y = float(node[1])
    return np.array([x, y])


def change2name(x, y):
    alphabet = letters()
    x_s = alphabet[int(x)]
    y_s = str(int(y))
    return x_s + y_s

import numpy as np
from genetic_alghorithm.random_path_maker import random_connection
from genetic_alghorithm.helper_functions import change2coordinates


def make_kid(left, right, cut, edges):
    beggining = left[:cut]
    end = right[cut:]
    last_of_beggining = change2coordinates(beggining[-1])
    first_of_end = change2coordinates(end[0])
    diff_distance = np.linalg.norm(first_of_end - last_of_beggining)
    if diff_distance > 1.5:
        s, e = beggining[-1], end[0]
        conn, _ = random_connection(s, e, edges, d=10)
        kid = beggining + conn[1:-1] + end
    else:
        kid = beggining + end
    return kid


def crossing(parent_0, parent_1, edges):
    path_0 = parent_0[1]
    path_1 = parent_1[1]

    cut = np.random.randint(1, min(len(path_0) - 1, len(path_1) - 1))
    kid_0 = make_kid(path_0, path_1, cut, edges)
    kid_1 = make_kid(path_1, path_0, cut, edges)

    return kid_0, kid_1

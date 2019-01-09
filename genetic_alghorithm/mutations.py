import numpy as np

from genetic_alghorithm.helper_functions import change2coordinates, change2name


def mutation(specimen):
    point = np.random.randint(1, len(specimen) - 1)
    old_node = specimen[point]
    prev = specimen[point - 1]
    next = specimen[point + 1]
    on_coords = change2coordinates(old_node)
    p_coords = change2coordinates(prev)
    n_coords = change2coordinates(next)
    po_dist = np.linalg.norm(p_coords - on_coords)
    on_dist = np.linalg.norm(n_coords - on_coords)
    pn_dist = np.linalg.norm(p_coords - n_coords)
    new_node = [-2, -2]
    if pn_dist < 2:
        # O-O    O
        #   | =>  \
        #   O      O
        new_specimen = specimen[:point] + specimen[(point + 1):]
        return new_specimen
    if 1 < on_dist < 2 and 1 < po_dist < 2:
        # do nothing
        return specimen
    if (po_dist == 1 and on_dist > 1) or (po_dist > 1 and on_dist == 1):
        # O-O       O
        #    \  <=>  \
        #     O       O-O
        if on_coords[1] == p_coords[1]:
            new_node = [on_coords[0], n_coords[1]]
        elif on_coords[1] == n_coords[1]:
            new_node = [on_coords[0], p_coords[1]]
        elif on_coords[0] == p_coords[0]:
            new_node = [n_coords[0], on_coords[1]]
        elif on_coords[0] == n_coords[0]:
            new_node = [p_coords[0], on_coords[1]]
        else:
            raise Exception("Out of options?")
    if on_dist == 1 and po_dist == 1:
        # O      O
        # |     /
        # O => O
        # |     \
        # O      O
        p = np.random.randint(0, 1)
        min_coords = [0, 0]

        if p_coords[1] == on_coords[1]:
            # horizontal
            if p == 0 or on_coords[1] == min_coords[1]:
                new_node = [on_coords[0], on_coords[1] + 1]
            else:
                new_node = [on_coords[0], on_coords[1] - 1]
        else:
            # vertical
            if p == 0 or on_coords[0] == min_coords[0]:
                new_node = [on_coords[0] + 1, on_coords[1]]
            else:
                new_node = [on_coords[0] - 1, on_coords[1]]
    if 1 < on_dist < 2 and 1 < po_dist < 2 and pn_dist == 2:
        #   O   O
        #  /    |
        # O  => O
        #  \    |
        #   O   O
        if n_coords[0] == p_coords[0]:
            new_node = [n_coords[0], on_coords[1]]
        else:
            new_node = [on_coords[0], n_coords[1]]
    new_prev_curr_dist = np.linalg.norm(new_node - p_coords)
    new_next_curr_dist = np.linalg.norm(new_node - n_coords)
    if new_next_curr_dist > 1.5 or new_prev_curr_dist > 1.5:
        raise Exception("Error during mutation")

    new_node = change2name(new_node[0], new_node[1])
    specimen[point] = new_node

    return specimen

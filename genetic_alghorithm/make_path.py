import numpy as np

import genetic_alghorithm.random_path_maker as rpm
from genetic_alghorithm.crossings import crossing
from genetic_alghorithm.mutations import mutation
from Edges_dijkstra import Edges_normal


def make_population(start, finish, edges, specimen_num):
    _specimen = []
    _rewards = []
    for _ in range(specimen_num):
        s, r = rpm.random_connection(start, finish, edges)
        _rewards.append(r)
        _specimen.append(s)

    return _specimen, _rewards


def threshold(population, rewards, parents_prop=.5):
    t = int(len(population) * parents_prop)
    pop_dict = {}
    for p, r in zip(population, rewards):
        pop_dict[r] = p
    rewards.sort()
    best_rewards = rewards[:t]
    probabilities = np.ones(len(best_rewards)) / len(best_rewards)
    selections = np.random.uniform(0, 1, t)
    parents = []
    for sel_p in selections:
        total_p = 0
        for r, p in zip(best_rewards, probabilities):
            total_p += p
            if sel_p < total_p:
                parents.append(pop_dict[r])
                break

    return parents


edges = Edges_normal.edges
start = "b0"
fin = "f9"
pop_num = 100
iterations = 100
select = .5
pc = .9
pm = .3
population, rewards = make_population(start, fin, edges, pop_num)


def estimate_rewards(population):
    return np.random.uniform(0, 100, len(population))


for _ in range(iterations):
    parents = threshold(population, rewards)

    pairs_num = int((len(population) * (1 - select)) / 2)
    kids = []
    parents_i = np.arange(len(parents))
    pairs_i = [np.random.choice(parents_i, size=2) for _ in range(pairs_num)]
    pairs = np.array([[parents[i[0]], parents[i[1]]] for i in pairs_i])

    for p0, p1 in pairs:
        crosing_lottery = np.random.uniform(0, 1)
        if crosing_lottery < pc:
            k0, k1 = crossing(p0, p1)
        else:
            k0, k1 = p0, p1

        mutation_lottery = np.random.uniform(0, 2)

        if mutation_lottery[0] < pm:
            k0 = mutation(k0)
        if mutation_lottery[1] < pm:
            k0 = mutation(k1)
        kids.append(k0)
        kids.append(k1)
    population = parents + kids
    rewards = estimate_rewards(population)


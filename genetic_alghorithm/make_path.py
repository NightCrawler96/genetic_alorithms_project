import numpy as np

import genetic_alghorithm.random_path_maker as rpm
from genetic_alghorithm.crossings import crossing
from genetic_alghorithm.mutations import mutation
from Edges_dijkstra import Edges_normal

cost_specimen = [('cost', float), ('specimen', list)]


def make_population(start, finish, edges, specimen_num):
    _specimen = []
    _costs = []
    for _ in range(specimen_num):
        s, r = rpm.random_connection(start, finish, edges, d=.1)
        _costs.append(r)
        _specimen.append(s)

    return _specimen, _costs


def combine(population, costs):
    pop = []
    for p, r in zip(population, costs):
        pop.append((r, p))
    pop = np.array(pop, dtype=cost_specimen)
    return pop


def threshold(population, costs, parents_prop=.5):
    t = int(len(population) * parents_prop)
    pop = combine(population, costs)
    pop.sort(order='cost')
    parents = pop[:t]

    return parents


edges = Edges_normal.edges
start = 'a0'
fin = 'l8'
pop_num = 100
iterations = 100
select = .5
pc = .9
pm = .2
population, costs = make_population(start, fin, edges, pop_num)


def estimate_costs(population):
    cost = 0
    list_of_costs = []

    for path in population:
        for i in range(len(path)):
            if i < len(path) - 1:
                for j in range(len(Edges_normal.edges)):
                    if path[i] == Edges_normal.edges[j][0] and path[i+1] == Edges_normal.edges[j][1]:
                        value = Edges_normal.edges[j][2]
                        cost += value
        list_of_costs.append(cost)
        cost = 0

    rewards = np.array([i for i in list_of_costs])

    return rewards


for _ in range(iterations):
    parents = threshold(population, costs)

    pairs_num = int((len(population) * (1 - select)) / 2)
    kids = []
    parents_i = np.arange(len(parents))
    pairs_i = [np.random.choice(parents_i, size=2) for _ in range(pairs_num)]
    pairs = np.array([[parents[i[0]], parents[i[1]]] for i in pairs_i])

    for p0, p1 in pairs:
        crosing_lottery = np.random.uniform(0, 1)
        if crosing_lottery < pc:
            k0, k1 = crossing(p0, p1, edges)
        else:
            k0, k1 = p0[1], p1[1]

        mutation_lottery = np.random.uniform(0, 1, 2)

        if mutation_lottery[0] < pm:
            k0 = mutation(k0)
        if mutation_lottery[1] < pm:
            k0 = mutation(k1)
        kids.append(k0)
        kids.append(k1)
    population = [p[1] for p in parents] + kids
    costs = estimate_costs(population)

final_pop = combine(population, costs)
final_pop.sort(order='cost')

print(final_pop)

best_s = final_pop[0]
best_path = best_s[1]
best_cost = best_s[0]

# print(best_s[1])

print("Best path:")
print(best_path)
print("cost: " + str(best_cost))


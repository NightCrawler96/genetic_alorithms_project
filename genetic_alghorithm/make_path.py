import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Edges_graph.Edges as Edges_file
import matplotlib.image as mpimg

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


def estimate_costs(pop):
    cost = 0
    list_of_costs = []

    for path in pop:
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


def create_graph_nodes_and_dict_nodes_with_pos():
    list_of_keys_dict = []
    list_of_values_dict = []
    os_x = 0
    for letter in letters:
        for number in range(0, 10):
            name_node = letter + str(number)
            values_of_pos = os_x, number

            G.add_node(name_node, pos=(os_x, number))

            list_of_keys_dict.append(name_node)
            list_of_values_dict.append(values_of_pos)
        os_x += 1

    data = dict(zip(list_of_keys_dict, list_of_values_dict))

    return data


def create_graph_edges(G):
    weight_normal = 1
    weight_mountain = 10

    Edges_file.create_edges_for_series_A(G, weight_normal)
    Edges_file.create_edges_for_series_Z(G, weight_normal)

    for ind, letter in enumerate(letters):
        if letter != 'A' and letter != 'Z':
            for i in range(0, 10):
                if i != 9:
                    start_name = letter + str(i)
                    first = letters[ind - 1] + str(i + 1)
                    second = letters[ind] + str(i + 1)
                    third = letters[ind + 1] + str(i)
                    fourth = letters[ind + 1] + str(i + 1)

                    G.add_edge(start_name, first, weight=weight_normal)
                    G.add_edge(start_name, second, weight=weight_normal)
                    G.add_edge(start_name, third, weight=weight_normal)
                    G.add_edge(start_name, fourth, weight=weight_normal)
                else:
                    start_name = letter + str(i)
                    last = letters[ind + 1] + str(i)
                    G.add_edge(start_name, last, weight=weight_normal)

    Edges_file.create_edges_for_mountain_left(G, weight_mountain)
    Edges_file.create_edges_for_mountain_right(G, weight_mountain)


def create_path_to_draw(data):
    ways_to_draw = []
    for i in range(len(data)):
        if i != len(data) - 1:
            tupla = data[i], data[i + 1]
            ways_to_draw.append(tupla)

    return ways_to_draw


def draw_plot_and_write_legend(cost, path):
    plt.imshow(image, zorder=0, extent=[-1.0, 25.0, -1.0, 10.0])
    figure = plt.gcf()
    figure.set_size_inches(16, 12)
    cost = 'Cost -> ' + str(cost)
    path = 'Path -> ' + str(path)
    plt.text(12, 11.5, cost)
    plt.text(12, 12.0, path)
    plt.get_current_fig_manager().window.showMaximized()
    plt.show()


def draw_path(ways_to_draw, cost, path):
    edges_with_delete_ways_to_draw = G.edges - ways_to_draw

    nx.draw_networkx_nodes(G, pos_of_nodes)
    nx.draw_networkx_edges(G, pos_of_nodes, edgelist=edges_with_delete_ways_to_draw)
    nx.draw_networkx_edges(G, pos_of_nodes, edgelist=ways_to_draw, alpha=1, edge_color='b', style='dashed')
    nx.draw_networkx_labels(G, pos_of_nodes)

    draw_plot_and_write_legend(cost, path)


def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,


def create_path_to_visualization(letters):
    data, list_of_values_x, list_of_values_y = ([] for i in range(3))
    for i in letters:
        data.append(pos_of_nodes[i])

    for i in data:
        list_of_values_x.append(i[0])
        list_of_values_y.append(i[1])

    return np.array([np.array(list_of_values_x), np.array(list_of_values_y)])


def create_line_visualization(path_of_letters):
    path_to_visualization = create_path_to_visualization(path_of_letters)

    fig1 = plt.figure()

    l, = plt.plot([], [], 'r-')
    line_ani = animation.FuncAnimation(fig1, update_line, 250, fargs=(path_to_visualization, l),
                                       interval=50, blit=True, repeat=False)

    plt.imshow(image, zorder=0, extent=[-1.0, 25.0, -1.0, 10.0])
    plt.get_current_fig_manager().window.showMaximized()
    plt.show()


edges = Edges_normal.edges
start = 'a0'
fin = 'd8'
pop_num = 100
iterations = 100
select = .5
pc = .9
pm = .2
population, costs = make_population(start, fin, edges, pop_num)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']


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

best_s = final_pop[0]
best_path = best_s[1]
best_cost = best_s[0]

print("Best path:")
print(best_path)
print("cost: " + str(best_cost))

G = nx.Graph()
pos_of_nodes = create_graph_nodes_and_dict_nodes_with_pos()
create_graph_edges(G)
image = mpimg.imread('Background.png')
draw_path(create_path_to_draw(best_path), best_cost, best_path)
create_line_visualization(best_path)

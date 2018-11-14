import networkx as nx
import matplotlib.pyplot as plt
from scipy.misc import imread

import Edges_graph.Edges as Edges_file


class Graph:
    def __init__(self, sphere, weather):
        self.G = nx.Graph()
        self.letters = self.crate_list_of_letters()
        self.dict_nodes_with_pos = self.create_graph_nodes_and_dict_nodes_with_pos()
        self.path_accident = self.create_graph_edges(self.G, sphere, weather)
        self.pos = nx.get_node_attributes(self.G, 'pos')

#############################################################################

    def draw_way_dijktra(self, ways_to_draw):
        edges_with_delete_ways_to_draw = self.G.edges - ways_to_draw
        edges_with_delete_ways_to_draw = edges_with_delete_ways_to_draw - set(self.path_accident)

        nx.draw_networkx_nodes(self.G, self.pos)
        nx.draw_networkx_edges(self.G, self.pos, edgelist=edges_with_delete_ways_to_draw)
        nx.draw_networkx_edges(self.G, self.pos, edgelist=ways_to_draw, alpha=1, edge_color='b', style='dashed')
        nx.draw_networkx_edges(self.G, self.pos, edgelist=self.path_accident, alpha=1, edge_color='r', style='dashed')
        nx.draw_networkx_labels(self.G, self.pos)

        datafile = 'Wallpapers/Background.png'
        img = imread(datafile)
        plt.imshow(img, zorder=0, extent=[-1.0, 25.0, -1.0, 10.0])
        plt.savefig("Images/dijkstra.png")
        plt.show()

    def draw_way_a_star(self, ways_to_draw):
        edges_with_delete_ways_to_draw = self.G.edges - ways_to_draw
        edges_with_delete_ways_to_draw = edges_with_delete_ways_to_draw - set(self.path_accident)

        nx.draw_networkx_nodes(self.G, self.pos)
        nx.draw_networkx_edges(self.G, self.pos, edgelist=edges_with_delete_ways_to_draw)
        nx.draw_networkx_edges(self.G, self.pos, edgelist=ways_to_draw, alpha=1, edge_color='b', style='dashed')
        nx.draw_networkx_edges(self.G, self.pos, edgelist=self.path_accident, alpha=1, edge_color='r', style='dashed')
        nx.draw_networkx_labels(self.G, self.pos)

        datafile = 'Wallpapers/Background.png'
        img = imread(datafile)
        plt.imshow(img, zorder=0, extent=[-1.0, 25.0, -1.0, 10.0])
        plt.savefig("Images/a_star.png")
        plt.show()

    def crate_list_of_letters(self):
        data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']

        return data

    def create_graph_nodes_and_dict_nodes_with_pos(self):
        list_of_keys_dict = []
        list_of_values_dict = []
        os_x = 0
        for letter in self.letters:
            for number in range(0, 10):
                name_node = letter + str(number)
                values_of_pos = os_x, number

                self.G.add_node(name_node, pos=(os_x, number))

                list_of_keys_dict.append(name_node)
                list_of_values_dict.append(values_of_pos)
            os_x += 1

        data = dict(zip(list_of_keys_dict, list_of_values_dict))

        return data

    def create_graph_edges(self, G, sphere, weather):
        weight_normal = 0.5
        weight_mountain = 8.0

        Edges_file.create_edges_for_series_A(G, weight_normal)
        Edges_file.create_edges_for_series_Z(G, weight_normal)

        for ind, letter in enumerate(self.letters):
            if letter != 'A' and letter != 'Z':
                for i in range(0, 10):
                    if i != 9:
                        start_name = letter + str(i)
                        first = self.letters[ind - 1] + str(i + 1)
                        second = self.letters[ind] + str(i + 1)
                        third = self.letters[ind + 1] + str(i)
                        fourth = self.letters[ind + 1] + str(i + 1)

                        G.add_edge(start_name, first, weight=weight_normal)
                        G.add_edge(start_name, second, weight=weight_normal)
                        G.add_edge(start_name, third, weight=weight_normal)
                        G.add_edge(start_name, fourth, weight=weight_normal)
                    else:
                        start_name = letter + str(i)
                        last = self.letters[ind + 1] + str(i)
                        G.add_edge(start_name, last, weight=weight_normal)

        Edges_file.create_edges_for_mountain_left(G, weight_mountain)
        Edges_file.create_edges_for_mountain_right(G, weight_mountain)

        path_accident = []

        if weather != 0:
            if sphere == 0:
                Edges_file.create_edges_for_accident_B8_C7(G, weather)
                path_accident = Edges_file.create_path_for_accident_B8_C7()
            elif sphere == 1:
                Edges_file.create_edges_for_accident_D2_E1(G, weather)
                path_accident = Edges_file.create_path_for_accident_D2_E1()
            elif sphere == 2:
                Edges_file.create_edges_for_accident_O8_P7(G, weather)
                path_accident = Edges_file.create_path_for_accident_O8_P7()
            elif sphere == 3:
                Edges_file.create_edges_for_accident_X6_Y5(G, weather)
                path_accident = Edges_file.create_path_for_accident_X6_Y5()
            else:
                print('You are over size of random sphere')
        return path_accident

from collections import defaultdict
import random
from heapq import *

import Edges_dijkstra.Edges_normal as Edges_normal
import Edges_dijkstra.Edges_B8_C7 as Edges_B8_C7
import Edges_dijkstra.Edges_D2_E1 as Edges_D2_E1
import Edges_dijkstra.Edges_O8_P7 as Edges_O8_P7
import Edges_dijkstra.Edges_X6_Y5 as Edges_X6_Y5


class Algorithms:
    def __init__(self):
        self.weather = self.rand_weather()
        self.sphere = self.rand_sphere(self.weather)
        self.dict_nodes_with_pos = self.create_graph_nodes_and_dict_nodes_with_pos()
        self.start_input_point = self.read_start_point()
        self.end_input_point = self.read_end_point()
        self.edges_dijstra = self.create_edges_dijkstra(self.sphere, self.weather)
        self.path_to_unpack_dijkstra = self.dijkstra(self.edges_dijstra, self.start_input_point, self.end_input_point)
        self.length_of_way_dijkstra = self.path_to_unpack_dijkstra[0]
        self.path_dijkstra_to_print = self.create_good_path(self.path_to_unpack_dijkstra[1])
        self.path_to_draw_dijktra = self.create_path_to_draw(self.path_dijkstra_to_print)


#############################################################################
    def read_start_point(self):
        self.start_input_point = str(input('Please insert starting point of graph -> '))

        if_correct = True
        while if_correct:
            if len(self.start_input_point) == 2:
                self.start_input_point = self.start_input_point[0].upper() + self.start_input_point[1]
                if_correct = False
            else:
                print('Please insert only two letters')
                self.start_input_point = str(input('Please insert starting point of graph -> '))
                self.start_input_point = self.start_input_point.upper()

        return self.start_input_point

    def read_end_point(self):
        self.end_input_point = str(input('Please insert ending point of graph -> '))

        if_correct = True
        while if_correct:
            if len(self.end_input_point) == 2:
                self.end_input_point = self.end_input_point[0].upper() + self.end_input_point[1]
                if_correct = False
            else:
                print('Please insert only two letters')
                self.end_input_point = str(input('Please insert ending point of graph -> '))
                self.end_input_point = self.end_input_point.upper()

        return self.end_input_point

    def create_good_path(self, data):
        ways_dijktra_wrong_order = []
        ways_dijktra_good_order = []
        our_data = str(data)

        for index, value in enumerate(our_data):
            if value.isalpha():
                node = value + str(our_data[index+1])
                ways_dijktra_wrong_order.append(node)

        for i in reversed(ways_dijktra_wrong_order):
            ways_dijktra_good_order.append(i)

        return ways_dijktra_good_order

    def create_path_to_draw(self, data):
        ways_to_draw = []
        for i in range(len(data)):
            if i != len(data) - 1:
                tupla = data[i], data[i + 1]
                ways_to_draw.append(tupla)

        return ways_to_draw

    def dijkstra(self, edges, f, t):
        g = defaultdict(list)
        for l, r, c in edges:
            g[l].append((c, r))

        q, seen, mins = [(0, f, ())], set(), {f: 0}
        while q:
            (cost, v1, path) = heappop(q)
            if v1 not in seen:
                seen.add(v1)
                path = (v1, path)
                if v1 == t:
                    return (cost, path)

                for c, v2 in g.get(v1, ()):
                    if v2 in seen:
                        continue
                    prev = mins.get(v2, None)
                    next = cost + c
                    if prev is None or next < prev:
                        mins[v2] = next
                        heappush(q, (next, v2, path))

        return float("inf")

    def create_graph_nodes_and_dict_nodes_with_pos(self):
        data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']

        list_of_keys_dict = []
        list_of_values_dict = []
        os_x = 0
        for letter in data:
            for number in range(0, 10):
                name_node = letter + str(number)
                values_of_pos = os_x, number
                list_of_keys_dict.append(name_node)
                list_of_values_dict.append(values_of_pos)
            os_x += 1

        data = dict(zip(list_of_keys_dict, list_of_values_dict))

        return data

    def distance(self, a, b):
        (x1, y1) = self.dict_nodes_with_pos[a]
        (x2, y2) = self.dict_nodes_with_pos[b]

        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def rand_weather(self):
        weather = random.randrange(3)
        kind_of_weather = ['normal', 'strong rain', 'tornado']
        print(kind_of_weather[weather])
        return weather

    def rand_sphere(self, weather):
        if weather != 0:
            number = random.randrange(4)
            kind_of_sphere = ['B8-C7', 'D2-E1', 'O8-P7', 'X6-Y5']
            print(kind_of_sphere[number])
            return number

    def create_edges_dijkstra(self, sphere, weather):
        edges = Edges_normal.edges

        if weather == 1 or weather == 2:
            if sphere == 0:
                edges = Edges_B8_C7.create_edges(weather)
            elif sphere == 1:
                edges = Edges_D2_E1.create_edges(weather)
            elif sphere == 2:
                edges = Edges_O8_P7.create_edges(weather)
            elif sphere == 3:
                edges = Edges_X6_Y5.create_edges(weather)
            else:
                print('You are over size of random sphere')
        else:
            edges = Edges_normal.edges

        return edges

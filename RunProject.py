import networkx as nx

import Algorithms as Algorithms_file
import GraphVisualization as Graph_file

if __name__ == "__main__":
    algorithms_run = Algorithms_file.Algorithms()

    print('Cost of way dijktra - > ', algorithms_run.length_of_way_dijkstra)
    print('Path dijktra - > ', algorithms_run.path_dijkstra_to_print)
    print('Path to draw dijktra - > ', algorithms_run.path_to_draw_dijktra)

    graph_run = Graph_file.Graph(algorithms_run.sphere, algorithms_run.weather)
    graph_run.draw_way_dijktra(algorithms_run.path_to_draw_dijktra)

    path_with_number = nx.astar_path(graph_run.G_to_find_a_path,
                                     graph_run.dict_nodes_with_pos[algorithms_run.start_input_point],
                                     graph_run.dict_nodes_with_pos[algorithms_run.end_input_point],
                                     algorithms_run.distance)

    list_of_letters_of_path_a_star = algorithms_run.change_path_a_star_from_coordinates_to_letters\
        (path_with_number, graph_run.dict_nodes_with_pos.keys(), graph_run.dict_nodes_with_pos)
    path_to_draw_a_star = algorithms_run.create_path_to_draw_a_star(list_of_letters_of_path_a_star)

    print('Path a_star - > ', list_of_letters_of_path_a_star)
    print('Path to draw a_star - > ', path_to_draw_a_star)

    graph_run.draw_way_a_star(path_to_draw_a_star)



import networkx as nx

from Big_graph import Algorithms as Algorithms_file
from Big_graph import GraphVisualization as Graph_file

if __name__ == "__main__":
    algorithms_run = Algorithms_file.Algorithms()

    print('Path dijktra - > ', algorithms_run.path_dijkstra_to_print)
    print('Cost of way dijktra - > ', algorithms_run.length_of_way_dijkstra)

    graph_run = Graph_file.Graph(algorithms_run.sphere, algorithms_run.weather)
    graph_run.draw_way_dijktra(algorithms_run.path_to_draw_dijktra)

    a_star_path = nx.astar_path(graph_run.G, algorithms_run.start_input_point, algorithms_run.end_input_point,
                                heuristic=algorithms_run.distance, weight='weight')

    a_star_cost = nx.astar_path_length(graph_run.G, algorithms_run.start_input_point, algorithms_run.end_input_point,
                                       heuristic=algorithms_run.distance, weight='weight')

    path_to_draw_a_star = algorithms_run.create_path_to_draw(a_star_path)

    print('Path a_star - > ', a_star_path)
    print('Cost a_star - > ', a_star_cost)

    graph_run.draw_way_a_star(path_to_draw_a_star)

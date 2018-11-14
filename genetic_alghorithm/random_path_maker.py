import numpy as np
from genetic_alghorithm import helper_functions


def random_connection(start_node, target_node, graph_eges, p=0.001, d=1):
    '''
    Function creates random connection between dwo given nodes

    :param start_node: Starting node.
    :param target_node: Target node.
    :param graph_eges: All edges in the graph.
    :param p: Indicates the cost penalty for the nodes that are further from target than the current one.
    :param d: Multiplies probability of choosing node being the closest one to the target
    :return: List of nodes representing connection and its cost
    '''

    edges_array = np.array(graph_eges)
    current_node = start_node
    target_coordinates = helper_functions.change2coordinates(target_node)
    connection_cost = 0.
    path = [start_node]
    while current_node != target_node:
        current_edges = edges_array[edges_array[:, 0] == current_node]
        current_coordinates = helper_functions.change2coordinates(current_node)
        current_distance = np.linalg.norm(target_coordinates - current_coordinates)
        costs = []
        for edge in current_edges:
            _, neighbour, weight = tuple(edge)
            # if neighbour in path:
            #     costs.append(0.)
            #     continue
            neighbour_coordinates = helper_functions.change2coordinates(neighbour)
            neighbour_distance = np.linalg.norm(neighbour_coordinates - target_coordinates)
            if neighbour_distance < 1:
                costs.append(float('Inf'))
                continue
            distance_difference = 1 - neighbour_distance/current_distance
            edge_cost = abs(distance_difference)
            if distance_difference < 0:
                costs.append(p * edge_cost)
            else:
                costs.append(neighbour_distance * edge_cost)

        costs[costs.index(max(costs))] *= d
        summed_costs = sum(costs)
        neighbours = current_edges[:, 1]
        edges_probabilities = []
        for edge, edge_cost in zip(neighbours, costs):
            edges_probabilities.append(edge_cost / summed_costs)
        if not np.any(np.isnan(edges_probabilities)):
            edges_probabilities = np.array(edges_probabilities)
            next_node = np.random.choice(neighbours, 1, p=edges_probabilities)[0]
        else:
            next_node = neighbours[np.isnan(edges_probabilities)][0]

        path.append(next_node)
        current_node = next_node
        chosen_edge = current_edges[current_edges[:, 1] == current_node].T
        connection_cost += float(chosen_edge[2])

    return path, connection_cost

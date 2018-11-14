import unittest
from genetic_alghorithm import random_path_maker
from Edges_dijkstra import Edges_normal


class MakeRandomPath(unittest.TestCase):

    def test_node_connection(self):
        edges = Edges_normal.edges
        start = 'A0'
        target = 'Z9'
        path, cost = random_path_maker.random_connection(start, target, edges)
        self.assertGreater(cost, 0)
        self.assertIn(start, path)
        self.assertIn(target, path)


if __name__ == '__main__':
    unittest.main()

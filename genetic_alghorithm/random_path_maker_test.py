import unittest
from genetic_alghorithm import random_path_maker
from Edges_dijkstra import Edges_normal


class MakeRandomPath(unittest.TestCase):

    def test_node_connection(self):
        test_pairs = [
            ['a0', 'z9'],
            ['D3', 'A8'],
            ['x4', 'a1']
        ]
        edges = Edges_normal.edges
        for start, target in test_pairs:
            path, cost = random_path_maker.random_connection(start, target, edges)
            self.assertGreater(cost, 0)
            self.assertIn(start.capitalize(), path)
            self.assertIn(target.capitalize(), path)


if __name__ == '__main__':
    unittest.main()

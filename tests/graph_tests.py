import unittest
from csair.graph.graph import Graph


class TestRouteMap(unittest.TestCase):
    def setUp(self):
        self.map = Graph()

    def test_parse_data(self):
        self.assertTrue('data sources' in self.map.json_obj.keys())
        self.assertTrue('metros' in self.map.json_obj.keys())
        self.assertTrue('routes' in self.map.json_obj.keys())

    def test_parse_data_from_file(self):
        self.map.parse_data_from_file()

    def test_get_nodes(self):
        self.assertEqual(len(self.map.nodes), 48)

    def test_get_edges(self):
        edges = self.map.edges
        self.assertTrue('LIM' in edges['BOG'].keys())
        self.assertTrue('MEX' in edges['BOG'].keys())
        self.assertTrue('MIA' in edges['BOG'].keys())
        self.assertTrue('SAO' in edges['BOG'].keys())
        self.assertTrue('BUE' in edges['BOG'].keys())

        self.assertTrue('ATL' in edges['MIA'].keys())
        self.assertTrue('WAS' in edges['MIA'].keys())
        self.assertTrue('MEX' in edges['MIA'].keys())
        self.assertTrue('BOG' in edges['MIA'].keys())


if __name__ == '__main__':
    unittest.main()
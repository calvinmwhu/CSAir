import unittest
from csair.graph.graph import Graph


class TestRouteMap(unittest.TestCase):
    def setUp(self):
        self.map = Graph()

    def test_parse_data(self):
        self.map.parse_data(Graph.url_link)
        self.assertTrue('data sources' in self.map.json_obj.keys())
        self.assertTrue('metros' in self.map.json_obj.keys())
        self.assertTrue('routes' in self.map.json_obj.keys())

    def test_get_nodes(self):
        self.map.parse_data(Graph.url_link)
        self.map.get_nodes()
        print(self.map.nodes.values())
        self.assertTrue(len(self.map.nodes), 48)

    def test_get_edges(self):
        self.map.parse_data(Graph.url_link)
        self.map.get_edges()
        self.map.get_edges()
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
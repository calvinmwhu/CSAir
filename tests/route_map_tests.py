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

    def test_get_cites(self):
        self.map.parse_data(Graph.url_link)
        self.map.get_nodes()
        self.assertTrue(len(self.map.cities), 48)

    def test_get_routes(self):
        self.map.parse_data(Graph.url_link)
        self.map.get_nodes()
        self.map.get_routes()
        self.assertTrue(len(self.map.routes), 94)

    def test_construct_map(self):
        self.map.parse_data(Graph.url_link)
        self.map.get_nodes()
        self.map.get_routes()
        self.map.construct_map()
        ins = self.map.cities['WAS'].incidents
        self.assertTrue('YYZ' in ins.keys() and ins['YYZ'] == 575)
        self.assertTrue('NYC' in ins.keys() and ins['NYC'] == 334)


if __name__ == '__main__':
    unittest.main()
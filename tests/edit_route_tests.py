__author__ = 'calvinmwhu'

import unittest
from csair.edit_route.edit_route import EditRoute


class TestEditRoute(unittest.TestCase):
    def setUp(self):
        self.edit_route = EditRoute()

    def test_remove_city(self):
        self.edit_route.remove_city('LIM')
        cities = self.edit_route.map.nodes
        edges = self.edit_route.map.edges
        self.assertTrue('LIM' not in cities.keys())
        self.assertTrue('LIM' not in edges.keys())
        for city in edges.keys():
            # print(city , edges[city])
            self.assertTrue('LIM' not in edges[city].keys())

    def testRemoveRoute(self):
        self.edit_route = EditRoute()
        self.edit_route.remove_route('TYO','OSA')
        edges = self.edit_route.map.edges
        self.assertTrue('OSA' not in edges['TYO'].keys())

    def testAddCity(self):
        self.edit_route.add_city('CHA', 'Champaign', 'USA', 'North America',-5, {"N" : 11, "W" : 74}, 100000, 2)
        cities = self.edit_route.map.nodes
        self.assertTrue('CHA' in cities.keys())

    def testAddRoute(self):
        self.edit_route = EditRoute()
        self.edit_route.add_route('CHI','WAS',1000)
        edges = self.edit_route.map.edges
        self.assertTrue('WAS' in edges['CHI'].keys())
        self.assertTrue(edges['CHI']['WAS']==1000)

    def testEditCity(self):
        self.edit_route = EditRoute()
        self.edit_route.edit_city('KHI', 'Karachi', 'PK', 'Asia', 5, {"N" : 11, "E" : 74}, 16200000, 2)
        cities = self.edit_route.map.nodes
        self.assertTrue(cities['KHI'].coordinates == {"N" : 11, "E" : 74})


if __name__ == '__main__':
    unittest.main()

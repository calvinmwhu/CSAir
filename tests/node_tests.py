import unittest
import queue as Q
import heapq
from csair.graph.node import Node



class TestCity(unittest.TestCase):
    def setUp(self):
        self.obj = {'code': "LIM",
                    'name': "Lima",
                    'country': "PE",
                    'continent': "South America",
                    'timezone': -5,
                    'coordinates': {"S": 12,"W": 77},
                    'population': 9050000,
                    'region': 1}
        self.city1 = Node(**self.obj)
        self.city1.distance = 0
        self.city2 = Node(**self.obj)
        self.city2.distance = 2
        self.city3 = Node(**self.obj)
        self.city3.distance = 3
        self.city4 = Node(**self.obj)
        self.city4.distance = 4

    def test_init(self):
        self.assertEqual(self.obj['code'], self.city1.code)
        self.assertEqual(self.obj['name'], self.city1.name)
        self.assertEqual(self.obj['country'], self.city1.country)
        self.assertEqual(self.obj['continent'], self.city1.continent)
        self.assertEqual(self.obj['timezone'], self.city1.timezone)
        self.assertEqual(self.obj['coordinates'], self.city1.coordinates)
        self.assertEqual(self.obj['population'], self.city1.population)
        self.assertEqual(self.obj['region'], self.city1.region)


    def test_cmp(self):
        cities = [self.city1,self.city3,self.city4,self.city2]
        heapq.heapify(cities)
        cities[0].distance = 10
        heapq.heapify(cities)
        # heapq.heappop(cities)
        # heapq.heappop(cities)
        # heapq.heappop(cities)

        for i in cities:
            print(i.distance)


if __name__ == '__main__':
    unittest.main()
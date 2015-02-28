import unittest
from csair.graph.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.obj = {'code': "LIM",
                    'name': "Lima",
                    'country': "PE",
                    'continent': "South America",
                    'timezone': -5,
                    'coordinates': {"S": 12, "W": 77},
                    'population': 9050000,
                    'region': 1}
        self.city = City(self.obj)

    def test_init(self):
        self.assertEqual(self.obj['code'], self.city.code)
        self.assertEqual(self.obj['name'], self.city.name)
        self.assertEqual(self.obj['country'], self.city.country)
        self.assertEqual(self.obj['continent'], self.city.continent)
        self.assertEqual(self.obj['timezone'], self.city.timezone)
        self.assertEqual(self.obj['coordinates'], self.city.coordinates)
        self.assertEqual(self.obj['population'], self.city.population)
        self.assertEqual(self.obj['region'], self.city.region)

    def test_add_neighbour(self):
        self.city.add_neighbour('MEX',4231)
        self.assertEqual(self.city.incidents['MEX'],4231)

if __name__ == '__main__':
    unittest.main()
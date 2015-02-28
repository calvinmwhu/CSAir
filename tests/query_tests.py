import unittest
from csair.graph.route_map import RouteMap
from csair.query.query import Query


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.query = Query()

    def test_get_all_cities(self):
        cities = self.query.get_all_cities()
        self.assertTrue(len(cities) == 48)

    def test_get_longest_single_flight(self):
        flight = self.query.get_longest_single_flight()
        self.assertEqual(flight, ['SYD', 'LAX'])

    def test_get_shortest_single_flight(self):
        flight = self.query.get_shortest_single_flight()
        self.assertEqual(flight, ['WAS', 'NYC'])

    def test_get_biggest_city(self):
        city = self.query.get_biggest_city()
        self.assertEqual(city, {'Tokyo': 34000000})

    def test_get_smallest_city(self):
        city = self.query.get_smallest_city()
        self.assertEqual(city, {'Essen': 589900})

    def test_get_continents(self):
        continents = self.query.get_continents()
        self.assertTrue('Washington' in continents['North America'])
        self.assertTrue('Atlanta' in continents['North America'])
        self.assertTrue('Miami' in continents['North America'])
        self.assertTrue('Mexico City' in continents['North America'])


if __name__ == '__main__':
    unittest.main()
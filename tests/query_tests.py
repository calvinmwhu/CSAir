import unittest
from csair.graph.route_map import RouteMap
from csair.query.query  import Query


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.query = Query()

    def test_get_all_cities(self):
        cities = self.query.get_all_cities()
        self.assertTrue(len(cities)==48)


if __name__ == '__main__':
    unittest.main()
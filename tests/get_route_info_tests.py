from csair.get_route_info.get_route_info import GetRouteInfo
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.getRouteInfo = None

    def test_get_total_distance_true(self):
        route = ['SCL', 'LIM', 'BOG', 'BUE', 'SAO', 'LOS']
        total_dis = 2453 + 1879 + 4651 + 1680 + 6367
        self.getRouteInfo = GetRouteInfo(route)
        self.assertEqual(self.getRouteInfo.get_total_distance(), total_dis)

    def test_get_total_distance_false(self):
        route = ['SCL', 'LIM', 'LEX', 'BUE', 'SAO', 'LOS']
        self.getRouteInfo = GetRouteInfo(route)
        self.assertEqual(self.getRouteInfo.get_total_distance(), None)

    def test_get_total_cost(self):
        route = ['CHI','ATL','WAS','YYZ']
        self.getRouteInfo = GetRouteInfo(route)
        self.assertEqual(self.getRouteInfo.get_total_cost(),744)


    def test_get_total_time(self):
        pass


if __name__ == '__main__':
    unittest.main()

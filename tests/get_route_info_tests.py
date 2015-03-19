from csair.get_route_info.get_route_info import GetRouteInfo
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.getRouteInfo = None

    def test_get_total_distance_true(self):
        route = ['SCL', 'LIM', 'BOG', 'BUE', 'SAO', 'LOS']
        total_dis = 2453 + 1879 + 4651 + 1680 + 6367
        self.getRouteInfo = GetRouteInfo(route,'online_data.json')
        self.assertEqual(self.getRouteInfo.get_total_distance(), total_dis)

    def test_get_total_distance_false(self):
        route = ['SCL', 'LIM', 'LEX', 'BUE', 'SAO', 'LOS']
        self.getRouteInfo = GetRouteInfo(route,'online_data.json')
        self.assertEqual(self.getRouteInfo.get_total_distance(), None)

    def test_get_total_cost(self):
        route = ['CHI','ATL','WAS','YYZ']
        self.getRouteInfo = GetRouteInfo(route,'online_data.json')
        self.assertEqual(self.getRouteInfo.get_total_cost(),743.95)



    def test_get_total_route(self):
        dist1 = 1022
        dist2 = 391
        dist3 = 400
        self.getRouteInfo=GetRouteInfo([],'online_data.json')
        self.assertEqual(self.getRouteInfo.get_time_for_route(dist1),1.36)
        self.assertEqual(self.getRouteInfo.get_time_for_route(dist2),0.53)
        self.assertEqual(self.getRouteInfo.get_time_for_route(dist3),0.53)

    def test_get_total_time(self):
        route = ['ATL','WAS','NYC','LON']
        self.getRouteInfo = GetRouteInfo(route,'online_data.json')
        total_time = self.getRouteInfo.get_total_time()
        self.assertEqual(total_time, (13,46))

    def test_get_shortest_route(self):
        self.getRouteInfo = GetRouteInfo([],'online_data.json')
        route=self.getRouteInfo.get_shortest_path('PEK','CHI')
        self.assertEqual(route,['PEK', 'ICN', 'TYO', 'SFO', 'CHI'])

        self.getRouteInfo = GetRouteInfo([],'online_data.json')
        route=self.getRouteInfo.get_shortest_path('CHI', 'PEK')
        self.assertEqual(route,['CHI', 'SFO', 'TYO', 'ICN', 'PEK'])

        self.getRouteInfo = GetRouteInfo([],'online_data.json')
        route=self.getRouteInfo.get_shortest_path('CHI', 'WAS')
        self.assertEqual(route,['CHI', 'YYZ', 'WAS'])

        self.getRouteInfo = GetRouteInfo([],'online_data.json')
        route=self.getRouteInfo.get_shortest_path('CHI', 'WAS')
        self.assertEqual(route,['CHI', 'YYZ', 'WAS'])


if __name__ == '__main__':
    unittest.main()

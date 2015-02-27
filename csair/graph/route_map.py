from csair.graph.city import City
from csair.graph.route import Route
import json
import urllib.request


class RouteMap:
    url_link = 'https://wiki.cites.illinois.edu/wiki/download/attachments/502596813/map_data.json?version=1&modificationDate=1408551729000&api=v2'

    def __init__(self):
        self.cities = {}
        self.routes = []
        self.json_obj = {}

    def parse_data(self, url_str=None):
        req = urllib.request.Request(url_str)
        try:
            data_file = urllib.request.urlopen(req)
        except urllib.error.URLError as e:
            print(e)
        map_data = data_file.read().decode('utf-8')
        self.json_obj = json.loads(map_data)

    def get_cites(self):
        for item in self.json_obj['metros']:
            city = City(item)
            self.cities[city.code] = city

    def get_routes(self):
        self.routes = self.json_obj['routes']

    def construct_map(self):
        for route in self.routes:
            key1 = route['ports'][0]
            key2 = route['ports'][1]
            if key1 in self.cities.keys() and key2 in self.cities.keys():
                city1 = self.cities[key1]
                city2 = self.cities[key2]
                city1.add_neighbour(city2.code, route['distance'])


#
# map = RouteMap()
# map.parse_data(RouteMap.url_link)
# map.get_cites()
# map.get_routes()
# map.construct_map()
#
# for key in map.cities.keys():
#     print(map.cities[key])
#




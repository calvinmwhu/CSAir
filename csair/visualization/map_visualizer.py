from csair.graph.route_map import RouteMap
from csair.graph.city import City


class Visualizer:
    """
    Visualizer will construct a url base on CSAir's route network
    """
    map_url_prefix = 'http://www.gcmap.com/mapui?P='
    def __init__(self):
        self.map = RouteMap()
        self.map.parse_data(RouteMap.url_link)
        self.map.get_cites()
        self.map.get_routes()
        self.map.construct_map()


    def find_all_route(self):
        """
        Constructs a url string to request for. The url string contains all the possible routes of CSAir
        :return:
        """
        all_route = []
        for route in self.map.routes:
            all_route.append(route['ports'][0] + '-' + route['ports'][1])
        return Visualizer.map_url_prefix+','.join(all_route)

def main():
    v = Visualizer()
    print(v.find_all_route())

if __name__ == "__main__":
    main()

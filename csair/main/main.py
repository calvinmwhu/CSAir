from csair.graph.route_map import RouteMap
from csair.graph.city import City


def main():
    map = RouteMap()
    map.parse_data(RouteMap.url_link)
    map.get_cites()
    map.get_routes()
    map.construct_map()


if __name__ == "__main__":
    main()
from csair.graph.graph import Graph
from csair.graph.node import Node


def main():
    map = Graph()
    map.parse_data(Graph.url_link)
    map.get_nodes()
    map.get_edges()

    print(map.edges)
    # map.get_routes()
    # map.construct_map()


if __name__ == "__main__":
    main()
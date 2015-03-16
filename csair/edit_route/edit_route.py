from csair.graph.graph import Graph
from csair.graph.node import Node
from csair.graph.edge import Edge


class EditRoute:
    def __init__(self):
        self.map = Graph()
        self.map.parse_data(Graph.url_link)
        self.map.get_nodes()
        self.map.get_edges()


    def remove_city(self, city_code):
        if city_code not in self.map.nodes.keys():
            print(city_code + " does not exist")
            return
        else:
            del self.map.nodes[city_code]
            neighbors = self.map.edges[city_code]
            for neighbor in neighbors.keys():
                neighbor_neighbors = self.map.edges[neighbor]
                if city_code in neighbor_neighbors.keys():
                    del neighbor_neighbors[city_code]
            del self.map.edges[city_code]


    def remove_route(self, ori=None, des=None):
        edges = self.map.edges
        if ori not in edges.keys() or des not in edges[ori].keys():
            return
        del edges[ori][des]


    def add_city(self, code=None, name=None, country=None, continent=None, timezone=None, coordinates=None,
                 population=None, region=None):
        if code is None or name is None:
            return
        else:
            node_obj = {'code': code, 'name': name, 'country': country, 'continent': continent, 'timezone': timezone,
                        'coordinate': coordinates, 'population': population, 'region': region}
            node = Node(node_obj)
            self.map.nodes[node.code] = node


    def add_route(self, ori=None, des=None, dis=0):
        if ori is None or des is None:
            return
        elif ori not in self.map.edges.keys():
            return
        else:
            self.map.edges[ori][des] = dis


    def edit_city(self, code=None, name=None, country=None, continent=None, timezone=None, coordinates=None,
                  population=None, region=None):
        if code is None or name is None:
            return
        elif code not in self.map.nodes:
            self.add_city(code,name,country,continent,timezone,coordinates,population,region)
        else:
            node_obj = {'code': code, 'name': name, 'country': country, 'continent': continent, 'timezone': timezone,
                        'coordinate': coordinates, 'population': population, 'region': region}
            node = Node(node_obj)
            self.map.nodes[node.code] = node

    
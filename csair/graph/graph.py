from csair.graph.node import Node
from csair.graph.edge import Edge
import json
import urllib.request


class Graph:
    """
    this class is responsible for creating a RouteMap instance that gets data from the web and parse it into its own data structure, i.e. cities and routes
    """
    url_link = 'https://wiki.cites.illinois.edu/wiki/download/attachments/502596813/map_data.json?version=1&modificationDate=1408551729000&api=v2'

    def __init__(self):
        """
        constructor: initializes cities and json_obj to empty objects, initializes route to empty array
        :return:
        """
        self.cities = {}
        self.routes = []
        self.json_obj = {}
        self.nodes = {}
        self.edges = {}

    def parse_data(self, url_str=None):
        """
        Sends a HTTP GET request to get a html file and convert it to JSON format
        :param url_str: an yrl string to request the data
        :return:
        """
        req = urllib.request.Request(url_str)
        try:
            data_file = urllib.request.urlopen(req)
        except urllib.error.URLError as e:
            print(e)
        map_data = data_file.read().decode('utf-8')
        self.json_obj = json.loads(map_data)

    def get_nodes(self):
        """
        Constructs city objects from the json_obj
        :return:
        """
        for item in self.json_obj['metros']:
            node = Node(item)
            self.cities[node.code] = node

    def get_edges(self):
        """
        construct all the edges from the json object
        :return:
        """
        for item in self.json_obj['routes']:
            edge = Edge(item)
            key1 = edge.ports[0]
            key2 = edge.ports[1]
            if key1 not in self.edges:
                self.edges[key1] = {}
            if key2 not in self.edges:
                self.edges[key2] = {}
            self.edges[key1][key2] = edge.distance
            self.edges[key2][key1] = edge.distance

    def get_routes(self):
        """
        Constructs routes array from the JSON object
        :return:
        """
        self.routes = self.json_obj['routes']

    def construct_map(self):
        """
        Populates each city's neighbours from the routes object
        :return:
        """
        for route in self.routes:
            key1 = route['ports'][0]
            key2 = route['ports'][1]
            if key1 in self.cities.keys() and key2 in self.cities.keys():
                city1 = self.cities[key1]
                city2 = self.cities[key2]
                city1.add_neighbour(city2.code, route['distance'])





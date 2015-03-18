from csair.graph.node import Node
from csair.graph.edge import Edge
import json
import urllib.request
import os
from os.path import dirname
from os.path import join


class Graph:
    """
    this class is responsible for creating a RouteMap instance that gets data from the web and parse it into its own data structure, i.e. cities and routes
    """
    url_link = 'https://wiki.cites.illinois.edu/wiki/download/attachments/502596813/map_data.json?version=1&modificationDate=1408551729000&api=v2'

    def __init__(self, file_name='online_data.json'):
        """
        constructor: initializes cities and json_obj to empty objects, initializes route to empty array
        :return:
        """
        self.json_obj = {}
        self.nodes = {}
        self.edges = {}
        self.routes = []
        self.source = []
        # self.parse_data()
        self.parse_data_from_file()
        self.get_nodes()
        self.get_edges()
        self.get_source()


    def parse_data(self, url_str=url_link):
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



    def parse_data_from_file(self):
        file_path=dirname(dirname(dirname(__file__)))+'/route_network/online_data.json'
        file_obj = open(file_path)
        self.json_obj = json.load(file_obj)


    def get_nodes(self):
        """
        Constructs city objects from the json_obj
        :return:
        """
        for item in self.json_obj['metros']:
            node = Node(**item)
            self.nodes[node.code] = node

    def get_edges(self):
        """
        construct all the edges from the json object
        :return:
        """
        for item in self.json_obj['routes']:
            edge = Edge(item)
            self.routes.append(edge)
            key1 = edge.ports[0]
            key2 = edge.ports[1]
            if key1 not in self.edges:
                self.edges[key1] = {}
            if key2 not in self.edges:
                self.edges[key2] = {}
            self.edges[key1][key2] = edge.distance
            self.edges[key2][key1] = edge.distance

    def get_source(self):
        self.source = self.json_obj['data sources']




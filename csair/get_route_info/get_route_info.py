from csair.graph.graph import Graph
import math


class GetRouteInfo:
    def __init__(self, route=[]):
        self.map = Graph()
        self.route = route

    def get_total_distance(self):
        edges = self.map.edges
        total_dis = 0
        for i in range(len(self.route) - 1):
            ori = self.route[i]
            des = self.route[i + 1]
            if ori not in edges.keys() or des not in edges[ori].keys():
                return None
            total_dis += edges[ori][des]
        return total_dis


    def get_total_cost(self):
        begin = 0.35
        edges = self.map.edges
        cost = 0.0;
        for i in range(len(self.route) - 1):
            ori = self.route[i]
            des = self.route[i + 1]
            if ori not in edges.keys() or des not in edges[ori].keys():
                return None
            cond = begin-i*0.05
            price = cond if cond>0 else 0
            cost += price*edges[ori][des]
        return math.ceil(cost)

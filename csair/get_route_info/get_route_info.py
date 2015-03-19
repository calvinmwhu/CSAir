from csair.graph.graph import Graph
import math
import heapq
import sys


class GetRouteInfo:
    """
    this class gives user an interface to query a map about the distance, time, cost of a route and the shortest route between two cities
    """
    def __init__(self, route=[], file_name=None):
        if file_name:
            self.map = Graph(file_name)
        else:
            self.map = Graph()
        self.route = [city.upper() for city in route]
        self.slope = 750 / (400 / 750)


    def get_total_distance(self):
        """
        calculates the total distance along a route path
        """
        edges = self.map.edges
        total_dis = 0
        for i in range(len(self.route) - 1):
            ori = self.route[i]
            des = self.route[i + 1]
            if ori not in edges or des not in edges[ori]:
                print("route does not exist")
                return None
            total_dis += edges[ori][des]
        print("total distance for the route ", self.route, "is ", total_dis, "kilometers")
        return total_dis


    def get_total_cost(self):
        """
        calculates the total cost along a route path
        """
        begin = 0.35
        edges = self.map.edges
        cost = 0.0;
        for i in range(len(self.route) - 1):
            ori = self.route[i]
            des = self.route[i + 1]
            if ori not in edges or des not in edges[ori]:
                print("route does not exist")
                return None
            cond = begin - i * 0.05
            price = cond if cond > 0 else 0
            cost += price * edges[ori][des]
        cost = round(cost, 2)
        print("It costs ", cost, "dollars to flight through ", self.route)
        return cost


    def get_time_for_route(self, dist=0):
        if dist <= 400:
            return round(math.sqrt(dist / self.slope), 2)
        else:
            return round((dist - 400) / 750 + math.sqrt(400 / self.slope), 2)

    def get_total_time(self):
        if len(self.route) < 2:
            return (0, 0)
        first_layover = 2
        total_time = 0
        edges = self.map.edges
        for i in range(len(self.route) - 1):
            ori = self.route[i]
            des = self.route[i + 1]
            if ori not in edges or des not in edges[ori]:
                print("route does not exist")
                return None
            flight_time = self.get_time_for_route(edges[ori][des])
            total_time += flight_time + first_layover - (1 / 6) * (len(edges[ori]) - 1)
        total_time = round(total_time, 2)
        hours = int(total_time)
        minutes = int(60 * (total_time - hours))
        print("It takes ", hours, "hours and ", minutes, "minutes to flight through the route", self.route)
        return (hours, minutes)


    def get_shortest_path(self, ori=None, des=None):
        """
        this function first runs Dijkstra's algorithm to determine the shortest length between the ori and every other nodes.
        then it start with the destination node and find the shortest route backward
        """
        nodes = self.map.nodes
        edges = self.map.edges
        ori = ori.upper()
        des = des.upper()
        solved = set()
        if ori not in nodes or des not in nodes:
            print("cities invalid")
            return []
        cities = [item[1] for item in nodes.items()]
        # print(cities)
        nodes[ori].distance = 0
        heapq.heapify(cities)
        # print(cities)

        # run Dijkstra's algorithm
        for i in range(len(nodes)):
            nearest = heapq.heappop(cities)
            nearest_code = nearest.code
            solved.add(nearest_code)
            # print(nearest_code)
            if nearest_code == des:
                break
            for neighbor in edges[nearest_code]:
                if neighbor not in solved:
                    edge = edges[nearest_code][neighbor]
                    if nodes[neighbor].distance > nearest.distance + edge:
                        nodes[neighbor].distance = nearest.distance + edge
                        nodes[neighbor].parent = nearest_code
            heapq.heapify(cities)

        # retrieve the route:
        curr = des
        route = []
        while curr:
            route.insert(0, curr)
            curr = nodes[curr].parent
        if ori not in route:
            print("cannot get from ", ori, "to", des)
            return []
        print("shortest route from",ori,"to",des,"is",route)
        return route


def main():
    queries = {'1','2','3','4','5'}
    print(
        """
        1.  Get total distance of a route
        2.  Get total cost of a route
        3.  Get total time of a route
        4.  Get shortest route from [origin] to [destination]
        """
    )

    while True:
        question = str(input("\nPlease select the question number: \n"))
        if question not in queries:
            print("cannot answer your question")
            continue
        if question=='1' or question=='2' or question=='3':
            route = str(input("\n   Please enter the route:\n")).split()
            getRouteInfo = GetRouteInfo(route)
            if question=='1':
                getRouteInfo.get_total_distance()
            elif question=='2':
                getRouteInfo.get_total_cost()
            else:
                getRouteInfo.get_total_time()
        elif question=='4':
            getRouteInfo = GetRouteInfo()
            twoCities = str(input("\n   Please enter origin and destination:\n")).split()
            if len(twoCities)!=2:
                print("invalid input")
                continue
            route=getRouteInfo.get_shortest_path(twoCities[0],twoCities[1])
            if len(route)==0:
                continue
            getRouteInfo.route=route
            getRouteInfo.get_total_distance()
            getRouteInfo.get_total_cost()
            getRouteInfo.get_total_time()

if __name__ == "__main__":
    main()

from csair.graph.graph import Graph
from csair.graph.node import Node
import sys


class Query:
    """
    Query class is responsible for returning data based on user's query
    """

    def __init__(self, otherGraph=None):
        if otherGraph:
            self.map = otherGraph
        else:
            self.map = Graph()

    def get_all_cities(self):
        """
        :return: all the cities in CSAir
        """
        city_list = []
        for city in self.map.nodes.values():
            city_list.append(city.name)
        return city_list

    def get_city_info(self, code):
        """
        :param code: a city's code
        :return: all the info of the city with code code, none if city with the code does not exist
        """
        if code not in self.map.nodes.keys():
            return None
        return self.map.nodes[code]

    def get_longest_single_flight(self):
        """
        :return: A flight object that covers the longest distance
        """
        longest_dist = 0
        longest_flight = []
        for route in self.map.routes:
            if route.distance > longest_dist:
                longest_dist = route.distance
                longest_flight = route.ports
        return (longest_flight, longest_dist)

    def get_shortest_single_flight(self):
        """
        :return: A flight object that covers the shortest distance
        """
        shortest_dist = sys.maxsize
        shortest_flight = []
        for route in self.map.routes:
            if route.distance < shortest_dist:
                shortest_dist = route.distance
                shortest_flight = route.ports
        return (shortest_flight, shortest_dist)

    def get_average_distance(self):
        """
        :return: average of all the routes in terms of the distance
        """
        ave = 0
        for route in self.map.routes:
            ave = ave + route.distance
        ave = ave / len(self.map.routes)
        return ave

    def get_biggest_city(self):
        """
        :return: City with highest population
        """
        name = ""
        biggest = 0
        for city in self.map.nodes.values():
            if city.population > biggest:
                biggest = city.population
                name = city.name
        return {name: biggest}


    def get_smallest_city(self):
        """
        :return: City with the lowest population
        """
        name = ""
        smallest = sys.maxsize
        for city in self.map.nodes.values():
            if city.population < smallest:
                smallest = city.population
                name = city.name
        return {name: smallest}

    def get_cities_average_size(self):
        """
        :return: Average population of all the cities
        """
        ave = 0
        for city in self.map.nodes.values():
            ave = ave + city.population
        ave = ave / len(self.map.nodes)
        return ave

    def get_continents(self):
        """
        :return: A dictionary that group cities based on the continent they belong to
        """
        continents = {}
        for city in self.map.nodes.values():
            if city.continent not in continents:
                continents[city.continent] = [city.name]
            else:
                continents[city.continent].append(city.name)
        return continents

    def get_hub_cities(self):
        """
        :return: City with the highest number of edges
        """
        hub = Node()
        neighbour_edges = {}
        connections = 0
        for city_code in self.map.edges.keys():
            neighbours = self.map.edges[city_code]
            num_incident_cities = len(neighbours)
            if num_incident_cities > connections:
                connections = num_incident_cities
                hub = self.map.nodes[city_code]
                neighbour_edges = neighbours
        return {hub.name: neighbour_edges.keys()}


def main():
    query = Query()
    gac = query.get_all_cities
    gci = query.get_city_info
    glsf = query.get_longest_single_flight
    gssf = query.get_shortest_single_flight
    gad = query.get_average_distance
    gbc = query.get_biggest_city
    gsc = query.get_smallest_city
    gcas = query.get_cities_average_size
    gc = query.get_continents
    ghc = query.get_hub_cities

    queries = {
        '1': gac,
        '2': gci,
        '3a': glsf,
        '3b': gssf,
        '3c': gad,
        '3d': gbc,
        '3e': gsc,
        '3f': gcas,
        '3g': gc,
        '3h': ghc
    }

    print(
        """
        FAQ:
        1.  List of all the cities that CSAir flies to
        2.  Information about a specific city in the CSAir route network
        3a. Longest single flight in the network
        3b. Shortest single flight in the network
        3c. Average distance of all the flights in the network
        3d. Biggest city (by population) served by CSAir
        3e. Smallest city (by population) served by CSAir
        3f. Average size (by population) of all the cities served by CSAir
        3g. List of the continents served by CSAir and which cities are in them
        3h. CSAir's hub cities – the cities that have the most direct connections

        """
    )

    while True:
        question = str(input("\nPlease select the question number: \n"))
        if question not in queries.keys():
            print("cannot answer your question")
        elif question == '2':
            code = str(input("Please enter the city's code: \n"))
            code = code.upper()
            city = queries[question](code)
            if city == None:
                print("Cannot find city with code ", code)
            else:
                print(city)
        else:
            print(queries[question]())

#
# print(query.get_all_cities())
# print(query.get_city_info('BGW'))
# print(query.get_longest_single_flight())
# print(query.get_shortest_single_flight())
# print(query.get_average_distance())
# print(query.get_biggest_city())
# print(query.get_smallest_city())
# print(query.get_cities_average_size())
# print(query.get_continents())
# print(query.get_hub_cities())

if __name__ == "__main__":
    main()
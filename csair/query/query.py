from csair.graph.route_map import RouteMap
from csair.graph.city import City
import sys


class Query:
    def __init__(self):
        self.map = RouteMap()
        self.map.parse_data(RouteMap.url_link)
        self.map.get_cites()
        self.map.get_routes()
        self.map.construct_map()

    def get_all_cities(self):
        city_list = []
        for city in self.map.cities.values():
            city_list.append(city.name)
        return city_list

    def get_city_info(self, code):
        if code not in self.map.cities.keys():
            return None
        return self.map.cities[code]

    def get_longest_single_flight(self):
        longest_dist = 0
        longest_flight = []
        for route in self.map.routes:
            if route['distance'] > longest_dist:
                longest_dist = route['distance']
                longest_flight = route['ports']
        return longest_flight

    def get_shortest_single_flight(self):
        shortest_dist = sys.maxsize
        shortest_flight = []
        for route in self.map.routes:
            if route['distance'] < shortest_dist:
                shortest_dist = route['distance']
                shortest_flight = route['ports']
        return shortest_flight

    def get_average_distance(self):
        ave = 0
        for route in self.map.routes:
            ave = ave + route['distance']
        ave = ave / len(self.map.routes)
        return ave

    def get_biggest_city(self):
        name = ""
        biggest = 0
        for city in self.map.cities.values():
            if city.population > biggest:
                biggest = city.population
                name = city.name
        return {name: biggest}


    def get_smallest_city(self):
        name = ""
        smallest = sys.maxsize
        for city in self.map.cities.values():
            if city.population < smallest:
                smallest = city.population
                name = city.name
        return {name: smallest}

    def get_cities_average_size(self):
        ave = 0
        for city in self.map.cities.values():
            ave = ave + city.population
        ave = ave / len(self.map.cities)
        return ave

    def get_continents(self):
        continents = {}
        for city in self.map.cities.values():
            if city.continent not in continents:
                continents[city.continent] = [city.name]
            else:
                continents[city.continent].append(city.name)
        return continents

    def get_hub_cities(self):
        hub = City()
        connections = 0
        for city in self.map.cities.values():
            num_incident_cities = len(city.incidents)
            if len(city.incidents) > connections:
                connections = num_incident_cities
                hub = city
        return {hub.name: hub.incidents}


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
        if question not in queries:
            print("cannot answer your question")
        elif question == '2':
            code = str(input("Please enter the city's code: \n"))
            code = code.upper()
            city = queries[question](code)
            if  city == None:
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
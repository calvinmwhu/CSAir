class Node:
    """
    A city defines a node in the graph.
    """
    def __init__(self, obj={}):
        """
        Initializes all the fields with a dictionary parameter passed in
        :param obj: A JSON object that represents a city
        :return:
        """
        try:
            self.code = obj['code']
            self.name = obj['name']
            self.country = obj['country']
            self.continent = obj['continent']
            self.timezone = obj['timezone']
            self.coordinates = obj['coordinates']
            self.population = obj['population']
            self.region = obj['region']
            self.incidents = {}
        except KeyError as e:
            print(e)


    def add_neighbour(self, city, dist):
        """
        Add a neighbour to the incidents dictionary; it represents an edge that comes out of this node
        :param city: A neighbour's code
        :param dist: Distance between this node and the neighbour
        :return:
        """
        self.incidents[city] = dist

    def __str__(self):
        """
        convert the node to string for easy printing
        :return: A string representation of an instance of City
        """
        city_dict = {}
        city_dict['code'] = self.code
        city_dict['name'] = self.name
        city_dict['country'] = self.country
        city_dict['continent'] = self.continent
        city_dict['timezone'] = self.timezone
        city_dict['coordinates'] = self.coordinates
        city_dict['population'] = self.population
        city_dict['region'] = self.region
        city_dict['accessible cities'] = str(self.incidents)
        return str(city_dict)



import sys

class Node():
    city_para = ['code', 'name', 'country', 'continent', 'timezone', 'coordinates', 'population', 'region']
    """
    A city defines a node in the graph.
    """

    def __init__(self, code=None, name=None, country=None, continent=None, timezone=None, coordinates=None,
                 population=None, region=None):
        """
        Initializes all the fields with data passed in
        :param obj: A JSON object that represents a city
        :return:
        """
        self.code = code
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinates = coordinates
        self.population = population
        self.region = region
        self.distance = sys.maxsize
        self.parent = None

    def __eq__(self, other):
        # print("called")
        if isinstance(other, Node):
            return self.distance==other.distance
        return NotImplemented

    def __lt__(self, other):
        # print("called")
        if isinstance(other, Node):
            return self.distance<other.distance
        return NotImplemented

    def __gt__(self, other):
        # print("called")
        if isinstance(other, Node):
            return self.distance>other.distance
        return NotImplemented
    #
    # def __ge__(self, other):
    #     print("called")
    #     if isinstance(other, Node):
    #         return self.distance>=other.distance
    #     return NotImplemented
    #
    # def __le__(self, other):
    #     print("called")
    #     if isinstance(other, Node):
    #         return self.distance<=other.distance
    #     return NotImplemented


    def __repr__(self):
        return str(self)

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
        return str(city_dict)



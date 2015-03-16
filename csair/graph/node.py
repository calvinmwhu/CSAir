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
        except KeyError as e:
            print(e)


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



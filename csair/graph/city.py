class City:
    def __init__(self, obj={}):
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
        self.incidents[city] = dist

    def __str__(self):
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



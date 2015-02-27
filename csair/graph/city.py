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
        return self.code+": "+ str(self.incidents)


# print(id(City))

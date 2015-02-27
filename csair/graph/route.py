from csair.graph import city

class Route:
    def __init__(self, obj):
        self.ports = obj['ports']
        self.distance = obj['distance']


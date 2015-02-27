from csair.graph import city

class Route:
    """
    Defines an edge in a graph; contains the origin, destination nodes and the distance between them
    """
    def __init__(self, obj):
        self.ports = obj['ports']
        self.distance = obj['distance']


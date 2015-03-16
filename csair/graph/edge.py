import copy

class Edge:
    """
    Defines an edge in a graph; contains the origin, destination nodes and the distance between them
    """
    def __init__(self, obj):
        self.ports = copy.deepcopy(obj['ports'])
        self.distance = obj['distance']


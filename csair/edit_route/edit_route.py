from csair.graph.graph import Graph
from csair.graph.node import Node
from csair.graph.edge import Edge
import json
from os.path import dirname


class EditRoute:
    def __init__(self, otherGraph=None):
        if otherGraph:
            self.map = otherGraph
        else:
            self.map = Graph()

    def remove_city(self, code=None):
        if code not in self.map.nodes.keys():
            print(code + " does not exist")
            return
        else:
            del self.map.nodes[code]
            neighbors = self.map.edges[code]
            for neighbor in neighbors.keys():
                neighbor_neighbors = self.map.edges[neighbor]
                if code in neighbor_neighbors.keys():
                    del neighbor_neighbors[code]
            del self.map.edges[code]


    def remove_route(self, origin=None, destination=None):
        edges = self.map.edges
        if origin not in edges.keys() or destination not in edges[origin].keys():
            print(origin + " or " + destination + " does not exist !")
            return
        del edges[origin][destination]


    def add_city(self, code=None, name=None, country=None, continent=None, timezone=None, coordinates=None,
                 population=None, region=None):
        if code is None or name is None:
            return
        else:
            node_obj = {'code': code, 'name': name, 'country': country, 'continent': continent, 'timezone': timezone,
                        'coordinates': coordinates, 'population': population, 'region': region}
            node = Node(**node_obj)
            self.map.nodes[node.code] = node


    def add_route(self, origin=None, destination=None, distance=None):
        if origin is None or destination is None:
            return
        elif origin not in self.map.edges.keys():
            return
        else:
            self.map.edges[origin][destination] = distance

    def edit_city(self, code=None, name=None, country=None, continent=None, timezone=None, coordinates=None,
                  population=None, region=None):
        if code is None or name is None:
            return
        elif code not in self.map.nodes:
            self.add_city(code, name, country, continent, timezone, coordinates, population, region)
        else:
            node_obj = {'code': code, 'name': name, 'country': country, 'continent': continent, 'timezone': timezone,
                        'coordinates': coordinates, 'population': population, 'region': region}
            node = Node(**node_obj)
            self.map.nodes[node.code] = node

    def write_to_disk(self):
        file_name = dirname(dirname(dirname(__file__))) + '/route_network/saved_data.json'
        file_obj = open(file_name, 'w')

        new_json = {}
        new_json['data sources'] = self.map.source
        new_json['metros'] = []
        new_json['routes'] = []
        nodes = self.map.nodes
        edges = self.map.edges
        for node in nodes.values():
            new_json['metros'].append(node.__dict__)
        for ori in edges.keys():
            for des in edges[ori].keys():
                edge = {}
                edge['ports'] = [ori, des]
                edge['distance'] = edges[ori][des]
                new_json['routes'].append(edge)
        json.dump(new_json, file_obj)
        file_obj.close()


def main():
    edit_route = EditRoute()
    rc = edit_route.remove_city
    rr = edit_route.remove_route
    ac = edit_route.add_city
    ar = edit_route.add_route
    ec = edit_route.edit_city
    se = edit_route.write_to_disk

    inputs = {
        '1': rc,
        '2': rr,
        '3': ac,
        '4': ar,
        '5': ec,
        '6': se
    }

    prompt = """
        1.  Remove a city (City code)
        2.  Remove a route [origin, destination]
        3.  Add a city (code, name, country, continent, timezone, coordinates, population, region)
        4.  Add a route [origin, destination, distance]
        5.  Edit a city (code, name, country, continent, timezone, coordinates, population, region)
        6.  Exit/save to disk
        """
    print(prompt)

    while True:
        info_dict = {}
        num = str(input("\nPlease select the input: \n"))
        if num not in inputs.keys():
            print("cannot answer your question")
            continue
        elif num == '2' or num == '4':
            for para in Edge.edge_para:
                if para == 'distance' and num == '2':
                    continue
                info_dict[para] = None
                str_value = str(input("enter route's %s: " % para)).upper()
                if len(str_value) > 0:
                    if para == 'distance':
                        try:
                            info_dict[para] = int(str_value)
                        except ValueError as err:
                            print("exception occurs, value: ", err)
                    else:
                        info_dict[para] = str_value
            print(info_dict)
        elif num == '3' or num == '5':
            for para in Node.city_para:
                info_dict[para] = None
                if para == 'coordinates':
                    NS = str(input("enter coordinate [N/S value]: ")).upper().split()
                    WE = str(input("enter coordinate [W/E value]: ")).upper().split()
                    if (len(NS) == 2 and len(WE) == 2):
                        coord = {NS[0]: int(NS[1]), WE[0]: int(WE[1])}
                        info_dict[para] = coord
                elif para == 'population' or para == 'region' or para == 'timezone':
                    try:
                        int_value = int(str(input("enter city's %s: " % para)))
                    except ValueError as err:
                        print("exception occurs, value: ", err)
                    else:
                        info_dict[para] = int_value
                else:
                    str_value = str(input("enter city's %s: " % para))
                    if para == 'code':
                        str_value = str_value.upper()
                    if len(str_value) > 0:
                        info_dict[para] = str_value
            print(info_dict)
        elif num == '1':
            info_dict['code'] = None;
            input_val = str(input("enter city's code: ")).upper()
            if len(input_val) > 0:
                info_dict['code'] = input_val
        inputs[num](**info_dict)
        if num == '6':
            break


if __name__ == "__main__":
    main()




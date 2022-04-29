
import json
import random

def main():

    layer_data = {}

    f1 = open('circuit_data/layer_download.json')
    f2 = open('circuit_data/pathways_anatomy_factsheets_simplified.json')
    f3 = open('circuit_data/pathways_physiology_factsheets_simplified.json')

    layer_data = json.load(f1)
    ana_data = json.load(f2)
    phys_data = json.load(f3)

    f1.close()
    f2.close()
    f3.close()

    layer_counts = {}
    nodes = {}
    cell_connections = {}
    connections_prob = {}

    layers = [key for key, value in layer_data.items()]

    for layer in layers:
        layer_counts[layer] = layer_data[layer]["No. of neurons per morphological types"]


    print(layer_counts)

    for key, value in layer_counts.items():
        for k, v in value.items():
            cell_connections[k] = [key for key, value in ana_data.items() if k in key]
            for key, value in ana_data.items():
                if k in key:
                    connections_prob[key] = value["connection_probability"]

    print(layer_counts)      
    print(cell_connections)
    print(connections_prob)

    # for k1, v1 in l1_counts:
    #     count = v1
    #     while count !=0:
    #         nodes.append(Node("L1", k1))
    
    # for k1, v1 in l1_counts:
    #     count = v1
    #     for k2, v2 in cell_connections:
    #         if k1 in k2:
    #             while count != 0:
    #                 prob  = connections_prob[k2]
    #                 r = random.randrange(0, 100)
    #                 if r < prob:
    #                     # n = Node("L1")
    #                     count-=1

 

if __name__ == "__main__":
    main()


class Node:
    def __init__(self, layer, type):
        self.layer = layer
        self.type = type
        self.connections = []
        self.weight = 0

    def addConnection(self, node):
        self.connections.append(node)

        
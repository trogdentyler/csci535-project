
import json
import re

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


    layers = [key for key, value in layer_data.items()]

    for layer in layers:
        type_count = layer_data[layer]["No. of neurons per morphological types"]
        print(layer + " " +str(type_count))
        

    l1_connections = [key for key, value in ana_data.items() if 'l1' in key.lower()]
    l1_neurons = [value for key, value in ana_data.items() if 'l1' in key.lower()]

    # print(type_count)
 

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
        
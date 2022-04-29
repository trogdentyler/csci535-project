import json
from random import random



class Node:
    def __init__(self, layer, type):
        self.layer = layer
        self.type = type
        self.connections = []
        self.weight = 0

    def addConnection(self, node):
        self.connections.append(node)

    def __repr__(self):
        return super(Node, self).__repr__()[:-1] + f" {self.layer} {self.type} {self.connections}>"


with open("circuit_data/layer_download.json") as f:
    layer_data = json.load(f)

with open("circuit_data/pathways_anatomy_factsheets_simplified.json") as f:
    anatomy_data = json.load(f)

layer_counts = dict()
cell_connections = dict()
connections_prob = dict()

layers = [key for key, value in layer_data.items()]

for layer in layers:
    layer_counts[layer] = layer_data[layer]["No. of neurons per morphological types"]


for key, value in layer_counts.items():
    for k, v in value.items():
        cell_connections[k] = [key for key, value in anatomy_data.items() if k in key]
        for key, value in anatomy_data.items():
            if k in key:
                connections_prob[key] = value["connection_probability"]


neurons = dict()
for key in layer_data:
    for mtype in layer_data[key]["No. of neurons per morphological types"]:
        neurons[mtype] = [Node(layer=key, type=mtype)
                               for i in range(layer_data[key]["No. of neurons per morphological types"][mtype])]

num_of_connections = 0
for source_key in neurons:
    for sink_key in neurons:
        try:
            prob = connections_prob[source_key + ":" + sink_key]
            for source_neuron in neurons[source_key]:
                for sink_neuron in neurons[sink_key]:
                    if random()*100 < prob:
                        source_neuron.connections.append(sink_neuron)
                        num_of_connections += 1
        except KeyError:
            print(f"KEY ERROR {source_key}:{sink_key}")
            pass

print("DONE")



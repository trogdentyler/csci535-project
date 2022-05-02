import json
from random import random, seed
"""
This produces a a random direct graph with vertices being neurons vertices and
the edges between any two neurons being determined by the probabilities given in
the pathways_anatomy_factsheets_simplified.json
"""

old = False  # variable that determines if old method is used.

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

scale_factor = 5

layers = [key for key, value in layer_data.items()]

for layer in layers:
    layer_counts[layer] = dict()
    for key in layer_data[layer]["No. of neurons per morphological types"]:
        layer_counts[layer][key] = max(1,layer_data[layer]["No. of neurons per morphological types"][key]//scale_factor)

for key, value in layer_counts.items():
    for k, v in value.items():
        cell_connections[k] = [key for key, value in anatomy_data.items() if k in key]
        for key, value in anatomy_data.items():
            if k in key:
                connections_prob[key] = value["connection_probability"]

if old:
    neurons = dict()
    for key in layer_data:
        for m_type in layer_data[key]["No. of neurons per morphological types"]:
            neurons[m_type] = [Node(layer=key, type=m_type)
                               for i in range(layer_data[key]["No. of neurons per morphological types"][m_type])]

    num_of_connections = 0
    for source_key in neurons:
        for sink_key in neurons:
            try:
                prob = connections_prob[source_key + ":" + sink_key]
                for source_neuron in neurons[source_key]:
                    for sink_neuron in neurons[sink_key]:
                        if random() * 100 < prob:
                            source_neuron.connections.append(sink_neuron)
                            num_of_connections += 1
            except KeyError:
                print(f"KEY ERROR {source_key}:{sink_key}")
                pass

    print("DONE")
    print(f"NUMBER OF CONNECTIONS: {num_of_connections}")

neuron_types = ['L1_DAC', 'L1_DLAC', 'L1_HAC', 'L1_NGC-DA', 'L1_NGC-SA', 'L1_SLAC', 'L23_BP', 'L23_BTC', 'L23_ChC',
                'L23_DBC', 'L23_LBC', 'L23_MC', 'L23_NBC', 'L23_NGC', 'L23_PC', 'L23_SBC', 'L4_BP', 'L4_BTC', 'L4_ChC',
                'L4_DBC', 'L4_LBC', 'L4_MC', 'L4_NBC', 'L4_NGC', 'L4_PC', 'L4_SBC', 'L4_SP', 'L4_SS', 'L5_BP', 'L5_BTC',
                'L5_ChC', 'L5_DBC', 'L5_LBC', 'L5_MC', 'L5_NBC', 'L5_NGC', 'L5_SBC', 'L5_STPC', 'L5_TTPC1', 'L5_TTPC2',
                'L5_UTPC', 'L6_BP', 'L6_BPC', 'L6_BTC', 'L6_ChC', 'L6_DBC', 'L6_IPC', 'L6_LBC', 'L6_MC', 'L6_NBC',
                'L6_NGC', 'L6_SBC', 'L6_TPC_L1', 'L6_TPC_L4', 'L6_UTPC']

num_of_connections = 0
cMat = dict()
Layers = ["L1", "L4", "L5", "L23", "L6"]
seed(12)
for m_type1 in neuron_types:
    layer1 = m_type1.split("_")[0]
    if layer1 not in Layers:
        continue
    else:
        cMat[m_type1] = dict()
        for m_type2 in neuron_types:
            layer2 = m_type2.split("_")[0]
            cMat[m_type1][m_type2] = [[0 for i in range(layer_counts[layer2][m_type2])]
                                      for j in range(layer_counts[layer1][m_type1])]
            if layer2 not in Layers:
                continue
            try:
                prob = connections_prob[m_type1 + ":" + m_type2]
                for i in range(layer_counts[layer1][m_type1]):
                    for j in range(layer_counts[layer2][m_type2]):
                        if random() * 100 < prob:
                            cMat[m_type1][m_type2][i][j] = 1
                            num_of_connections += 1
            except KeyError:
                continue
print(f"NUMBER OF RANDOM CONNECTIONS: {num_of_connections}")

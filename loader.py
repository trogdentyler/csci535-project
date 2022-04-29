import json
import graph
from random import random

probs = graph.connections_prob

with open("circuit_data/layer_download.json") as f:
    layer_data = json.load(f)

neurons = dict()
for key in layer_data:
    for mtype in layer_data[key]["No. of neurons per morphological types"]:
        neurons[mtype] = [graph.Node(layer=key, type=mtype)
                               for i in range(layer_data[key]["No. of neurons per morphological types"][mtype])]

num_of_connections = 0
for source_key in neurons:
    for sink_key in neurons:
        try:
            prob = probs[source_key + ":" + sink_key]
            for source_neuron in neurons[source_key]:
                for sink_neuron in neurons[sink_key]:
                    if random()*100 < prob:
                        source_neuron.connections.append(sink_neuron)
                        num_of_connections += 1
        except KeyError:
            print(f"KEY ERROR {source_key}:{sink_key}")
            pass

print("DONE")
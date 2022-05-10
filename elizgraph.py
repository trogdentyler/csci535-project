import json
import pickle

import h5py
import numpy as np

h5 = h5py.File("circuit_data/connectome_data/cons_locs_pathways_mc6_Column/cons_locs_pathways_mc6_Column.h5")

output = dict()


def get_tuple(me_type: str, place: int):
    value = me_type.split("_")
    return value[0], "_".join(value[1:]), str(place)


"""
Iterates through each type pair, then each pair of neuron of neurons between the two types.
"""
pos = 0  # progress counter for sanity; goes to 3025
for m_type1 in h5["connectivity"]:
    print(m_type1)
    for i in range(h5["connectivity"][m_type1]["L4_MC"]['cMat'].shape[0]):  # gets number of m_type1
        output[get_tuple(m_type1, i)] = []  # initializes adjacency list for tuple
    for m_type2 in h5["connectivity"][m_type1]:
        pos += 1  # on new type pair, increase by 1
        print(f'\t{m_type2}\t{pos}')
        lookup = np.array(h5["connectivity"][m_type1][m_type2]['cMat'])  # loads adjacency matrix into numpy for speed.
        for m1_neuron in range(h5["connectivity"][m_type1][m_type2]['cMat'].shape[0]):
            for m2_neuron in range(h5["connectivity"][m_type1][m_type2]['cMat'].shape[1]):
                if lookup[m1_neuron][m2_neuron] == 1:  # checks if connected
                    output[get_tuple(m_type1, m1_neuron)].append(get_tuple(m_type2, m2_neuron))


with open("elizgraph.pkl", 'wb') as f:
    pickle.dump(output, f)

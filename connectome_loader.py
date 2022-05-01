import h5py
import numpy as np
import bisect

h5 = h5py.File("circuit_data/connectome_data/cons_locs_pathways_mc6_Column/cons_locs_pathways_mc6_Column.h5")
count = False

if count:
    number_of_connection = 0
    number_of_neurons = 0
    for m_type1 in h5["connectivity"]:
        for m_type2 in h5["connectivity"][m_type1]:
            number_of_connection += np.sum(h5["connectivity"][m_type1][m_type2]['cMat'])
            number_of_neurons += h5["connectivity"][m_type1][m_type2]['cMat'].shape[0]

    print(f"Number of connection: {number_of_connection}")
    print(f"Number of Neurons: {number_of_neurons}")


class SimplexHasse:
    def __init__(self, me_types: list, h5_data):
        self.h5 = h5_data

        # make a key dictionary to quickly look up order
        self.type_order = [key for key in me_types]  # TODO remove this as list is now passed in directly
        self.type_order.sort()
        self.type_to_int = {self.type_order[i]: i for i in range(len(self.type_order))}
        self.number_of_type = {me_type: self.h5["connectivity"][self.type_order[0]][me_type]['cMat'].shape[0]
                               for me_type in self.type_order}
        self.type_base = {me_type: sum([self.number_of_type[self.type_order[i]]
                                        for i in range(self.type_to_int[me_type])])
                          for me_type in self.type_order}
        self.base_to_type = {self.type_base[me_type]: me_type for me_type in self.type_order}
        self.base_list = sorted(list(self.base_to_type))

        self.number_of_neurons = sum(self.number_of_type[me_type] for me_type in self.number_of_type)

    def get_type(self, neuron: int):
        """ Finds the type of the neuron using pythons built in binary search module
        """
        index = bisect.bisect_right(self.base_list, neuron)
        return self.base_to_type[self.base_list[index-1]]

    def neuron_to_int(self, neuron_type: str, pos: int):
        """ short method, just gives each neuron a unique number.
            Most logic is located above and done globally to prevent recalculation.

            neuron_type: layer of the neuron plus morphological type abbreviation
            pos: position of neuron in the connectivity array
        """
        return self.type_base[neuron_type] + pos

    def are_connected(self, neuron1: int, neuron2: int):
        """ Determine if two neuron (record as ints) have a connection in the loaded connectome column.
            Looks for a connection starting a neuron1 and heading to neuron2
        """
        neuron1_type = self.get_type(neuron1)
        neuron1_pos = neuron1 - self.type_base[neuron1_type]
        neuron2_type = self.get_type(neuron2)
        neuron2_pos = neuron2 - self.type_base[neuron2_type]
        return self.h5["connectivity"][neuron1_type][neuron2_type]["cMat"][neuron1_pos][neuron2_pos] == 1

    def make_hasse(self, full=True):
        """
        Makes the hasse diagram.
        Full=False does not complete simplifies

        SUPER SLOW! Runs in O(n^6) (O(E^3) really but hey) at least.
        Still better then O(n!) however.
        """
        dim_list = dict()  # list of simplices by dimension
        ver = dict()  # zero faces of a simplex, zero simplices are set [] though
        tar = dict()  # targets? paper is unclear
        src = dict()  # sources? paper is again unclear

        # line 1 from Riemann Supplemental paper
        dim_list[0] = [(i,) for i in range(self.number_of_neurons)]
        for neuron in dim_list[0]:
            ver[neuron] = []
            tar[neuron] = []
            src[neuron] = []
        dim_list[1] = []
        for neuron1 in range(self.number_of_neurons):
            for neuron2 in range(self.number_of_neurons):
                if neuron1 == neuron2:
                    continue
                if self.are_connected(neuron1, neuron2):
                    dim_list[1].append((neuron1, neuron2))  # linter is confused ignore this
                    ver[neuron1, neuron2] = (neuron1, neuron2)
                    tar[neuron1, neuron2] = []  # probably have real values I just don't know yet
                    src[neuron1, neuron2] = []
        if not full:
            return dim_list  # returns only nodes and vertices

        u_set = dict()  # triangles where u_list[e] does not point toward target.
        # lines 2 to 5 of the paper
        for e in dim_list[1]:
            u_set[e] = set()
            for e1 in dim_list[1]:
                for e2 in dim_list[1]:
                    if e1[0] == e[0] and e2[0] == e[1] and e1[1] == e2[1]:
                        u_set[e].add(e2[1])

        dim = 2
        # python do-while equivalent
        while True:
            next_level_nodes = []
            for e in dim_list[dim-1]:
                for u in u_set[e]:
                    # line 12
                    t_u = list(e)
                    t_u.append(u)
                    t_u = tuple(t_u)

                    ver[t_u] = t_u
                    u_set[t_u] = u_set[e].copy()
                    tar[t_u] = [e]
                    src[e].append(t_u)
                    for bd in tar[e]:
                        for cbd in src[bd]:
                            if cbd and cbd[-1] == u:
                                tar[t_u].append(cbd)
                                src[cbd].append(t_u)
                                u_set[t_u].intersection(u_set[cbd])
                    next_level_nodes.append(t_u)
            dim_list[dim] = next_level_nodes.copy()
            dim += 1
            if len(next_level_nodes) == 0:
                break
            return dim_list


if __name__ == "__main__":
    test = SimplexHasse(["L4_MC"], h5)
    non_full_test = test.make_hasse(full=False)
    full_test = test.make_hasse(full=True)
    print("DONE")


class HasseBuilder:
    def __init__(self, number_of_neurons, c_mat):
        self.number_of_neurons = number_of_neurons
        self.c_mat = c_mat

    def are_connected(self, neuron1, neuron2):
        return self.c_mat[neuron1][neuron2] == 1

    def make_hasse(self, full=False):
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
        dim_list[0] = [i for i in range(self.number_of_neurons)]
        for neuron in dim_list[0]:
            ver[neuron] = []
            tar[neuron] = []
            src[neuron] = []
        dim_list[1] = []
        for neuron1 in range(self.number_of_neurons):
            # print(neuron1)
            for neuron2 in range(self.number_of_neurons):
                if neuron1 == neuron2:
                    continue
                if self.are_connected(neuron1, neuron2):
                    dim_list[1].append((neuron1, neuron2))  # linter is confused ignore this
                    ver[neuron1, neuron2] = (neuron1, neuron2)
                    tar[neuron1, neuron2] = [neuron1, neuron2]
                    src[neuron1].append((neuron1, neuron2))
                    src[neuron2].append((neuron1, neuron2))
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
            for e in dim_list[dim - 1]:
                for u in u_set[e]:
                    # line 12
                    t_u = list(e)
                    t_u.append(u)
                    t_u = tuple(t_u)

                    ver[t_u] = t_u
                    u_set[t_u] = u_set[e].copy()
                    tar[t_u] = [e]
                    try:
                        src[e].append(t_u)
                    except KeyError:
                        src[e] = [t_u]
                    for bd in tar[e]:
                        for cbd in src[bd]:
                            if cbd and cbd[-1] == u:
                                try:
                                    tar[t_u].append(cbd)
                                except KeyError:
                                    tar[t_u] = [cbd]
                                try:
                                    src[cbd].append(t_u)
                                except KeyError:
                                    src[cbd] = [t_u]
                                u_set[t_u] = u_set[t_u].intersection(u_set[cbd])
                    next_level_nodes.append(t_u)
            dim_list[dim] = next_level_nodes.copy()
            dim += 1
            if len(next_level_nodes) == 0:
                break
        return dim_list

    def get_flag_file(self, output_file, full=True):
        with open(output_file, "w") as f:
            dim_list = self.make_hasse(full=full)
            f.write("dim 0\n")
            dim0 = " ".join(["0" for i in dim_list[0]]) + "\n"
            f.write(dim0)
            for i in range(1,len(dim_list)):
                f.write(f"dim {i}\n")
                for simplex in dim_list[i]:
                    str_simplex = [str(i) for i in simplex]
                    f.write(" ".join(str_simplex) + "\n")


if __name__ == "__main__":
    test = (5, [[0,1,1,1,1],[0,0,1,1,1],[0,0,0,1,1],[0,0,0,0,1],[0,0,0,0,0]])
    out = HasseBuilder(*test)
    out.get_flag_file("hasse.flag")


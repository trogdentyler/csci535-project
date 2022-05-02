import matplotlib.pyplot as plt
import networkx as nx

for i in range(6):
    n = 5000   
    # m = 0.004 * n * (n-1)  
    p = 0.04
    G = nx.erdos_renyi_graph(n, p)

    print("here")

    with open(f"er_graphs/er_{i}.flag", "w") as f:
        f.write("dim 0\n")
        dim0 = " ".join(["0" for i in range(int(n))]) + "\n"
        f.write(dim0)
        f.write("dim 1\n")
        for e in G.edges:
            f.write(f"{e[0]} {e[1]}\n")



import matplotlib.pyplot as plt
import networkx as nx

n = 10000  
m = 0.004 * n * (n-1)  
G = nx.gnm_random_graph(n, m)

print("here")

with open("er.flag", "w") as f:
    f.write("dim 0\n")
    dim0 = " ".join(["0" for i in range(int(m))]) + "\n"
    f.write(dim0)
    f.write("dim 1\n")
    for e in G.edges:
        f.write(f"{e[0]} {e[1]}\n")



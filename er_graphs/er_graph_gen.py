import matplotlib.pyplot as plt
from matplotlib import pylab
import networkx as nx
from pyvis.network import Network
import pygraphviz

for i in range(1):
    n = 500   
    # m = 0.004 * n * (n-1)  
    p = 0.04
    G = nx.erdos_renyi_graph(n, p)


    # A = nx.nx_agraph.to_agraph(G)
    # A.layout()
    # A.draw('networkx_graph.png')


    net = Network(notebook=True, height='750px', width='100%', bgcolor='#222222', font_color='white')
    net.from_nx(G)
    net.toggle_physics(False)
    net.show_buttons()
    net.show("pyvis_visualization.html")

    print("here")

    # with open(f"er_graphs/er_{i}.flag", "w") as f:
    #     f.write("dim 0\n")
    #     dim0 = " ".join(["0" for i in range(int(n))]) + "\n"
    #     f.write(dim0)
    #     f.write("dim 1\n")
    #     for e in G.edges:
    #         f.write(f"{e[0]} {e[1]}\n")



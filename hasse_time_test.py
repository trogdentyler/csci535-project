import json
from time import process_time_ns
import hasse_diagram
import random

random.seed(110)
def make_random_graph(nodes: int, edge_prob: float):
    c_mat = []
    for i in range(nodes):
        c_mat.append([])
        for j in range(nodes):
            if i == j:
                c_mat[i].append(0)
            elif random.random() < edge_prob:
                c_mat[i].append(1)
            else:
                c_mat[i].append(0)
    return c_mat

print(make_random_graph(5,.5))

step = 10
tests = []
for i in range(1, 11):
    tests.append([(i*step, make_random_graph(i*step, .08)) for j in range(16)])

print("done generating")

output = {i*step: [] for i in range(1, 11)}
for test in tests:
    for inst in test:
        print(inst)
        times = []
        hasse = hasse_diagram.HasseBuilder(inst[0], inst[1])
        start_time = process_time_ns()
        for i in range(5):
            hasse.make_hasse(full=True)
        output[inst[0]].append(process_time_ns()-start_time)

print(output)
print(json.dump(output))

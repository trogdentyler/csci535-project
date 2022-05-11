import json
import numpy as np
import matplotlib.pyplot as plt

with open('complete.json', 'r') as f:
    df= json.load(f)

with open('er_data.json', 'r') as f:
    df_er= json.load(f)

for data_type in df:
    for sample in df[data_type]:
        for layers in df[data_type][sample]:
            df[data_type][sample][layers]= {i: df[data_type][sample][layers][i] for i in range(len(df[data_type][sample][layers]))}

for data_type in df_er:
    for sample in df_er[data_type]:
        df_er[data_type][sample]= {i: df_er[data_type][sample][i] for i in range(len(df_er[data_type][sample]))}

random_samples= ["random12", "random15", "random17", "random23", "random24", "random25"]
mc_samples= [f"mc{i}" for i in range(1,7)]

betti_numbers_data= {
    "random": {i: 0 for i in range(0,8)},
    "mc": {i: 0 for i in range(0,8)},
    "er": {i: 0 for i in range(0,8)}
}

cell_counts_data= {
    "random": {i: 0 for i in range(0,8)},
    "mc": {i: 0 for i in range(0,8)},
    "er": {i: 0 for i in range(0,8)}
}

for sample in df["betti_numbers"]:
    for layer in df["betti_numbers"][sample]:
        if sample in random_samples:
            for i in range(len(betti_numbers_data["random"])):
                betti_numbers_data["random"][i] += df['betti_numbers'][sample][layers].get(i, 0)/ len(betti_numbers_data["random"])
        elif sample in mc_samples:
            for i in range(len(betti_numbers_data["mc"])):
                betti_numbers_data["mc"][i] += df["betti_numbers"][sample][layers].get(i, 0)/ len(betti_numbers_data["mc"])
        else:
            continue

for sample in df["cell_counts"]:
    for layer in df["cell_counts"][sample]:
        if sample in random_samples:
            for i in range(len(cell_counts_data["random"])):
                cell_counts_data["random"][i] += df['cell_counts'][sample][layers].get(i, 0)/ len(cell_counts_data["random"])
        elif sample in mc_samples:
            for i in range(len(cell_counts_data["mc"])):
                cell_counts_data["mc"][i] += df["cell_counts"][sample][layers].get(i, 0)/ len(cell_counts_data["mc"])
        else:
            continue

for sample in df_er:
    for i in df_er[sample]["betti_numbers"]:
        betti_numbers_data["er"][i] += df_er[sample]["betti_numbers"].get(i, 0)/ len(betti_numbers_data["er"])

for sample in df_er:
    for i in df_er[sample]["cell_counts"]:
        cell_counts_data["er"][i] += df_er[sample]["cell_counts"].get(i, 0)/ len(cell_counts_data["er"])

X= np.arange(0, 8)
Y_betti_ran= np.zeros(len(X))
Y_betti_mc= np.zeros(len(X))
Y_betti_er= np.zeros(len(X))
Y_cc_ran= np.zeros(len(X))
Y_cc_mc= np.zeros(len(X))
Y_cc_er= np.zeros(len(X))

for i in range(len(X)):
    Y_betti_ran[i]= betti_numbers_data["random"][i]
    Y_betti_mc[i]= betti_numbers_data["mc"][i]
    Y_betti_er[i]= betti_numbers_data["er"][i]
    Y_cc_ran[i]= cell_counts_data["random"][i]
    Y_cc_mc[i]= cell_counts_data["mc"][i]
    Y_cc_er[i]= cell_counts_data["er"][i]

plt.yscale("log")
plt.plot(X, Y_betti_ran, label='Naive Random')
plt.plot(X, Y_betti_mc, label='MC')
plt.plot(X, Y_betti_er, label='E-R')
plt.title('Average Betti Numbers of Approximate Neocortex')
plt.xlabel('Betti Number')
plt.ylabel('Averaged Betti Number Count')
plt.legend()
plt.show()

plt.yscale("log")
plt.plot(X, Y_cc_ran, label='Naive Random')
plt.plot(X, Y_cc_mc, label='MC')
plt.plot(X, Y_cc_er, label='E-R')
plt.title('Average Number of Simplices of Approximate Neocortex')
plt.xlabel('Dimension of Simplex')
plt.ylabel('Averaged Number of Simplices')
plt.legend()
plt.show()
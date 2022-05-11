import os
import json

cmd = "./flagser/flagser"
out_opt = "--out"
app_opt = "--approximate"

output_path_base = "./data_raw/random_data_raw/"


groups = ["L1", "L4", "L5", "L6", "L23"]
combos = []
for i in range(len(groups)-1):
    for j in range(i+1,len(groups)):
        combos.append(f"{groups[i]}_{groups[j]}")
subgrps = groups + combos

jobs = []

for smpl in ["random23", "random24", "random25"]:
    for grp in subgrps:
        jobs.append(f"./{smpl}/{smpl}_{grp}.flag")

jobs.sort(key =(lambda x: os.path.getsize(x)))

old_samples = ["random12", "random15", "random17", "mc1", "mc2", "mc3", "mc4", "mc5", "mc6"]
samples = ["random23", "random24", "random25"]
compl_samples = samples + old_samples

with open("complete_idata.json", 'r') as ff:
    x = json.load(ff)
    cell_counts = x["cell_counts"]
    betti_numbers = x["betti_numbers"]
    betti_error = x["betti_error"]

for sample in samples:
    cell_counts[sample] = dict()
    betti_numbers[sample] = dict()
    betti_error[sample] = dict()
    for grp in subgrps:
        cell_counts[sample][grp] = []
        betti_numbers[sample][grp] = []
        betti_error[sample][grp] = []

num = 0
for path in jobs:
    num += 1
    file = path.split('/')[-1]
    a = file.split('.')
    b = a[0].split('_')
    groups = "_".join(b[1:])
    smple = b[0]
    print(file,smple,groups)
    input_path = output_path_base + f"{groups}/{smple}_{groups}.homology"
    print(f"\nON JOB {num}/{len(jobs)}")
    try:
        with open(input_path, 'r') as f:
            lines = f.readlines()
            try:
                if len(lines) == 12: # no approximation was run.
                    cell_counts[smple][groups] = [int(value) for value in lines[1].split()]
                    betti_numbers[smple][groups] = [int(value) for value in lines[-1].split()]
                    betti_error[smple][groups] = [0 for value in lines[-1].split()]
                else:
                    cell_counts[smple][groups] = [int(value) for value in lines[1].split()]
                    betti_numbers[smple][groups] = [int(value) for value in lines[-1].split()]
                    betti_error[smple][groups] = [int(value) for value in lines[-3].split()]
                print(cell_counts[smple][groups])
                print(betti_numbers[smple][groups])
                print(betti_error[smple][groups])
            except IndexError:
                pass
    except FileNotFoundError:
        pass

print("\n\n")
print(cell_counts)
print("\n\n")
print(betti_numbers)
print("\n\n")
print(betti_error)

print(subgrps)
for item in subgrps:
    print(f"\n{item}:")
    for sample in compl_samples:
        b_numbers = '\t'.join([f"{str(betti_numbers[sample][item][i])}\t{betti_error[sample][item][i]}"
                               for i in range(len(betti_numbers[sample][item]))])
        print(f"\t{sample}\t\t" + b_numbers)

print("CELL COUNT: " + 50*"==")

for item in subgrps:
    print(f"\n{item}:")
    for sample in compl_samples:
        c_numbers = '\t'.join([f"{str(cell_counts[sample][item][i])}"
                               for i in range(len(cell_counts[sample][item]))])
        print(f"\t{sample}\t\t" + c_numbers)

x = dict()
x["cell_counts"] = cell_counts
x["betti_numbers"] = betti_numbers
x["betti_error"] = betti_error
with open("complete.json", "w") as f:
    json.dump(x, f)

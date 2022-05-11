import os

cmd = "../flagser/flagser"
out_opt = "--out"
app_opt = "--approximate"
approx = "50000"

output_path_base = "./data_raw/random_data_raw/"



groups = ["L1", "L4", "L5", "L6", "L23"]
combos = []
for i in range(len(groups)-1):
    for j in range(i+1,len(groups)):
        combos.append(f"{groups[i]}_{groups[j]}")
subgrps = groups + combos

for grp in subgrps:
    output_path_base = "./data_raw/random_data_raw/"
    os.system(f"mkdir {output_path_base}{grp}")

"""
Running Small jobs here
"""
jobs = []

for smpl in ["random23", "random24", "random25"]:
    for grp in subgrps:
        jobs.append(f"./{smpl}/{smpl}_{grp}.flag")
        print(f"{jobs[-1]} size: {os.path.getsize(jobs[-1])}")

print(jobs)
jobs.sort(key =(lambda x: os.path.getsize(x)))


print(f"TOTAL JOBS: {len(jobs)}")
num = 0
for path in jobs:
    num += 1
    file = path.split('/')[-1]
    a = file.split('.')
    b = a[0].split('_')
    groups = "_".join(b[1:])
    smpl = b[0]
    print(file,smpl,groups)
    output_path = output_path_base + f"{groups}/{smpl}_{groups}.homology"
    input_path = path
    print(f"\nON JOB {num}/{len(jobs)}")
    print(f"\nJOB SIZE: {os.path.getsize(path)}")
    if os.path.getsize(path) > 2530500:
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
        print()
        os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))
    else:
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,])}")
        os.system(" ".join([cmd, out_opt, output_path, input_path]))





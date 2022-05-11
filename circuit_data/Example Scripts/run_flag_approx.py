import os

cmd = "./flagser/flagser"
out_opt = "--out"
app_opt = "--approximate"

mc_input_path_base = "./mc_flag_files/"
random12_input_path_base = "./random12/"
random15_input_path_base = "./random15/"
random17_input_path_base = "./random17/"


mc_output_path_base = "./data_raw/mc_data_raw/"
random_output_path_base = "./data_raw/random_data_raw/"

mc_small_jobs = ['mc1_L1.flag', 'mc2_L1.flag', 'mc3_L1.flag', 'mc4_L1.flag', 'mc5_L1.flag', 'mc6_L1.flag']

mc_medium_jobs = ['mc1_L1_L23.flag', 'mc1_L5.flag', 'mc2_L4.flag', 'mc3_L23.flag', 'mc4_L1_L5.flag', 'mc5_L1_L4.flag',
               'mc6_L1_L23.flag', 'mc6_L5.flag', 'mc1_L1_L4.flag', 'mc2_L1_L23.flag', 'mc2_L5.flag', 'mc3_L4.flag',
               'mc4_L23.flag', 'mc5_L1_L5.flag', 'mc6_L1_L4.flag', 'mc1_L1_L5.flag', 'mc2_L1_L4.flag',
               'mc3_L1_L23.flag', 'mc3_L5.flag', 'mc4_L4.flag', 'mc5_L23.flag', 'mc6_L1_L5.flag', 'mc1_L23.flag',
               'mc2_L1_L5.flag', 'mc3_L1_L4.flag', 'mc4_L1_L23.flag', 'mc4_L5.flag', 'mc5_L4.flag', 'mc6_L23.flag',
               'mc1_L4.flag', 'mc2_L23.flag', 'mc3_L1_L5.flag', 'mc4_L1_L4.flag', 'mc5_L1_L23.flag', 'mc5_L5.flag',
               'mc6_L4.flag']

mc_large_jobs = ['mc1_L1_L6.flag', 'mc1_L6.flag', 'mc2_L5_L23.flag', 'mc3_L4_L5.flag', 'mc4_L4_L23.flag', 'mc5_L1_L6.flag',
              'mc5_L6.flag', 'mc6_L5_L23.flag', 'mc1_L4_L23.flag', 'mc2_L1_L6.flag', 'mc2_L6.flag', 'mc3_L5_L23.flag',
              'mc4_L4_L5.flag', 'mc5_L4_L23.flag', 'mc6_L1_L6.flag', 'mc6_L6.flag', 'mc1_L4_L5.flag', 'mc2_L4_L23.flag',
              'mc3_L1_L6.flag', 'mc3_L6.flag', 'mc4_L5_L23.flag', 'mc5_L4_L5.flag', 'mc6_L4_L23.flag',
              'mc1_L5_L23.flag', 'mc2_L4_L5.flag', 'mc3_L4_L23.flag', 'mc4_L1_L6.flag', 'mc4_L6.flag',
              'mc5_L5_L23.flag', 'mc6_L4_L5.flag']

random12_small = ['randon12_L1.flag', 'randon12_L1_L4.flag', 'randon12_L23.flag', 'randon12_L4_L23.flag',
                  'randon12_L5.flag', 'randon12_L1_L23.flag', 'randon12_L1_L5.flag', 'randon12_L4.flag',
                  'randon12_L4_L5.flag', 'randon12_L5_L23.flag']

random12_medium = ['randon12_L1_L6.flag', 'randon12_L4_L6.flag', 'randon12_L5_L6.flag', 'randon12_L6.flag',
                  'randon12_L6_L23.flag']

random15_small = ['randon15_L1.flag', 'randon15_L1_L4.flag', 'randon15_L23.flag', 'randon15_L4_L23.flag',
                  'randon15_L5.flag', 'randon15_L1_L23.flag', 'randon15_L1_L5.flag', 'randon15_L4.flag',
                  'randon15_L4_L5.flag', 'randon15_L5_L23.flag']

random15_medium = ['randon15_L1_L6.flag', 'randon15_L4_L6.flag', 'randon15_L5_L6.flag', 'randon15_L6.flag',
                   'randon15_L6_L23.flag']

random17_small = ['randon17_L1.flag', 'randon17_L1_L4.flag', 'randon17_L23.flag', 'randon17_L4_L23.flag',
                  'randon17_L5.flag', 'randon17_L1_L23.flag', 'randon17_L1_L5.flag', 'randon17_L4.flag',
                  'randon17_L4_L5.flag', 'randon17_L5_L23.flag']


random17_medium = ['randon17_L1_L6.flag', 'randon17_L4_L6.flag', 'randon17_L5_L6.flag', 'randon17_L6.flag',
                   'randon17_L6_L23.flag']

remaining = ['mc1_L5_L6.flag', 'mc1_L6_L23.flag', 'mc1_L4_L6.flag', 'mc2_L5_L6.flag', 'mc2_L6_L23.flag',
             'mc2_L4_L6.flag', 'mc3_L5_L6.flag', 'mc3_L6_L23.flag', 'mc3_L4_L6.flag', 'mc4_L5_L6.flag',
             'mc4_L6_L23.flag', 'mc4_L4_L6.flag', 'mc5_L5_L6.flag', 'mc5_L6_L23.flag', 'mc5_L4_L6.flag',
             'randon12_L4_L5.flag', 'randon15_L4_L5.flag', 'randon17_L4_L5.flag', 'randon12_L5_L23.flag']

remaining = ["randon12_L5_L23.flag"]

mc_massive = ['mc1_L4_L6.flag', 'mc2_L4_L6.flag', 'mc3_L4_L6.flag', 'mc4_L4_L6.flag', 'mc5_L4_L6.flag',
              'mc6_L4_L6.flag', 'mc1_L5_L6.flag', 'mc2_L5_L6.flag', 'mc3_L5_L6.flag', 'mc4_L5_L6.flag',
              'mc5_L5_L6.flag', 'mc6_L5_L6.flag', 'mc1_L6_L23.flag', 'mc2_L6_L23.flag', 'mc3_L6_L23.flag',
              'mc4_L6_L23.flag', 'mc5_L6_L23.flag', 'mc6_L6_L23.flag']



"""
Running Small jobs here
"""

for file in mc_small_jobs:
    if file in remaining:
        approx = "100000"
        a = file.split('.')
        b = a[0].split('_')
        column = b[0][2:]
        groups = "_".join(b[1:])
        output_path = mc_output_path_base + f"{groups}/data_mc{column}_{groups}.homology"
        input_path = mc_input_path_base + f"mc_flag_files_small/{file}"
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
        os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))


for file in random12_small:
    if file in remaining:
        approx = "100000"
        a = file.split('.')
        b = a[0].split('_')
        column = b[0][2:]
        groups = "_".join(b[1:])
        output_path = random_output_path_base + f"{groups}/random12_{groups}.homology"
        input_path = random12_input_path_base + f"random12_small/{file}"
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
        os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))

for file in random15_small:
    if file in remaining:
        approx = "100000"
        a = file.split('.')
        b = a[0].split('_')
        column = b[0][2:]
        groups = "_".join(b[1:])
        output_path = random_output_path_base + f"{groups}/random15_{groups}.homology"
        input_path = random15_input_path_base + f"random15_small/{file}"
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
        os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))

for file in random17_small:
    if file in remaining:
        approx = "100000"
        a = file.split('.')
        b = a[0].split('_')
        column = b[0][2:]
        groups = "_".join(b[1:])
        output_path = random_output_path_base + f"{groups}/random17_{groups}.homology"
        input_path = random17_input_path_base + f"random17_small/{file}"
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
        os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))

"""
Running Small Jobs here
"""

for file in mc_medium_jobs:
    if file in remaining:
        approx = "10000"
        a = file.split('.')
        b = a[0].split('_')
        column = b[0][2:]
        groups = "_".join(b[1:])
        output_path = mc_output_path_base + f"{groups}/data_mc{column}_{groups}.homology"
        input_path = mc_input_path_base + f"mc_flag_files_medium/{file}"
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
        os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))

for file in random12_medium:
    if file in remaining:
        approx = "10000"
        a = file.split('.')
        b = a[0].split('_')
        column = b[0][2:]
        groups = "_".join(b[1:])
        output_path = random_output_path_base + f"{groups}/random12_{groups}.homology"
        input_path = random12_input_path_base + f"random12_medium/{file}"
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
        os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))

for file in random15_medium:
    if file in remaining:
        approx = "10000"
        a = file.split('.')
        b = a[0].split('_')
        column = b[0][2:]
        groups = "_".join(b[1:])
        output_path = random_output_path_base + f"{groups}/random15_{groups}.homology"
        input_path = random15_input_path_base + f"random15_medium/{file}"
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
        os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))

for file in random17_medium:
    if file in remaining:
        approx = "10000"
        a = file.split('.')
        b = a[0].split('_')
        column = b[0][2:]
        groups = "_".join(b[1:])
        output_path = random_output_path_base + f"{groups}/random17_{groups}.homology"
        input_path = random17_input_path_base + f"random17_medium/{file}"
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
        os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))


"""
Running large Jobs
"""

for file in mc_large_jobs:
    if file in remaining:
        approx = "10000"
        a = file.split('.')
        b = a[0].split('_')
        column = b[0][2:]
        groups = "_".join(b[1:])
        output_path = mc_output_path_base + f"{groups}/data_mc{column}_{groups}.homology"
        input_path = mc_input_path_base + f"mc_flag_files_large/{file}"
        print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
        os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))


for file in mc_massive:
    approx = "10000"
    a = file.split('.')
    b = a[0].split('_')
    column = b[0][2:]
    groups = "_".join(b[1:])
    output_path = mc_output_path_base + f"{groups}/data_mc{column}_{groups}.homology"
    input_path = mc_input_path_base + f"mc_flag_files_massive/{file}"
    print(f"NOW RUNNING: {' '.join([cmd, out_opt, output_path, input_path,app_opt,approx])}")
    os.system(" ".join([cmd, out_opt, output_path, input_path,app_opt,approx]))

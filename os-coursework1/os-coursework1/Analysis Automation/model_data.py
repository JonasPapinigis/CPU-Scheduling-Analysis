import numpy as np
import matplotlib.pyplot as plt
from io import BufferedReader
import os
import re
from mpl_toolkits.mplot3d import axes3d

#id	priority	createdTime	startedTime	terminatedTime	cpuTime	blockedTime	turnaroundTime	waitingTime	responseTime

def convert_doc(output_doc):
    contents = ""
    processes = []
    attribute_list = ["id",	"priority", "createdTime", "startedTime", "terminatedTime", "cpuTime", "blockedTime", "turnaroundTime","waitingTime", "responseTime"]
    with open(output_doc, 'r') as f:
        contents = f.read()
    all_lines = contents.split("\n")
    raw_processes = [f.replace("\t"," ") for f in all_lines[1:-2]]
    for proc in raw_processes:
        process_dict = {}
        val_array = proc.split(" ")
        for num,attr in enumerate(attribute_list):
            process_dict[attr] = int(val_array[num])
        processes.append(process_dict)

    return processes

def aggregate_data(experiment):
    scheduler_types = ["Fcfs","IdealSJF", "FeedbackRR","RR","SJF"]
    outputs = []
    #Need this to be (Type, Data)
    output_paths = [f"{experiment}/{f}" for f in os.listdir(experiment) if f.endswith(".out")]
    for path in output_paths:
        _path = path
        scheduler = "ERROR"
        input = -1
        #Want this to be in order so RR check comes after FeedbackRR, as it is its subsrtring
        for type in scheduler_types:
            if type in path:
                scheduler = type
                break
        match = re.search(r'inpt(\d+)', _path)
        input = int(match.group(1))
        if (input < -1 or scheduler == "ERROR"):
            raise RuntimeError(f"Error Extracting Data:{path}")
        outputs.append((scheduler,input,convert_doc(path)))
    return outputs


exp1_out = aggregate_data("experiment1")
prp_files =  [f"inpt{num}.prp" for num in range(0,64)]
#inpt,cpu,io, log(cpu/io)
inpt_cpuio_vals = {}
for num,filename in enumerate(prp_files):
    with open(os.path.join("experiment1",filename),'r') as file:
        lines = file.readlines()
        cpu_burst = int(lines[3].strip().replace("meanCpuBurst=",""))
        io_burst = int(lines[4].strip().replace("meanIOBurst=",""))
        inpt_cpuio_vals[num] = cpu_burst,io_burst,np.log(cpu_burst/io_burst)
"""
for key,value in inpt_cpuio_vals.items():
    print(f"{key},{value}")
"""

exp1_averages = []
for datapoint in exp1_out:
    num_proc = len(datapoint[2])
    cpu_time = turnaround_time =  blocked_time = waiting_time = 0
    means = {}
    for process in datapoint[2]:
        cpu_time += process.get("cpuTime")
        turnaround_time += process.get("turnaroundTime")
        blocked_time += process.get("blockedTime")
        waiting_time += process.get("waitingTime")
    means['cpuTime'] = cpu_time / num_proc
    means['turnaroundTime'] = turnaround_time / num_proc
    means['blockedTime'] = blocked_time / num_proc
    means['waitingTime'] = waiting_time /num_proc
    exp1_averages.append((datapoint[0],datapoint[1],means))


fcfs_means = [f for f in exp1_averages if f[0] == 'Fcfs']
_x = []
_y = []
_z = []
print(fcfs_means)
print(inpt_cpuio_vals)


for mean in fcfs_means:
    _x.append(inpt_cpuio_vals.get(mean[1])[0])
    _y.append(inpt_cpuio_vals.get(mean[1])[1])
    _z.append(mean[2].get('turnaroundTime'))



fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(_x,_y,_z )
ax.set_xlabel('Mean CPU time')
ax.set_ylabel('Mean IO Time')
ax.set_zlabel('Turnaround time')
plt.legend()
plt.show()
    

"""
plt.plot(*gt_data, 'b', label='gt_function')

#plt.plot and .scatter have different ways of setting visuals
plt.scatter(*train_data, marker='x',c='r', label='train_data')

plt.scatter(*val_data, marker='o',c='g', label='train_data')

plt.scatter(*test_data, marker='s',c='k', label='train_data')


plt.legend()
plt.show()

"""



    

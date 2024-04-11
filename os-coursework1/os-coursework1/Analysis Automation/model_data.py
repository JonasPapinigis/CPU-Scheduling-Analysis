import numpy as np
import matplotlib as plt
from io import BufferedReader

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

print(convert_doc(r"Data\Outputs\beta\Fcfs0inpt1.in"))
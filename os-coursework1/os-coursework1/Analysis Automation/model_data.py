import numpy as np
import matplotlib as plt
from io import BufferedReader
import os

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
    scheduler_types = ["Fcfs","IdealSJF", "FeedbackRR","RR","SJFS"]
    outputs = []
    #Need this to be (Type, Data)
    output_paths = [f"{experiment}/{f}" for f in os.listdir(experiment) if f.endswith(".out")]
    print(len(output_paths))
    for path in output_paths:
        scheduler = "ERROR"
        #Want this to be in order so RR check comes after FeedbackRR, as it is its subsrtring
        for type in scheduler_types:
            if type in path:
                scheduler = type
                print(scheduler)
                break
                
        outputs.append((scheduler,convert_doc(path)))
    return outputs
    
        



    
print(aggregate_data("experiment2"))
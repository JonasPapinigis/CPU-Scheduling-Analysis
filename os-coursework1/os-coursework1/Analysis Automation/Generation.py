import numpy as np
import subprocess
import os
from typing import Any










"""
numberOfProcesses=4
staticPriority=0
meanInterArrival=50
meanCpuBurst=15.0
meanIOBurst=15.0
meanNumberBursts=2.0
seed=270826029269605
"""

#InputData class ensures the presence of all values in read parameters
class InputData:
    def __init__(self, num_proc: int, static_prior: int, mean_arrival: int, 
                 mean_cpu: float, mean_io: float, mean_num_burst: float, seed: int):
        
        if any(arg is None for arg in [num_proc, static_prior, mean_arrival, mean_cpu, mean_io, mean_num_burst]):
            raise ValueError("None value is not allowed for any parameter")
        self._num_proc = num_proc
        self._static_prior = static_prior
        self._mean_arrival = mean_arrival
        self._mean_cpu = mean_cpu
        self._mean_io = mean_io
        self._mean_num_burst = mean_num_burst
        if seed == None:
            self._seed = np.random.Generator.integers(100000000000000000,999999999999999999)
        else: 
            self._seed = seed

    

    def to_dict(self):
        return {
            'numberOfProcesses': self._num_proc,
            'staticPriority': self._static_prior,
            'meanInterArrival': self._mean_arrival,
            'meanCpuBurst': self._mean_cpu,
            'meanIOBurst': self._mean_io,
            'meanNumberBursts': self._mean_num_burst,
            'seed': self._seed
        }

    def to_list(self):
        return [self._num_proc, self._static_prior, self._mean_arrival, 
                self._mean_cpu, self._mean_io, self._mean_num_burst, self._seed]
        
        
def create_input_parameters(input_data, name: str, loc=None):
    folder_name = loc if loc is not None else 'Data'
    
    os.makedirs(folder_name, exist_ok=True)
    
    file_path = os.path.join(folder_name, name + ".prp")
    
    contents = ""
    for field_name, value in input_data.to_dict().items():  # Fixed iteration
        contents += f"{field_name}={value}\n"
    
    with open(file_path, 'w') as file:
        file.write(contents)

def create_experiment(init_values, to_test, test_values, trial_name):

    os.makedirs(trial_name, exist_ok=True)

    for num, value in enumerate(test_values):
        values = init_values.copy()  # Create a copy to avoid mutation
        values[to_test] = value
        _input_data = InputData(*values)
        create_input_parameters(_input_data, f"inpt{num}", trial_name)












#run = subprocess.run(['cmd', '/c', 'java','-cp', 'target/os-coursework1-1.0-SNAPSHOT.jar', 'InputGenerator','experiment1/input_parameters.prp','experiment1/inputs.in'],stdout=True,stdin=True)

def generate_inputs(trial_name):

    if not os.path.exists(trial_name) or not os.path.isdir(trial_name):
        raise ValueError("Input Folder Not found")

    input_files = [(os.path.join(trial_name,f)).replace('\\','/') for f in os.listdir(trial_name) if f.endswith(".prp")]

    for file in input_files:
        base_name = os.path.basename(file).replace(".prp","")
        output_destination = os.path.join(trial_name,base_name) + ".in"
        subprocess.run(['cmd', '/c', 'java','-cp', 'target/os-coursework1-1.0-SNAPSHOT.jar', 'InputGenerator', file, output_destination])











"""
scheduler=SJFScheduler
timeLimit=10000
periodic=false
interruptTime=0
timeQuantum=20
initialBurstEstimate=10
alphaBurstEstimate=0.5
"""


class SchedulerParams:

    def __init__(self,scheduler: str, timeLimit: int, periodic: bool, interruptTime: int, 
                 timeQuantum: int, initBurstEst: float, alphaBurstEst: float):

        if (scheduler not in ["FcfsScheduler","IdealSJFScheduler","RRScheduler","FeedbackRRScheduler","SJFScheduler"]):
            raise ValueError("Not a Real scheduler (FcfsScheduler,IdealSJFScheduler,RRScheduler,FeedbackRRScheduler,SJFScheduler")
        self.scheduler = scheduler
        self.timeLimit = timeLimit
        self.periodic = periodic
        self.interruptTime = interruptTime
        self.timeQuantum = timeQuantum
        self.initBurstEst = initBurstEst
        self.alphaBurstEst = alphaBurstEst

    def to_dict(self):

        return {
            'scheduler': self.scheduler,
            'timeLimit': self.timeLimit,
            'periodic': self.periodic,
            'interruptTime': self.interruptTime,
            'timeQuantum': self.timeQuantum,
            'initialBurstEstimate': self.initBurstEst,
            'alphaBurstEstimate': self.alphaBurstEst
        }

    def to_list(self):

        return [self.scheduler, self.timeLimit, self.periodic, 
                self.interruptTime, self.timeQuantum, self.initBurstEst, self.alphaBurstEst]




def create_input_file(input_data, name: str, trial_name):
    
    if not os.path.exists(trial_name):
        raise ValueError("Experiment directory not found")
    
    file_path = os.path.join(trial_name, f"{name}.prp")
    
    contents = ""
    for field_name, value in input_data.to_dict().items():
        contents += f"{field_name}={value}\n"
    
    with open(file_path, 'w') as file:
        file.write(contents)

def create_schedulers(init_values, to_test, test_values, trial_name):
    # Define all possible schedulers
    all_schedulers = ["FcfsScheduler", "IdealSJFScheduler", "RRScheduler", "FeedbackRRScheduler", "SJFScheduler"]
    
    # Determine which schedulers to test
    mask = init_values[0]
    print(init_values)
    if mask:
        schedulers_to_test = [scheduler for scheduler, to_include in zip(all_schedulers, mask) if to_include]
    else:
        schedulers_to_test = all_schedulers
    
    

    for scheduler in schedulers_to_test:
        scheduler_short_name = scheduler.replace("Scheduler", "")  
        
        for num, value in enumerate(test_values):
            values = init_values[1:].copy()  
            
            if to_test > 0:  
                
                values.insert(0, scheduler)
                
                values[to_test] = value
            _input_data = SchedulerParams(*values)
            
            file_name = f"{scheduler_short_name}{num}_"
            create_input_file(_input_data, file_name, trial_name)













#run = subprocess.run(['cmd', '/c', 'java','-cp', 'target/os-coursework1-1.0-SNAPSHOT.jar', 'InputGenerator','experiment1/input_parameters.prp','experiment1/inputs.in'],stdout=True,stdin=True)

def generate_outputs(trial_name):


    #print(f"Input,Scheduler,Output Directories:\n{input_path}\n{scheduler_path}\n{output_path}")

    if not os.path.exists(trial_name) or not os.path.isdir(trial_name):
        raise ValueError("Input Folder(s) Not found")

    input_files = [f for f in os.listdir(trial_name) if f.endswith(".in")]
    
    schedulers = [f for f in os.listdir(trial_name) if f.endswith("_.prp")]
    print(input_files,schedulers)

    for scheduler in schedulers: 
        for input in input_files:
            scheduler_base = os.path.basename(scheduler)
            input_base = os.path.basename(input)
            
            output_filename = scheduler_base.replace("_.prp","")+input_base.replace(".in","")+".out"
            final_output = os.path.join(trial_name,output_filename).replace("\\","/")
            
            print(f"Final Name:{final_output}")
            subprocess.run(['cmd', '/c', 'java','-cp', 'target/os-coursework1-1.0-SNAPSHOT.jar', 'Simulator', f"{trial_name}/{scheduler}", final_output, f"{trial_name}/{input}"])










    

example_params = [4,0,50,15.0,15.0,2.0,270826029269605]
_to_test = 2
_test_values = [10,20,40,80,160]
_test_name = "experiment2"
create_experiment(example_params,_to_test,_test_values,_test_name)

generate_inputs("experiment2")
_init_values = [[True,True,False,False,False], 10000, False, 0, 20, 10.0, 0.5]  
_to_test = 4  
_test_values = [10, 20, 30, 40]  
_trial_name = "experiment2"

create_schedulers(_init_values, _to_test, _test_values, _trial_name)

generate_outputs('experiment2')
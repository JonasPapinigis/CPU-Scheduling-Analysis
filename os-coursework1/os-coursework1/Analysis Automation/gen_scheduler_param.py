import numpy as np
import os
from typing import Any
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




def create_input_file(input_data, name: str, loc=None):
    folder_name = loc if loc is not None else 'Data/Parameters'
    
    os.makedirs(folder_name, exist_ok=True)
    
    file_path = os.path.join(folder_name, f"{name}.in")
    
    contents = ""
    for field_name, value in input_data.to_dict().items():
        contents += f"{field_name}={value}\n"
    
    with open(file_path, 'w') as file:
        file.write(contents)

def create_experiment(init_values, to_test, test_values, trial_name):
    base_folder_name = 'Data/Scheduler_Parameters'
    # Define all possible schedulers
    all_schedulers = ["FcfsScheduler", "IdealSJFScheduler", "RRScheduler", "FeedbackRRScheduler", "SJFScheduler"]
    
    # Determine which schedulers to test
    mask = init_values[0]
    if mask:
        schedulers_to_test = [scheduler for scheduler, to_include in zip(all_schedulers, mask) if to_include]
    else:
        schedulers_to_test = all_schedulers
    
    inputs_folder_name = os.path.join(base_folder_name, trial_name)
    os.makedirs(inputs_folder_name, exist_ok=True)
    
    
    for scheduler in schedulers_to_test:
        scheduler_short_name = scheduler.replace("Scheduler", "")  
        
        for num, value in enumerate(test_values):
            values = init_values[1:].copy()  
            
            if to_test > 0:  
                
                values.insert(0, scheduler)
                
                values[to_test] = value
            _input_data = SchedulerParams(*values)
            
            file_name = f"{scheduler_short_name}{num}"
            create_input_file(_input_data, file_name, inputs_folder_name)

_init_values = [[True,True,False,False,False], 10000, False, 0, 20, 10.0, 0.5]  
_to_test = 4  
_test_values = [10, 20, 30, 40]  
_trial_name = "beta"
create_experiment(_init_values, _to_test, _test_values, _trial_name)




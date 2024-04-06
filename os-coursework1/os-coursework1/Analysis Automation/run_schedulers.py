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
    base_folder_name = 'Data/Parameters'
    # Define all possible schedulers
    all_schedulers = ["FcfsScheduler", "IdealSJFScheduler", "RRScheduler", "FeedbackRRScheduler", "SJFScheduler"]
    
    # Determine which schedulers to test
    schedulers_to_test = init_values[0] if init_values[0] else all_schedulers
    
    inputs_folder_name = os.path.join(base_folder_name, trial_name)
    os.makedirs(inputs_folder_name, exist_ok=True)
    
    # Iterate through each specified scheduler
    for scheduler in schedulers_to_test:
        scheduler_short_name = scheduler.replace("Scheduler", "")  # Simplify the scheduler name
        # Iterate through each test value for the parameter
        for num, value in enumerate(test_values):
            values = init_values[1:].copy()  # Skip the first value which is for schedulers
            # Adjust the specified parameter with the current test value
            if to_test > 0:  # Ensure to_test is within valid range
                # Insert scheduler at the beginning of the values list
                values.insert(0, scheduler)
                # Adjust the test parameter
                values[to_test] = value
            _input_data = SchedulerParams(*values)
            # Format file name as [schedulerShortName][num]
            file_name = f"{scheduler_short_name}{num}"
            create_input_file(_input_data, file_name, inputs_folder_name)

# Example usage
_init_values = ["", 10000, False, 0, 20, 10.0, 0.5]  # Empty string for all schedulers
_to_test = 4  # Index for the parameter to test
_test_values = [10, 20, 30, 40]  # Different values for the test parameter
_trial_name = "QuantumVariation"
create_experiment(_init_values, _to_test, _test_values, _trial_name)




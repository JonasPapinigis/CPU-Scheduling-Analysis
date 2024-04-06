import numpy as np
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
    
    file_path = os.path.join(folder_name, name + ".in")
    
    contents = ""
    for field_name, value in input_data.to_dict().items():  # Fixed iteration
        contents += f"{field_name}={value}\n"
    
    with open(file_path, 'w') as file:
        file.write(contents)

def create_experiment(init_values, to_test, test_values, trial_name):
    base_folder_name = 'Data/Input_Parameters'
    inputs_folder_name = os.path.join(base_folder_name, trial_name)

    os.makedirs(inputs_folder_name, exist_ok=True)

    for num, value in enumerate(test_values):
        values = init_values.copy()  # Create a copy to avoid mutation
        values[to_test] = value
        _input_data = InputData(*values)
        create_input_parameters(_input_data, f"inpt{num}", inputs_folder_name)



example_params = [4,0,50,15.0,15.0,2.0,270826029269605]
_to_test = 2
_test_values = [10,20,40,80,160]
_test_name = "beta"
create_experiment(example_params,_to_test,_test_values,_test_name)




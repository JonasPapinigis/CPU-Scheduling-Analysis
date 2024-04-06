import os
import subprocess

#run = subprocess.run(['cmd', '/c', 'java','-cp', 'target/os-coursework1-1.0-SNAPSHOT.jar', 'InputGenerator','experiment1/input_parameters.prp','experiment1/inputs.in'],stdout=True,stdin=True)

def generate_inputs(parameter_dir: str):
    input_path = os.path.join(r'Data\Input_Parameters', parameter_dir)
    output_path = os.path.join(r'Data\Inputs',parameter_dir)

    if not os.path.exists(output_path) or not os.path.isdir(output_path):
        os.makedirs(output_path, exist_ok=True)
    if not os.path.exists(input_path) or not os.path.isdir(input_path):
        raise ValueError("Input Folder Not found")

    input_files = []
    for file in os.listdir(input_path):
        dependant_path = os.path.join(input_path,file)
        input_files.append(dependant_path)
    
    jar_path = 'target/os-coursework1-1.0-SNAPSHOT.jar'

    for file in input_files:
        base_name = os.path.basename(file)
        output_destination = os.path.join(output_path,base_name)
        subprocess.run(['cmd', '/c', 'java','-cp', 'target/os-coursework1-1.0-SNAPSHOT.jar', 'InputGenerator', file, output_destination])


generate_inputs("beta")

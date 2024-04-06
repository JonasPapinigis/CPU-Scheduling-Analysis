import os
import subprocess
import numpy as np

def generate_inputs(folder_name: str):
    base_path = os.path.join('Data', 'Input_Parameters')
    folder_path = os.path.join(base_path, folder_name)

    print("Input path:"+folder_path)

    
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        raise ValueError(f"Directory {folder_name} doesn't exist")
    
    output_folder = os.path.join('Data', 'Inputs', folder_name)
    print("Output folder: "+output_folder)
    os.makedirs(output_folder, exist_ok=True)
    print()
    #file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(os.listdir(folder_path))
    file_paths = []
    for file in os.listdir(folder_path):
        dependant_path = os.path.join(folder_path,file).replace('\\','/')
        print(dependant_path)
        file_paths.append(dependant_path)
        


    jar_path = 'target/os-coursework1-1.0-SNAPSHOT.jar'
    for input_file in file_paths:
        output_file = os.path.join(output_folder, os.path.basename(input_file).replace('_parameters.prp', '_inputs.in')).replace('\\','/')
        command = ['wsl', f'java -cp {jar_path} InputGenerator {input_file} {output_file}']
        try:
            subprocess.run(command, cwd=os.getcwd(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to generate inputs for {input_file}: {e}")


_command = ['wsl', 'ls']
subprocess.run(_command, cwd=os.getcwd(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#generate_inputs("alpha")
import os
import subprocess

#run = subprocess.run(['cmd', '/c', 'java','-cp', 'target/os-coursework1-1.0-SNAPSHOT.jar', 'InputGenerator','experiment1/input_parameters.prp','experiment1/inputs.in'],stdout=True,stdin=True)

def generate_inputs(input_dir: str):
    input_path = os.path.join(r'Data\Inputs', input_dir)
    scheduler_path = os.path.join(r'Data\Scheduler_Parameters',input_dir)
    output_path = os.path.join(r'Data\Outputs',input_dir)

    #print(f"Input,Scheduler,Output Directories:\n{input_path}\n{scheduler_path}\n{output_path}")

    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)
    if not os.path.exists(input_path) or not os.path.exists(scheduler_path):
        raise ValueError("Input Folder(s) Not found")

    input_files = []
    for file in os.listdir(input_path):
        dependant_path = os.path.join(input_path,file).replace('\\','/')
        input_files.append(dependant_path)
    
    schedulers = []
    for file in os.listdir(scheduler_path):
        dependant_path = os.path.join(scheduler_path,file).replace('\\','/')
        schedulers.append(dependant_path)
    
    for scheduler in schedulers: 
        for input in input_files:
            scheduler_base = os.path.basename(scheduler)
            input_base = os.path.basename(input)
            
            output_filename = scheduler_base.replace(".in","")+input_base
            final_output = os.path.join(output_path,output_filename)
            #print(f"Final Name:{final_output}")
            subprocess.run(['cmd', '/c', 'java','-cp', 'target/os-coursework1-1.0-SNAPSHOT.jar', 'Simulator', scheduler, final_output,input,])


generate_inputs('beta')
    
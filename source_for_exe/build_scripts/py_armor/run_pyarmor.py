import subprocess
import os

def run_pyarmor(input_directory, python_files, output_directory):
    print('here')
    print(python_files)
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    for python_file in python_files:
        # Check if python_file is a dictionary with the required fields
        if isinstance(python_file, dict) and 'relative_file_path' in python_file and 'absolute_file_path' in python_file:
            # Get the relative and absolute paths from the dictionary
            relative_path = python_file['relative_file_path']
            absolute_path = python_file['absolute_file_path']

            # Construct the full path for the Python file using input_directory and relative_path
            full_python_path = os.path.join(input_directory, relative_path)
            
            print(f"Processing file: {full_python_path}")
            
            # Ensure the Python file exists at the absolute path
            if not os.path.isfile(absolute_path):
                print(f"Error: {absolute_path} does not exist.")
                continue

            # Construct the output path while preserving the directory structure
        
            full_output_path = os.path.join(output_directory, os.path.dirname(relative_path))

            # Create the output directory for the protected files if it doesn't exist
            os.makedirs(full_output_path, exist_ok=True)

            # Change the current working directory to the directory of the Python file
            
            os.chdir(os.path.dirname(absolute_path))
            # Construct the PyArmor command to protect the individual Python file
            pyarmor_command = [
                'pyarmor', 'gen',
                '--output', full_output_path,  # Specify the output folder
                os.path.basename(absolute_path)  # Protect each individual Python file
            ]

            # Run the PyArmor command
            try:
                subprocess.run(pyarmor_command, check=True)
                print(f"File '{absolute_path}' protected successfully with PyArmor.")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while running PyArmor on '{absolute_path}': {e}")
                print("Command was:", pyarmor_command)  # Print the command for debugging
        else:
            # Provide more feedback if the python_file entry is invalid
            print(f"Invalid entry in python_files: {python_file}")


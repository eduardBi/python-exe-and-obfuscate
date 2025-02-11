import subprocess
import os
import shutil  # For cleaning or renaming directories
from config_definer.encryptor_config import type_of_executable

def build_executable(script_name, dist_path, work_path, collected_array, add_data_files):
    # Ensure the script exists
    if not os.path.isfile(script_name):
        print(f"Error: {script_name} does not exist.")
        return

    # Ensure dist_path and work_path exist, create them if they don't
    os.makedirs(dist_path, exist_ok=True)
    os.makedirs(work_path, exist_ok=True)

    # Clean the work path directory if needed
    if os.path.exists(work_path):
        print(f"Cleaning up the work directory '{work_path}'...")
        shutil.rmtree(work_path)  # Clear the work path
        os.makedirs(work_path, exist_ok=True)

    # Construct the PyInstaller command
    command = [
        'pyinstaller',
        type_of_executable,  # Creates a one-folder bundle instead of one file
        '--distpath', dist_path,  # Specify the output folder
        '--workpath', work_path,  # Specify a custom build directory
    ]

    # Loop through the collected imports and add them as hidden imports
    for file_info in collected_array:
        for imp in file_info['contains_imports']:
            # Check for standard import
            if imp.startswith('import '):
                module_name = imp.split('import ')[-1].strip().split()[0]  # Get the module name
                command.append(f'--hidden-import={module_name}')
            # Check for from-import statements
            elif imp.startswith('from '):
                module_name = imp.split('from ')[1].split(' import ')[0]  # Get the module name
                command.append(f'--hidden-import={module_name}')

    # Add the main script to the command
    command.append(script_name)

    # Add the additional data files to the command
    for file_path in add_data_files:
        # Use the format "source_path:destination_path" for add-data
        # Set destination to be at the same level as the script being bundled
        print(file_path['entry_point'])
        print(file_path['output_point'])
        print('hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        command.append(f"--add-data={file_path['entry_point']}:{file_path['output_point']}")


    print("Executing command:", ' '.join(command))
    # Run the command
    try:
        subprocess.run(command, check=True)
        print(f"Executable for {script_name} created successfully in '{dist_path}'.")
        return dist_path+'/app'

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running PyInstaller: {e}")


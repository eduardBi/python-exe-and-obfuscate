import os
from build_scripts.py_armor.find_path_difference import find_path_difference



def putch_imports_folder(output_folder, imports_info):

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for import_data in imports_info:
        
        # Get the relative path of the original file from the imports_info
        relative_path = import_data['relative_file_path']


        # remove unnesasary tree branching (for example if build sccripts exists (wraps) one folder above source code)
        remove_folder_leveling = find_path_difference(output_folder,import_data['relative_file_path'])
        
        # Get the full path for the new file in the output folder
        new_file_path = os.path.join(output_folder, relative_path)

        
        # Get the directory path for the new file
        directory_path = os.path.dirname(new_file_path)
        
        # Create the directory if it doesn't exist
        os.makedirs(directory_path, exist_ok=True)
        
        # Create the file and write the imports into it
        with open(new_file_path, 'w') as f:
            for import_statement in import_data['contains_imports']:
                f.write(import_statement + '\n')  # Write each import line into the file

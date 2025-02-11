import os
import fnmatch

def recursive_imports(current_path,data_to_exclude):
    python_files = []
    
    # Specify excluded items
    excluded_files = data_to_exclude["excluded_files"]
    excluded_dirs = data_to_exclude["excluded_dirs"]

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(current_path):
        # Remove excluded directories from the traversal
        dirnames[:] = [d for d in dirnames if d not in excluded_dirs]

        for filename in fnmatch.filter(filenames, '*.py'):
            # Skip excluded files
            if filename in excluded_files:
                continue
            
            # Construct the full path of the file
            full_path = os.path.join(dirpath, filename)
            # Append the full path to the list
            python_files.append(full_path)

    
    return python_files


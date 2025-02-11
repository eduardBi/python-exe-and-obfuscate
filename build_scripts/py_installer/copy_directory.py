import shutil
import os

def copy_directory(source, destination):
    """Copy a directory from the source path to the destination path."""
    # Check if the source directory exists
    if not os.path.isdir(source):
        print(f"Error: Source directory '{source}' does not exist or is not a directory.")
        return
    
    # If destination exists, copy files inside the source directory to the destination
    if os.path.exists(destination):
        try:
            for item in os.listdir(source):
                s = os.path.join(source, item)
                d = os.path.join(destination, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)  # Copy subdirectory
                else:
                    shutil.copy2(s, d)  # Copy file
            print(f"Directory contents copied from '{source}' to existing '{destination}'.")
        except Exception as e:
            print(f"An error occurred while copying the directory contents: {e}")
    else:
        # If destination does not exist, copy the entire directory
        try:
            shutil.copytree(source, destination)
            print(f"Directory copied from '{source}' to '{destination}'.")
        except Exception as e:
            print(f"An error occurred while copying the directory: {e}")


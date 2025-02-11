import shutil
import os

def copy_file(source, destination):
    """Copy a file from the source path to the destination path."""
    # Check if the source file exists
    if not os.path.isfile(source):
        print(f"Error: Source file '{source}' does not exist.")
        return
    
    # Create the destination directory if it does not exist
    destination_dir = os.path.dirname(destination)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    try:
        shutil.copy(source, destination)  # Copy the file
        print(f"File copied from '{source}' to '{destination}'.")
    except Exception as e:
        print(f"An error occurred while copying the file: {e}")


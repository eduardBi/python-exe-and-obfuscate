import os
import shutil  


def rename_build_exe_dir(dist_path, old_folder_name):
    """Rename the build directory from old_folder_name to miner_dist."""
    old_folder = os.path.join(dist_path, old_folder_name)  # Construct the full path to the old folder
    new_folder = os.path.join(dist_path, 'miner_dist')  # New folder name

    if os.path.exists(old_folder):
        shutil.move(old_folder, new_folder)  # Rename the folder
        print(f"Folder renamed from '{old_folder}' to '{new_folder}'.")
    else:
        print(f"Error: Folder '{old_folder}' does not exist for renaming.")

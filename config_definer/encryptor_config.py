import os

# Get the absolute path of the current file
encryptor_config_path = os.path.abspath(__file__)

# Get the parent directory (one level above)
current_folder = os.path.dirname(os.path.dirname(encryptor_config_path))  # Move up one directory

type_of_executable = "--onedir"

# type_of_executable = "--onefile"

souce_code_dir = os.path.join(current_folder, 'source_for_exe')

hashed_dir_destanation = os.path.join(current_folder, 'source_for_exe/armor_hashed')

cleaned_dir_destanation = os.path.join(current_folder, 'source_for_exe/import_clean')

build_dist = os.path.join(current_folder, 'source_for_exe/dist2')

work_dist_path = os.path.join(current_folder, 'source_for_exe/dist_helper')  # Change this to your desired build path


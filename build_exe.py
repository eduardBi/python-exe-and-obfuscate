#potentially i obfuscate as many times as there python files in folder

# from build_scripts.py_installer.rename_build_exe_dir import rename_build_exe_dir
# from build_scripts.py_installer.copy_file import copy_file
# from build_scripts.py_installer.copy_directory import copy_directory

import os
import shutil

from build_scripts.py_installer.build_executable import build_executable
from build_scripts.py_armor.run_pyarmor import run_pyarmor
from build_scripts.py_armor.recursive_imports import recursive_imports
from build_scripts.py_armor.collect_imports import collect_imports
from build_scripts.py_armor.putch_imports_folder import putch_imports_folder


from config_definer.encryptor_config import souce_code_dir
from config_definer.encryptor_config import current_folder
from config_definer.encryptor_config import hashed_dir_destanation
from config_definer.encryptor_config import cleaned_dir_destanation
from config_definer.encryptor_config import build_dist
from config_definer.encryptor_config import work_dist_path


from config_definer.not_python_imports import not_python_imports
from config_definer.data_to_exclude import data_to_exclude


def build_exe_to_spread(path_to_bootable_file):	

	# Get the list of Python files excluding files like "build_script.py" and folder "build_script"
	all_python_files_in_dir = recursive_imports(souce_code_dir,data_to_exclude)

	#changing directory to build_exe_source because build scripts one level above
	os.chdir(souce_code_dir)

	#returns massive of objects filename:string ,contains_imports:[import numpy,]
	collected_array=collect_imports(all_python_files_in_dir)

	print(collected_array)


	cleand_imports=cleaned_dir_destanation

	#creates clean imported files
	created_imports=putch_imports_folder(cleand_imports, collected_array)

	
	hashed = hashed_dir_destanation

	#hashesentry_point
	run_pyarmor(souce_code_dir, collected_array, hashed)

	hashed_python_entry = hashed + path_to_bootable_file

	return build_executable(hashed_python_entry,build_dist,work_dist_path,collected_array,not_python_imports)




path_to_bootable_file = "/app.py"
build_exe_to_spread(path_to_bootable_file)
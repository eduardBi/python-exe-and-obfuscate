# About Project  
It obfuscates and makes an exe from your file (after running `build_exe.py`, the exe file will be available in `source_for_exe/dist2`). However, to run the exe, you still need Python and all required libraries installed.  

# Take Into Consideration  
Every time you import, all imports are supposed to have only **one space** between words because PyInstaller doesn't handle imports well, so I hardcoded it.  

Extracting imports **can still fail**, but I covered most cases in `collect_imports` (like excluding imports if they are commented out using `""" """`).  

✅ `[from config_definer.encryptor_config import souce_code_dir]`  

✅ `[from[space]config_definer.encryptor_config[space]import souce_code_dir]`  

❌ `[from[space]config_definer.encryptor_config[space][space]import souce_code_dir]`  

❌ `[from[space][space]config_definer.encryptor_config[space]import souce_code_dir]`  

❌ `[from[space][space]config_definer.encryptor_config[space][space]import souce_code_dir]`  

# You Still Need Python  
Even though it makes a `.exe` from the file, you **still need to install Python and its libraries** on your system. It does not make it executable on the system level, but rather allows the executable file to trigger Python libraries.  

If you are considering running it in **Docker**, you **must install all Python dependencies inside the container**.  

# How To Use  

### Handling Non-Python Imports  
Inside the `config_definer` folder, you can add `not_python_imports`. These could be **pictures, videos, or other non-Python files**. Any files that **do not** have a `.py` extension belong here.  

### Excluding Unnecessary Files  
Inside the `config_definer` folder, you can add `data_to_exclude`.  
This contains **folders and directories to exclude**. By default, the project excludes **build scripts** on an internal level (`source_for_exe/build_script`).  

### Configuring Source Code Directory  
In `encryptor_config`, you must define `souce_code_dir`, which is the directory **from which all files will be obfuscated** into `armor_hashed_folder`.  
All necessary imports for PyInstaller will be stored in `import_clean`.  

### Choosing Output Type  
To make the output a **single executable file**, uncomment:  
`type_of_executable = "--onefile"` inside `encryptor_config`.  

To make the output a **directory with all internal files**, uncomment:  
`type_of_executable = "--onedir"` inside `encryptor_config`.  

### Running the Build Script  
Inside `build_exe.py`, pass the **path to your main Python file** inside the `build_exe_to_spread()` function.  

For example:  
If your main script is `/app.py` inside `source_for_exe`, just pass `app.py`.  
If your script is inside `source_for_exe/start/app.py`, pass `start/app.py`.  

After running `build_exe.py`, inside `souce_code_dir` (in my case, `"source_for_exe"` folder), you will get:  
📂 `source_for_exe/dist2/app` → **Executable file that can be run in the console**.  

### Cleanup  
🚨 **There is no cleanup script!**  
After each build, you need to manually delete:  
- `dist2`  
- `clean_import`  
- `armor_hashed`  
- `dist_helper`  

These folders will remain after execution.  

import os
import re

def collect_imports(python_files):
    result = []
    
    # Define regex patterns for matching "import" and "from" as whole words
    import_pattern = re.compile(r'(?<!\S)\bimport\b(?!\S)')  # Match "import" as a whole word
    from_pattern = re.compile(r'(?<!\S)\bfrom\b(?!\S)')      # Match "from" as a whole word
    print_pattern = re.compile(r'\bprint\s*\(.*?\)')          # Regex to match print statements

    for file_path in python_files:  # Use full paths directly
        contains_imports = []
        has_imports = False

        try:
            with open(file_path, 'r') as file:
                skip_lines = False  # Flag to skip lines after a docstring starts
                in_string = False    # Flag to track if we are inside a string

                for line in file:
                    # Remove comments
                    line = line.split('#', 1)[0].strip()  # Keep only the part before the first '#'

                    # Check for triple quotes to skip lines
                    if "'''" in line or '"""' in line:
                        skip_lines = True  # Set the flag to skip subsequent lines
                        continue  # Skip the current line

                    # Check for string literals
                    if '"' in line or "'" in line:
                        # Toggle the in_string flag based on quotes
                        quotes_count = line.count('"') + line.count("'")
                        if quotes_count % 2 == 1:
                            in_string = not in_string  # Toggle only if odd count of quotes

                    # If we are in a string or in a print statement, skip this line
                    if in_string or print_pattern.search(line):
                        continue  # If inside a string or a print statement, skip the line

                    # Check if the line contains "import" or "from" as whole words
                    if import_pattern.search(line) or from_pattern.search(line):
                        contains_imports.append(line.strip())  # Add the import line
                        has_imports = True

            # Append the file information to the result list if imports are found
            relative_path = os.path.relpath(file_path)  # Get relative path from current directory
            if not has_imports:
                contains_imports.append('import os')
            
            result.append({
                'absolute_file_path': file_path,  # Use full path directly
                'relative_file_path': relative_path,  # Calculate relative path
                'contains_imports': contains_imports
            })
        
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

    return result
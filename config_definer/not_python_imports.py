import os
#moving picture to executable diectory space

# Construct the correct image path / getting two folders above
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# searching source image
image_path = os.path.join(script_dir, "source_for_exe/90-Wildlife-1200x834.jpg")  # Adjust path as needed

not_python_imports=[
	{
		"entry_point": image_path,
		"output_point": './'
	}
]
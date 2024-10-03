from pathlib import Path

# Get the current directory of the script
script_dir = Path(__file__).parent

# Create a relative path to the text file
file_path = script_dir / 'random-words.txt'

# Read the contents of the text file
with file_path.open('r') as file:
    random_data_words = [line.strip() for line in file]

# Write the list to a new Python file
output_file_path = script_dir / 'output_list.py'
with output_file_path.open('w') as genereate_py_file:
    genereate_py_file.write(f"random_words = {random_data_words}\n")
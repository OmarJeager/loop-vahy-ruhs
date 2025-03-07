import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the sus.bat file
bat_file_path = os.path.join(current_directory, 'sus.bat')

# Run the sus.bat file
os.system(f'start {bat_file_path}')
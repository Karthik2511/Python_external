import os

# Specify the current file name and the new file name
current_name = 'old_file.txt'
new_name = 'new_file.txt'

# Rename the file
os.rename(current_name, new_name)

print(f"File renamed from {current_name} to {new_name}")

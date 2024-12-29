import os
import time

# Get the file path from the user
file_path = input("Enter the file path: ") #file location like  C:\Users\users\Documents\file.txt

if os.path.exists(file_path):
    # Get file statistics
    file_info = os.stat(file_path)

    # File size in bytes
    file_size = file_info.st_size

    # File creation time (converted to human-readable format)
    creation_time = time.ctime(file_info.st_ctime)

    # File modification time (converted to human-readable format)
    modification_time = time.ctime(file_info.st_mtime)

    # Print the file information
    print(f"File Path: {file_path}")
    print(f"File Size: {file_size} bytes")
    print(f"Creation Time: {creation_time}")
    print(f"Modification Time: {modification_time}")
else:
    print("The file does not exist.")

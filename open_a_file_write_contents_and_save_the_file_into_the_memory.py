# Open the file in write mode
with open('example.txt', 'w') as file:
    # Write some content to the file
    file.write("Hello, this is the content of the file.\n")
    file.write("The file is saved to the filesystem.\n")

print("File 'example.txt' has been created and saved.")

# write a python program to print the contents of a directory using the os module
#  Import the built-in os module
import os
directory_path = "C:\\Users\\HP\\Documents"
# os.listdir() returns a list of all files and folders in the directory
contents = os.listdir(directory_path)
# Print a message showing which directory is being listed
print(f"Contents of the directory '{directory_path}':")
# Loop through the contents and print each item
for item in contents:
    print(item)
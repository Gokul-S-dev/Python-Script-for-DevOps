import os

DIR = r"C:\Users\Gokul S"

files = os.listdir(DIR)
with open("file_list.txt","w") as output_files:
    for file in files:
        output_files.write(file+ "\n")

print("File names saved to file_list.txt")
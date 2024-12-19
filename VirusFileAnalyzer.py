import zipfile as zf
import os

files = zf.ZipFile("HackerProgram.zip", 'r') # Extraction folder
files.extractall('/Downloads') # Use your own /DestinationFolder

directory = '/Python 2024' # Directory of the files

#Autmatically look for specified file in every folder
def remove_file(filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            file_path = os.path.join(root, filename)
            try:
                os.remove(file_path)
                print(f"Removed: {file_path}")
            except Exception as e:
                print(f"Error removing {file_path}: {e}")

# Traversal through directory
for root, dirs, files in os.walk(directory):
    for file in files:
        print(os.path.join(root, file)) # Prints all files in directory object

# Task 1: Find the file: LooksGood.bin in the file folder and then remove it.
remove_file('LooksGood.bin')

#Show the file is deleted
for root, dirs, files in os.walk(directory):
    for file in files:
        print(os.path.join(root, file))

##### String Lookup #####
def word_lookup(directory, filename, word):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            file_path = os.path.join(root, filename)
            print(f"File found: {file_path}")

            with open(file_path, "r") as file:
                for line in file:
                    if word in line:
                        print(line.strip())
            break
    else:
        print(f"File '{filename}' not found in directory '{directory}'.")

# Task 2: Find the file virus_test_file.txt, read it, find and show/print all the lines with the word “Malicious”
# Parameters to change
directory = "/Python 2024"  
file_name = "virus_test_file.txt"              
keyword = "Malicious"

word_lookup(directory, file_name, keyword)

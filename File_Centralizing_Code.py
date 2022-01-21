import shutil
import os
from time import sleep
from tqdm import tqdm

# Define the fastq source directory and destination
source = ''
dest = ''
total = 0

# Get count of ".fastq.gz" files in the source directory and all subdirectories
for root, dirs, files in os.walk(source):
    for file in files:
        # change text in quotes if looking for different file types
        if file.endswith(".fastq.gz"):
            total += 1

# Progress bar that updates based on number of files to copy
for i in tqdm(range(total), desc="Progress"):
    sleep(0.001)
    # For loop through files in source and copy them to destination directory
    for root, dirs, files in os.walk(source):
        for file in files:
            # change text in quotes if looking for different file types
            if file.endswith(".fastq.gz"):
                path_file = os.path.join(root, file)
                shutil.copy2(path_file, dest)
print("Transfer Complete")

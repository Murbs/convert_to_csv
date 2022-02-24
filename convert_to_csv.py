import os
import pandas as pd

# Paths can be replaced with env variables, otherwise use raw strings
filepath = r'' # ingest data here
destination = r'' # outfiles go here
directory_list = os.listdir(filepath) # read directory into loop

os.chdir(filepath)

# Saves all .txt files in a directory as .csv
for files in directory_list:
    if files.endswith('.txt'):
        out_file = '\\'.join([destination,files])
        read_files = pd.read_csv(files).to_csv(out_file.replace('.txt', '.csv'), index=None)

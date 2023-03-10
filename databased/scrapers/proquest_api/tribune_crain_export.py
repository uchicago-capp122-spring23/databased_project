'''
Project: Analyzing News Coverage of Chicago's 2023 Mayoral Election
Team: dataBASED

File name: export.py
Associated files: data/proquest_files/chicago_tribune_2022.tar, 
    data/proquest_files/chicago_tribune_2023.tar, 
    data/proquest_files/chicago_tribune_final.tar, data/proquest_files/crain.tar
Primary Author: Kathryn Link-Oberstar

Description: Convert xml files from Proquest Dataset into a list of JSON files 
to export. This module takes a Proquest dataset (a folder of xml files - one for 
each newssource sepcified below)  from April 11, 2022 (the date of the first 
mayoral candidate's annoucement) to February 28, 2023 (election day) with the 
keyword "mayor". This module converts compresses and exports the file to stay 
within the Proquest 15MB weekly download limit. 
This function was run 4 times for:
    * Chicago Tribune (Online) 2022
        files_to_export  = "data/Chicago_Tribune_-_Mayor_-_2022"
        parq_file_path = "data/chicago_tribune_2022.parquet"
        tz_file_path = "data/chicago_tribune_2022.tar.gz"
    * Chicago Tribune (Online) 2023
        files_to_export  = "data/Chicago_Tribune_-_Mayor_-_2023"
        parq_file_path = "data/chicago_tribune_2023.parquet"
        tz_file_path = "data/chicago_tribune_2023.tar.gz"
        files_to_export  = "data/Chicago_Tribune_-_Mayor_-_Final_Week"
        parq_file_path = "data/chicago_tribune_final.parquet"
        tz_file_path = "data/chicago_tribune_final.tar.gz"
    * Crain Business Journal
        files_to_export  = "data/Crain_-_Mayor"
        parq_file_path = "data/crain.parquet"
        tz_file_path = "data/crain.tar.gz"

This files runs directly in ProQuest virtual environment. 
'''
import xmltodict
import pyarrow
import os
import json
import pandas as pd

# Replace FILES_TO_EXPORT, parq_file_path and tz_file_path with correct file paths
files_to_export  = " "
parq_file_path = " "
tz_file_path = " "

# Convert folder of xml files to list of JSON files
file_list = os.listdir(files_to_export)
file_list = [file for file in file_list if file.endswith("xml")]

list_of_file_data = []

for file in file_list:
    file_path = os.path.join(files_to_export , file)
    with open(file_path, "r") as f:
        file_as_xml = f.read()
        file_as_dict = xmltodict.parse(file_as_xml)
        list_of_file_data.append(json.dumps(file_as_dict))

# Write Dataframe to parquet and then tarball to compress file size for export
df = pd.DataFrame(list_of_file_data)
df.columns = ["Data"]
df.to_parquet(parq_file_path)

# Compress with tarball - Select the correct file path
# Chicago Tribune 2022
#!tar -czvf data/chicago_tribune_2022.tar.gz data/chicago_tribune_2022.parquet

# Chicago Tribune 2023
#!tar -czvf data/chicago_tribune_2023.tar.gz data/chicago_tribune_2023.parquet

# Chicago Tribune Final Week
#!tar -czvf data/chicago_tribune_final.tar.gz data/chicago_tribune_final.parquet

# Crain Business
#!tar -czvf data/crain.tar.gz data/crain.parquet

# Calculate final file size (to stay within Proquest file size limit)
file_size = os.path.getsize(tz_file_path)
print(f"Size of file: {file_size/1000000} MB")

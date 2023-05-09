import os
import json
import re

filename = "houza_uae_2023_04_04.json" 
file_size = os.path.getsize(filename)
file_type = filename.split(".")
file_type=file_type[-1].upper()

pattern = r"\d{4}_\d{2}_\d{2}"
with open(filename, 'r') as f:
    l = f.readlines()

with open(filename, 'r') as f:

    for line in f:
        data = json.loads(line)
    
        iteration_number = data.get("iteration_number")
        if re.match(pattern, iteration_number):
            a="success"
        else:
            a="fail"
            break
    

data_count = len(l)  
info = {
    "filename": filename,
    "size": f"{file_size/1000} KB",
    "data count": data_count,
    "file Type": file_type,
    "iteration_number": a
}

file_details = {"Info": info}

with open('file_details.json', 'w') as f:
    json.dump(file_details, f, indent=2)


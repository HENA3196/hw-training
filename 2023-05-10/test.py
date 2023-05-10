import os
import json
import re

iteration_flg="success"
date_flag="success"
scraped_flag="success"
published_flag="success"

filename = "/home/hena/QA/houza/houza_uae_2023_04_04.json" 
file_size = os.path.getsize(filename)
file_type = filename.split(".")
file_type=file_type[-1].upper()

pattern = r"\d{4}_\d{2}_\d{2}"
pattern_2=r"\d{4}-\d{2}-\d{2}"

with open(filename, 'r') as f:
    l = f.readlines()

with open(filename, 'r') as f:

    for line in f:
        data = json.loads(line)
    
        iteration_number = data.get("iteration_number")
        if re.match(pattern, iteration_number):
            pass
        else:
            iteration_flg="fail"
    
        date = data.get("date")
        if re.match(pattern_2, date):
           pass
        else:
            date_flag="fail"

        scraped = data.get("scraped_ts")
        if re.match(pattern_2, scraped):
           pass
        else:
            scraped_flag="fail"  


        published_at = data.get("published_at")
        if re.match(pattern_2, published_at):
           pass
        else:
            published_flag="fail"    
    
published_at
data_count = len(l)  
info = {
    "filename": filename,
    "size": f"{file_size/1000} KB",
    "data count": data_count,
    "file Type": file_type,
    "iteration_number": iteration_flg,
    "date":date_flag,
    "scraped_ts":scraped_flag,
    "published_at":published_flag
}

file_details = {"Info": info}

print(file_details)

with open('file_details.json', 'w') as f:
    json.dump(file_details, f, indent=2)


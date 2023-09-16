import json
import os
from collections import Counter

def generate_report(json_lines):
    report = {}

    for json_line in json_lines:
        data = json.loads(json_line)
        
        for field, value in data.items():
            
            if field not in report:
                report[field] = [value]

            else:
                report[field].append(value)
    

    return report


    

json_file_path = input("Enter the file path : ")


with open(json_file_path, 'r') as json_file:
    json_lines = json_file.readlines()
    

report = generate_report(json_lines)

folder_name = json_file_path.split('.')[0]+'_report'

if not os.path.exists(folder_name):
        os.makedirs(folder_name)


for field, values in report.items():
     
    value_count = (Counter(values)) 
    sortvalue=sorted(value_count.items()) 

   
    

    distinct_value_count = len(value_count) 
   

    field_file_name = os.path.join(folder_name, f"{field}.txt") 

    with open(field_file_name, 'w') as report_file:  
        report_file.write(f"{field} (Distinct Values: {distinct_value_count}):\n")
        for value, count in sortvalue:
            report_file.write(f"- {value} (Count: {count})\n")

print("===============Reports generated==========")

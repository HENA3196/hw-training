import os
import json
import re

iteration_flg="success"
date_flag="success"
scraped_flag="success"
empty_field="true"
boolean_field="True"
category_field="true"
subcategory_field="true"
completion_status_field="true"
package_type_field="true"
price_per_field="true"
furnished_field="true"
error_list=[]
Error={}

filename = "bayut_uae_2023_05_01.json" 
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

data_count = len(l)  




with open(filename, 'r') as f:
    for line_num, line in enumerate(f, 1):
        data = json.loads(line)

        expected_order = [
            "reference_number",
            'id',
            'url',
            'broker_display_name',
            'broker',
            'category',
            'category_url',
            'title',
            'description',
            'location',
            'price',
            'currency',
            'price_per',
            'bedrooms',
            'bathrooms',
            'furnished',
            'rera_permit_number',
            'dtcm_licence',
            'scraped_ts',
            'amenities',
            'details',
            'agent_name',
            'number_of_photos',
            'user_id',
            'phone_number',
            'date',
            'iteration_number',
            'rera_registration_number',
            'ded_license_number',
            'rera_length',
            'latitude',
            'longitude',
            'listing_id',
            'package_type',
            'locality',
            'object_id',
            'completion_status',
            'ad_type',
            'verified',
            'sub_category_1',
            'sub_category_2',
            'property_type',
            'depth',
            'published_at',
            'listing_availability'
        ]

        dict_keys = iter(data.keys())
        Header_Order = "correct"

        for key in expected_order:
            if key != next(dict_keys, ''):
                Header_Order = "INCORRECT"

        for key in ['dtcm_licence', 'depth', 'sub_category_2', 'ad_type']:
            value = data.get(key, '')
            if value != '':

                error_list.append(f"The key '{key}' is not empty in line {line_num} ")
                empty_field="false"


        for key in ['listing_availability', 'rera_length']:
            value = data.get(key)
            if not isinstance(value, bool):
                boolean_field = "false"

                error_list.append(f"The key '{key}' is not boolean in line {line_num} ")

                


       


        category_value = data.get('category')
        if category_value !='rent' and category_value!= 'sale':

            category_field="false"
            # Error.update({category_value:{}""})
            error_list.append(f"The 'category' value '{category_value}' in line {line_num}")


        subcategory_1=data.get("sub_category_1")
        if subcategory_1 !="Commercial" and  subcategory_1 != "Residential":
            subcategory_field="false"
            error_list.append(f"The 'subcategory_1' value '{subcategory_1}' in line {line_num} ")


        completion_status=data.get("completion_status")  
        if completion_status !="off-plan" and  completion_status !="ready" and completion_status !="rent":
            completion_status_field="false"
            error_list.append(f"The 'completion_status' value '{completion_status}' in line {line_num} ")



        package_type=data.get("package_type")   
        if package_type !="free" and  package_type !="hot" and package_type !="premium" and package_type!="superhot":
            package_type_field="false"
            error_list.append(f"The package_type value '{package_type}' in line {line_num} is invalid.")


        price_per=data.get("price_per")   
        if price_per !="Daily" and  price_per !="Weekly" and price_per !="Monthly" and price_per!="Yearly" and price_per!="":
            price_per_field="false"
            error_list.append(f"The package_type value '{price_per}' in line {line_num} is invalid.")


        furnished=data.get("furnished")
        if furnished !="Unfurnished" and  furnished != "Furnished" and furnished!="":
            furnished_field="false"
            error_list.append(f"The furnished value '{furnished}' in line {line_num} is invalid.")

        verified=data.get("verified") 
        if verified !="Checked" and  verified != "TruCheckTM" and verified!="":
            furnished_field="false"
            error_list.append(f"The verified value '{furnished}' in line {line_num} is invalid.")


# ===============================================================================================

        for key in ['reference_number', 'id','url','broker_display_name','broker','category_url','title','description','location','price','currency','bedrooms','bathrooms','rera_permit_number','amenities','details','agent_name','number_of_photos','user_id','phone_number','rera_registratio','ded_license_number','latitude','longitude','listing_id','locality','object_id','ad_type','property_type']:
            value = data.get(key, '')
            if value == '':

                error_list.append(f"The key '{key}' is empty in line {line_num} ")
                

Error={"error": error_list}
req={"empty":empty_field,"boolean":boolean_field,"category_value":category_field,"subcategory_1":subcategory_field,"completion_status":completion_status_field,"package_type":package_type_field, "price_per":price_per_field,"furnished":furnished_field}

info = {
    "filename": filename,
    "size": f"{file_size/1000} KB",
    "data count": data_count,
    "file Type": file_type,
    "scraped_ts":scraped_flag,
    "iteration_number": iteration_flg,
    "date": date_flag,
    "Header_Order": Header_Order,
    "req":req,
    "Error":Error

}

file_details = {"Info": info}

print(file_details)

with open('file_details.json', 'w') as f:
    json.dump(file_details, f, indent=2)

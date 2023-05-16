import os
import json
import re
import random

def file(filename):

    iteration_flg="success"
    date_flag="success"
    scraped_flag="success"
    Header_Order = "Correct"
    all_data = []
    error_list=[]


    file_size = os.path.getsize(filename)
    file_type = filename.split(".")
    file_type=file_type[-1].upper()

    pattern = r"\d{4}_\d{2}_\d{2}"
    pattern_2=r"\d{4}-\d{2}-\d{2}"

    with open(filename, 'r') as f:
        l = f.readlines()
        data_count = len(l)  
        for line_num, line in enumerate(l, 1):
            
                data = json.loads(line)
                all_data.append(data)
            
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

                for key in expected_order:
                    if key != next(dict_keys, ''):
                        Header_Order = "Incorrect"
            
           
    req,error_list=requirements(l)
    random_data=randomdata(all_data)

    info = {"filename": filename,
            "size": f"{file_size/1000} KB",
            "data count": data_count,
            "file Type": file_type,
            "scraped_ts":scraped_flag,
            "iteration_number": iteration_flg,
            "date": date_flag,
            "Header_Order": Header_Order,
            "requirements": req,
            "Error":error_list,
            "randomdata":random_data 
            }
    return info            


def requirements(l):
    error_list=[]    
    empty_field="true"
    boolean_field="true"
    category_field="true"
    subcategory_field="true"
    completion_status_field="true"
    package_type_field="true"
    price_per_field="true"
    furnished_field="true"
    verified_field="true"


    for line_num, line in enumerate(l, 1):
        
            data = json.loads(line)
            for key, value in data.items():
                if value == "None" or value=="null":
                    error_list.append(f"The key '{key}' in line {line_num} has a value of None or null")
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
                error_list.append(f"The 'category' value '{category_value}' in line {line_num}")


            subcategory_1=data.get("sub_category_1")
            if subcategory_1 !="Commercial" and  subcategory_1 != "Residential":
                subcategory_field="false"
                error_list.append(f"The 'subcategory_1' value '{subcategory_1}' in line {line_num} ")


            completion_status=data.get("completion_status")  
            if completion_status !="off-plan" and  completion_status !="ready" and completion_status !="rent" and completion_status!="" :
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
                verified_field="false"
                error_list.append(f"The verified value '{verified}' in line {line_num} is invalid.")

      
    requirements={"empty":empty_field,"boolean":boolean_field,"category_value":category_field,"subcategory_1":subcategory_field,"completion_status":completion_status_field,"package_type":package_type_field, "price_per":price_per_field,"furnished":furnished_field, "verified":verified_field}
    return(requirements,error_list)
    


def randomdata(all_data):   
    random_data_list=[]

    random_10_data = random.sample(all_data, k=10)

    for data in random_10_data:
     
        reference_number = data.get("reference_number")
        id_ = data.get("id")
        url=data.get("url")
        broker_display_name=data.get('broker_display_name')
        broker=data.get('broker')
        category_url=data.get("category_url")
        title=data.get("title")
        description=data.get("description")
        location=data.get("location")
        price=data.get("price")
        currency=data.get("currency")
        bedrooms=data.get("bedrooms")
        bathrooms=data.get("bathrooms")
        rera_permit_number=data.get("rera_permit_number")
        amenities=data.get("amenities")
        details=data.get("details")
        agent_name=data.get("agent_name")
        number_of_photos=data.get("number_of_photos")
        user_id=data.get("user_id")
        phone_number=data.get("phone_number")
        rera_registration_number=data.get("rera_registration_number")
        ded_license_number=data.get("ded_license_number")
        latitude=data.get("latitude")
        longitude=data.get("longitude")
        listing_id=data.get("listing_id")
        locality=data.get("locality")
        object_id=data.get("object_id")
        property_type=data.get("property_type")
        published_at=data.get("published_at")


        random_data={"reference_number":reference_number,
                       "id_":id_ ,
                       "url":url,
                       "broker_display_name":broker_display_name,
                       "broker":broker,
                       "category_url":category_url,
                       "title":title,
                       "description":description,
                       "location":location,
                       "price":price,
                       "currency":currency,
                       "bedrooms":bedrooms,
                       "bathrooms":bathrooms,
                       "rera_permit_number":rera_permit_number,
                       "amenities":amenities,
                       "details":details,
                       "agent_name":agent_name,
                       "number_of_photos":number_of_photos,
                       "user_id":user_id,
                       "phone_number":phone_number,
                       "rera_registration_number":rera_registration_number,
                       "ded_license_number":ded_license_number,
                       "latitude":latitude,
                       "longitude":longitude,
                       "listing_id":listing_id,
                       "locality":locality,
                       "object_id":object_id,
                       "property_type":property_type,
                       "published_at":published_at
                       }

        random_data_list.append(random_data)
    return random_data_list


 
file_name=input("Enter file name: ")
details= file(file_name)
with open('Out.json', 'w') as f:
    json.dump(details, f, indent=2)





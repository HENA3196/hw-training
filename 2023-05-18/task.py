import os
import json
import re
import random
from urllib.parse import urlparse
import datetime

global error_list
global file_info
error_list = []
file_info = {}

def header():
    current_date = datetime.date.today()
    current_year = current_date.year
    current_month = current_date.month
    first_day = datetime.date(current_year, current_month, 1)
    days_passed = (current_date - first_day).days
    current_week = (days_passed // 7) + 1
    current_month = str(current_month).zfill(2)
    current_week = str(current_week).zfill(2)
    file_format = f"{current_year}_{current_month}_{current_week}.json"
    
    return file_format

def bayut(filename):
    pattern_publish = r"\b\d{1,2}\s+[a-zA-Z]+\s+\d{4}\b"
    pattern = r"\d{4}_\d{2}_\d{2}"
    pattern_2 = r"\d{4}-\d{2}-\d{2}"
    pattern_lat = r"^\d{2}(\.\d+)?$"

    file_name_flag = "true"
    empty_field = "true"
    published_at_flag = "true"
    url_flag = "success"
    iteration_flg = "true"
    date_flag = "true"
    scraped_flag = "true"
    longitude_flag = "true"
    latitude_flag = "true"

    file_format = header()
    file_format = f"bayut_uae_{file_format}"
    file_name = os.path.basename(filename)

    if file_name == file_format:
        pass
    else:
        file_name_flag = "false"

    with open(filename, 'r') as f:
        file = f.readlines()
        
        for line_num, line in enumerate(file, 1):
            data = json.loads(line)

            iteration_number = data.get("iteration_number")
            if re.fullmatch(pattern, iteration_number):
                pass
            else:
                iteration_flg = "false"

            date = data.get("date")
            if re.fullmatch(pattern_2, date):
                pass
            else:
                date_flag = "false"

            scraped = data.get("scraped_ts")
            if re.fullmatch(pattern_2, scraped):
                pass
            else:
                scraped_flag = "false"

            currency=data.get("currency")
            if currency!="AED" and currency !='':
            	error_list.append(f"currency{currency} error in {lin}")


            latitude = data.get("latitude")
            if re.fullmatch(pattern_lat, latitude):
                pass
            else:
                error_list.append(f"The latitude '{latitude}' error in line {line_num} ")
                latitude_flag = "false"

            longitude = data.get("longitude")
            if re.fullmatch(pattern_lat, longitude):
                pass
            else:
                error_list.append(f"The longitude '{longitude}' error  in line {line_num} ")
                longitude_flag = "false"

            for key in ['dtcm_licence', 'depth', 'sub_category_2', 'ad_type']:
                value = data.get(key, '')
                if value != '':
                    error_list.append(f"The key '{key}' is not empty in line {line_num} ")
                    empty_field = "false"

            url = data.get("url")
            parsed_url = urlparse(url)
            base_url = parsed_url.scheme + "://" + parsed_url.netloc
            if base_url != "https://www.bayut.com":
                url_flag = "fail"
                error_list.append(f"The url '{url}' error  in line {line_num} ")

            published_at = data.get("published_at")
            if re.fullmatch(pattern_publish, published_at):
                pass
            else:
                published_at_flag = "false" 
                error_list.append(f"published_at {published_at} error in line {line_num}")

    file_info = {
        "file_name": file_name_flag,
        "iteration_number": iteration_flg,
        "scraped_ts": scraped_flag,
        "date": date_flag,
        "latitude": latitude_flag,
        "longitude": longitude_flag,
        "empty_field": empty_field, 
        "url": url_flag, 
        "published_at": published_at_flag, 
        "Error": error_list
    }

    return file_info

def houza(filename):
    file_name_flag = "true"
    empty_field = "true"
    published_at_flag = "true"
    url_flag = "true"
    iteration_flg = "true"
    date_flag = "true"
    scraped_flag = "true"
    longitude_flag = "true"
    latitude_flag = "true"

    pattern_publish = r"\d{4}-\d{2}-\d{2}"
    pattern = r"\d{4}_\d{2}_\d{2}"
    pattern_2 = r"\d{4}-\d{2}-\d{2}"
    pattern_lat = r"^\d{2}(\.\d+)?$"

    # check header
    file_format = header()
    file_format = f"houza_uae_{file_format}"
    file_name = os.path.basename(filename)
    if file_name == file_format:
        pass
    else:
        file_name_flag = "false"

    with open(filename, 'r') as f:
        file = f.readlines()
        data_count = len(file)

        for line_num, line in enumerate(file, 1):
            data = json.loads(line)

            iteration_number = data.get("iteration_number")
            if re.fullmatch(pattern, iteration_number):
                pass
            else:
                iteration_flg = "false"

            date = data.get("date")
            if re.fullmatch(pattern_2, date):
                pass
            else:
                date_flag = "false"

            scraped = data.get("scraped_ts")
            if re.fullmatch(pattern_2, scraped):
                pass
            else:
                scraped_flag = "false"

            currency = data.get('currency')
            if currency != "AED" and currency != '':
                error_list.append(f"error currency {currency} line {line_num}")

            latitude = data.get("latitude")
            if latitude == '':
                pass
            elif re.fullmatch(pattern_lat, latitude):
                pass
            else:
                error_list.append(f"The latitude '{latitude}' error in line {line_num} ")
                latitude_flag = "false"

            longitude = data.get("longitude")
            if longitude == '':
                pass
            elif re.fullmatch(pattern_lat, longitude):
                pass
            else:
                error_list.append(f"The longitude '{longitude}' error in line {line_num} ")
                longitude_flag = "false"

            for key in ['dtcm_licence', 'depth']:
                value = data.get(key, '')
                if value != '':
                    error_list.append(f"The key '{key}' is not empty in line {line_num} ")
                    empty_field = "false"

            url = data.get("url")
            parsed_url = urlparse(url)
            base_url = parsed_url.scheme + "://" + parsed_url.netloc
            if base_url != "https://houza.com":
                url_flag = "false"
                error_list.append(f"The url '{url}' error in line {line_num} ")

            published_at = data.get("published_at")
            if re.fullmatch(pattern_publish, published_at):
                pass
            else:
                published_at_flag = "false" 
                error_list.append(f"published_at {published_at} error in line {line_num}")

        file_info.update({
            "empty_field": empty_field, 
            "url": url_flag,
            "published_at": published_at_flag, 
            "Error": error_list,
            "file_name": file_name_flag,
            "iteration_number": iteration_flg,
            "scraped_ts": scraped_flag,
            "date": date_flag,
            "latitude": latitude_flag,
            "longitude": longitude_flag
        })

    return file_info


def dubizzle(filename):
    file_name_flag = "true"
    empty_field = "true"
    published_at_flag = "true"
    iteration_flg = "true"
    date_flag = "true"
    scraped_flag = "true"
    longitude_flag = "true"
    latitude_flag = "true"
    pattern = r"\d{4}_\d{2}_\d{2}"
    pattern_2 = r"\d{4}-\d{2}-\d{2}"
    pattern_lat = r"^\d{2}(\.\d+)?$"
    pattern_publish = r"\d{4}-\d{2}-\d{2}"

    file_format = header()
    file_format = f"dubizzel_uae_{file_format}"
    file_name = os.path.basename(filename)
    if file_name == file_format:
        pass
    else:
        file_name_flag = "false"

    with open(filename, 'r') as f:
        file = f.readlines()
        data_count = len(file)

        for line_num, line in enumerate(file, 1):
            data = json.loads(line)

            iteration_number = data.get("iteration_number")
            if re.fullmatch(pattern, iteration_number):
                pass
            else:
                iteration_flg = "false"

            date = data.get("date")
            if re.fullmatch(pattern_2, date):
                pass
            else:
                date_flag = "false"

            scraped = data.get("scraped_ts")
            if re.fullmatch(pattern_2, scraped):
                pass
            else:
                scraped_flag = "false"

            latitude = data.get("latitude")
            if latitude=='':
            	pass
            elif re.fullmatch(pattern_lat, latitude):
                pass
            else:
                error_list.append(f"The latitude '{latitude}' error in line {line_num} ")
                latitude_flag = "false"

            longitude = data.get("longitude")
            if longitude=='':
            	pass
            elif re.fullmatch(pattern_lat, longitude):
                pass
            else:
                error_list.append(f"The longitude '{longitude}' error in line {line_num} ")
                longitude_flag = "false"

            for key in ['dtcm_licence', 'agent_name', "user_id"]:
                value = data.get(key, '')
                if value != '':
                    error_list.append(f"The key '{key}' is not empty in line {line_num} ")
                    empty_field = "false"

            published_at = data.get("published_at")
            if re.fullmatch(pattern_publish, published_at):
                pass
            else:
                published_at_flag = "false" 
                error_list.append(f"published_at {published_at} error in line {line_num}")

            currency=data.get("currency")
            if currency!='' and currency!="AED":
            	error_list.append(f"error currency{currency} line no{line_num}")


        file_info.update({
            "file_name": file_name_flag,
            "iteration_number": iteration_flg,
            "scraped_ts": scraped_flag,
            "date": date_flag,
            "latitude": latitude_flag,
            "longitude": longitude_flag,
            "empty_field": empty_field,
            "published_at": published_at_flag,
            "Error": error_list
        })
                  
    return file_info


def aqarmap(filename):
    file_name_flag = "true"
    empty_field = "true"
    published_at_flag = "true"
    url_flag = "true"
    iteration_flg = "true"
    date_flag = "true"
    scraped_flag = "true"
    longitude_flag = "true"
    latitude_flag = "true"

    pattern_publish = r"\d{4}-\d{2}-\d{2}"
    pattern = r"\d{4}_\d{2}_\d{2}"
    pattern_2 = r"\d{4}-\d{2}-\d{2}"
    pattern_lat = r"^\d{2}(\.\d+)?$"

    file_format = header()
    file_format = f"aqarmap_egp_{file_format}"
    file_name = os.path.basename(filename)
    print(file_format,filename)

    if file_name == file_format:
        pass
    else:
        file_name_flag = "false"

    with open(filename, 'r') as f:
        file = f.readlines()
        data_count = len(file)

        for line_num, line in enumerate(file, 1):
            data = json.loads(line)

            iteration_number = data.get("iteration_number")
            if re.fullmatch(pattern, iteration_number):
                pass
            else:
                iteration_flg = "false"

            date = data.get("date")
            if re.fullmatch(pattern_2, date):
                pass
            else:
                date_flag = "false"

            scraped = data.get("scraped_ts")
            if re.fullmatch(pattern_2, scraped):
                pass
            else:
                scraped_flag = "false"

            latitude = data.get("latitude")
            if latitude=='':
            	pass
            elif re.fullmatch(pattern_lat, latitude):
                pass
            else:
                error_list.append(f"The latitude '{latitude}' error in line {line_num} ")
                latitude_flag = "false"

            longitude = data.get("longitude")
            if longitude=='':
            	pass
            elif re.fullmatch(pattern_lat, longitude):
                pass
            else:
                error_list.append(f"The longitude '{longitude}' error in line {line_num} ")
                longitude_flag = "false"

            for key in ['price_per', 'reference_number', 'furnished', 'rera_permit_number', 'amenities', 'verified', 'dtcm_licence', 'agent_name']:
                value = data.get(key, '')
                if value != '':
                    error_list.append(f"The key '{key}' is not empty in line {line_num} ")
                    empty_field = "false"

            url = data.get("url")
            parsed_url = urlparse(url)
            base_url = parsed_url.scheme + "://" + parsed_url.netloc
            if base_url != "https://aqarmap.com.eg":
                url_flag = "false"
                error_list.append(f"The url '{url}' error in line {line_num} ")

            published_at = data.get("published_at")
            if re.fullmatch(pattern_publish, published_at):
                pass
            else:
                published_at_flag = "false" 
                error_list.append(f"published_at {published_at} error in line {line_num}")

            currency=data.get("currency")
            if currency!='' and currency !='EGP':
            	error_list.append(f"error{currency} at line no: {line_num}")

            file_info.update({
                "file_name": file_name_flag,
                "iteration_number": iteration_flg,
                "scraped_ts": scraped_flag,
                "date": date_flag,
                "latitude": latitude_flag,
                "longitude": longitude_flag,
                "empty_field": empty_field,
                "url": url_flag,
                "published_at": published_at_flag,
                "Error": error_list
            })

        return file_info




def dari(filename):
    file_name_flag = "true"
    empty_field = "true"
    license_start_flag = "true"
    license_end_flag = 'true'
    url_flag = "true"
    pattern_license = r"\d{4}-\d{2}-\d{2}"
    iteration_flg = "true"
    date_flag = "true"
    scraped_flag = "true"
    longitude_flag = "true"
    latitude_flag = "true"

    pattern = r"\d{4}_\d{2}_\d{2}"
    pattern_2 = r"\d{4}-\d{2}-\d{2}"
    pattern_lat = r"^\d{2}(\.\d+)?$"
   

    file_format = header()
    file_format = f"dari_ae_{file_format}"
    file_name = os.path.basename(filename)
    if file_name == file_format:
        pass
    else:
        file_name_flag = "false"

    file_info.update({})

    with open(filename, 'r') as f:
        file = f.readlines()
        data_count = len(file)

        for line_num, line in enumerate(file, 1):
            data = json.loads(line)

            iteration_number = data.get("iteration_number")
            if re.fullmatch(pattern, iteration_number):
                pass
            else:
                iteration_flg = "false"

            scraped = data.get("scraped_ts")
            if re.fullmatch(pattern_2, scraped):
                pass
            else:
                scraped_flag = "false"

            for key in ['dtcm_licence', 'depth']:
                value = data.get(key, '')
                if value != '':
                    error_list.append(f"The key '{key}' is not empty in line {line_num} ")
                    empty_field = "false"

            license_start = data.get("license_start_date")
            if re.fullmatch(pattern_license, license_start):
                pass
            else:
                license_start_flag = "false"
                error_list.append(f"The key '{license_start}' is not empty in line {line_num} ")

            license_end = data.get("license_end_date")
            if re.fullmatch(pattern_license, license_end):
                pass
            else:
                license_end_flag = "false"
                error_list.append(f"The key '{license_end}' is not empty in line {line_num} ")

            url = data.get("url")
            parsed_url = urlparse(url)
            base_url = parsed_url.scheme + "://" + parsed_url.netloc
            if base_url != "https://www.dari.ae":
                url_flag = "false"
                error_list.append(f"The url '{url}' error in line {line_num} ")

           
            file_info.update({
                "file_name": file_name_flag,
                "iteration_number": iteration_flg,
                "scraped_ts": scraped_flag,
                "empty_field": empty_field,
                "url": url_flag,               
                "license_start":license_start_flag,
                "license_end":license_end_flag,
                "Error": error_list
            })

    return file_info


def olx(filename):
    file_name_flag = "true"
    empty_field = "true"
    published_at_flag = "true"
    url_flag = "true"
    iteration_flg = "true"
    date_flag = "true"
    scraped_flag = "true"
   

    pattern = r"\d{4}_\d{2}_\d{2}"
    pattern_2 = r"\d{4}-\d{2}-\d{2}"
    pattern_lat = r"^\d{2}(\.\d+)?$"
    pattern_publish = r"\d{4}-\d{2}-\d{2}"
    file_format = header()
    file_format = f"olx_egp_{file_format}"
    file_name = os.path.basename(filename)
    if file_name == file_format:
        pass
    else:
        file_name_flag = "false"

    error_list = []

    with open(filename, 'r') as f:
        file = f.readlines()
        data_count = len(file)

        for line_num, line in enumerate(file, 1):
            data = json.loads(line)

            iteration_number = data.get("iteration_number")
            if re.fullmatch(pattern, iteration_number):
                pass
            else:
                iteration_flg = "false"

            date = data.get("date")
            if re.fullmatch(pattern_2, date):
                pass
            else:
                date_flag = "false"

            scraped = data.get("scraped_ts")
            if re.fullmatch(pattern_2, scraped):
                pass
            else:
                scraped_flag = "false"

            url = data.get("url")
            parsed_url = urlparse(url)
            base_url = parsed_url.scheme + "://" + parsed_url.netloc
            if base_url != "https://www.olx.com.eg":
                url_flag = "false"
                error_list.append(f"The url '{url}' error in line {line_num}")

            published_at = data.get("published_at")
            if re.fullmatch(pattern_publish, published_at):
                pass
            else:
                published_at_flag = "false"
                error_list.append(f"published_at {published_at} error in line {line_num}")

            currency=data.get("currency")
            if currency!="EGP" and currency!='':
            	error_list.append(f"currency error line no{line_num}")

    file_info.update({
        "file_name": file_name_flag,
        "iteration_number": iteration_flg,
        "scraped_ts": scraped_flag,
        "date": date_flag,
        "url": url_flag,
        "published_at": published_at_flag,
        "Error": error_list
    })

    return file_info




def write_file(final_out):
    with open('Out.json', 'w') as f:
        json.dump(final_out, f, indent=2)


full_path = input("enter full path: ")
site = int(input("Enter site:\n 1-bayut, 2-houza, 3-dubizzle 4-aqarmap, 5-dari, 6-olx"))

if site == 1:
    final_out = bayut(full_path)
    write_file(final_out)
elif site==2:
	final_out=houza(full_path)
	write_file(final_out)
elif site==3:
	final_out=dubizzle(full_path)
	write_file(final_out)
elif site==4:
	final_out=aqarmap(full_path)
	write_file(final_out)
elif site==5:
	final_out=dari(full_path)
	write_file(final_out)
elif site==6:
	final_out=olx(full_path)
	write_file(final_out)



print(final_out)
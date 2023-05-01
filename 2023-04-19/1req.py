import requests
# import json



# r = requests.get("https://www.example.com")

# print(response.text)
# print(r.status_code)

# r= requests.put('https://httpbin.org/put', data={'key': 'value'})
# print(r)
# r = requests.delete('https://httpbin.org/delete')
# print(r)
# r = requests.head('https://httpbin.org/get')
# print(r)
# r = requests.options('https://httpbin.org/get')
# print(r)

# GET METHOD
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# r.status_code
# print(r.encoding)
# print(r.text)
# print(r.json())
# print(r.headers)



# POST METHOD
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})

# PASSING PARAMETERS In URLs
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url)

# Response Content
# r = requests.get('https://api.github.com/events')
# print(r.text)
 
# RAW RESPONSE CONTENT
# r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw)
# print(r.raw.read(10))


# SAVE TO JSON FILE
# with open('req.json', 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)
# with open('req.json', 'r') as f:  #load json data to python object
#     data = json.load(f)

# with open('req.json', 'w') as f:
#     json.dump(data, f, indent=4) #tdubmp write json back and add indent


# RESPONSE STATUS CODE
# r = requests.get('https://httpbin.org/get')
# print(r.status_code)

# COOKIES
# url = 'https://httpbin.org/cookies'
# r = requests.get(url)

# if 'example_cookie_name' in r.cookies:
#     cookie_value = r.cookies['example_cookie_name']
#     print(cookie_value)
# else:
# 	print('Cookie not found')

# url = 'https://httpbin.org/cookies'
# cookies = dict(cookies_are='working')

# r = requests.get(url, cookies=cookies)
# print(r.text)
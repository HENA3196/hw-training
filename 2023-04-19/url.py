import urllib.request


url = "https://www.example.com" # Define the URL to fetch
response = urllib.request.urlopen(url)
html = response.read().decode() # Make the HTTP request and get the response
print(html)

with urllib.request.urlopen('https://www.example.com') as response:
   html = response.read()

print(html)


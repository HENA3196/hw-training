import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)
if x:
  print("YES! We have a match!")
else:
  print("No match")

# from selenium import webdriver

# # Launch the browser driver
# driver = webdriver.Chrome()

# # Navigate to a webpage
# driver.get("https://www.google.com")

# # Find an element on the webpage and interact with it
# search_box = driver.find_element(By.NAME, "q")
 # search_box.send_keys("Selenium tutorial")
# search_box.submit()

# # Close the browser
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()        #https://sites.google.com/chromium.org/driver/  ""web drivr is an api""
driver.get("http://www.python.org")
assert "Python" in driver.title      #checks that the word "Python" is present in the title of the current web page. If it is not present, the code will stop and raise an AssertionError.
elem = driver.find_element(By.NAME, "q") #finds the search box on the web page by its name "q" using the find_element method from the driver object.
elem.clear()      #clears any pre-existing text in the search box.
elem.send_keys("pycon") #search pycon
elem.send_keys(Keys.RETURN)#presses the Enter key to submit the search query.
assert "No results found." not in driver.page_source
driver.close()


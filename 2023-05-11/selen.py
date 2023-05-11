from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.homerealestate.com/?p=agentResults.asp")
element = driver.find_element(By.XPATH,'//div[@class="rn-agent-icon-website"]/a')  
href = element.get_attribute("href")
print(href)

driver.quit()


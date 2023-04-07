# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options

# def browser_function():
#     driver_path = r"C:\Program Files (x86)\msedgedriver.exe"
#     chr_options = Options()
#     chr_options.add_experimental_option("detach", True)
#     chr_driver = webdriver.Edge(service=Service(executable_path=driver_path), options=chr_options)
#     chr_driver.get("https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx")
#     # button=chr_driver.find_element_by_class("joinWaitList")
#     # button.Click()
# browser_function()




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service

# set the driver path for your browser (in this case, Edge)
driver_path = 'C:\Program Files (x86)\msedgedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)

# open Bing
driver.get('https://www.bing.com/')

# wait for the AI chat icon to appear and click it
chat_icon = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'BingNP')))
chat_icon.click()

# switch to the AI chat iframe and wait for the chat to load
link_element = driver.find_element_by_xpath("link_element = driver.find_element_by_xpath('//a[@id='my-link']")
link_url = link_element.get_attribute('href')
print(link_url)
# full_url= "https://www.bing.com"+ link_url
# driver.get(full_url)

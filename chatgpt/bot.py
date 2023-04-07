from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/Program Files (x86)/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.reddit.com/")

wait = WebDriverWait(driver, 10)
reddit_logo = wait.until(EC.presence_of_element_located((By.ID, "header-img")))

# Do something with the page, e.g. print the page title
print(driver.title)

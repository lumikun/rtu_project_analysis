import time 
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.select import Select


url = "http://fiawec.alkamelsystems.com/?season=11_2022"
links = []
driver = webdriver.Firefox()
driver.get(url)
select_element = driver.find_element(By.NAME, 'season')
select = Select(select_element)
options_list = select.options 
select.select_by_visible_text("2024")
select_element = driver.find_element(By.NAME, "evvent")
select = Select(select_element)
select.select_by_visible_text("LE MANS")
found = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[3]/table/tbody/tr/td/div[2]/div[17]/a")
found.click()



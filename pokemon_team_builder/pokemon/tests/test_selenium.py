#test the functionality of my pokemon application
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://127.0.0.1:8000")

pokemon_nav_button = driver.find_element(By.LINK_TEXT, "POKEMON")
if (pokemon_nav_button.text == "POKEMON"):
    pokemon_nav_button.click()

time.sleep(1)

bulbasaur_button = driver.find_element(By.XPATH, "/html/body/div/ul[1]/li/a")
if bulbasaur_button:
    bulbasaur_button.click()

time.sleep(3)

home_button = driver.find_element(By.LINK_TEXT, "HOME")
if (home_button.text == "HOME"):
    home_button.click()
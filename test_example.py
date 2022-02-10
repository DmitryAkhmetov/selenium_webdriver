from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_ex():
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    WebDriverWait(driver, 10).until(EC.title_is("Google"))
    driver.quit()
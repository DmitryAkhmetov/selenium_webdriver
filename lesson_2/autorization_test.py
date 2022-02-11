import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return driver

def test_ex(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.CSS_SELECTOR, 'input[type="text" i]').send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, 'input[type="password" i]').send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
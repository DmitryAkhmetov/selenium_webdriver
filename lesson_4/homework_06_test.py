import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
    wait = WebDriverWait(driver, 20)
    box_apps_menu = wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, '#app-'))
    for i in range (len(box_apps_menu)):
        box_apps_menu = driver.find_elements(By.CSS_SELECTOR, '#app-')
        box_apps_menu[i].click()
        driver.find_element(By.CSS_SELECTOR, 'h1')
        docs_li = driver.find_elements(By.XPATH, '//*[@id="app-"]/ul/li')
        if docs_li is not None:
            for a in range(len(docs_li)):
                docs_li = driver.find_elements(By.XPATH, '//*[@id="app-"]/ul/li')
                docs_li[a].click()
                driver.find_element(By.CSS_SELECTOR, 'h1')
        else:
            pass
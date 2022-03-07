import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return driver

def test_ex(driver):
    driver.get("http://localhost/litecart/")
    wait = WebDriverWait(driver, 20)
    product_group = ('#box-most-popular', '#box-campaigns', '#box-latest-products')
    for a in product_group:
        box_most_popular =  wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, str(a) + ' > div > ul > li'))
        elem = len(box_most_popular)
        for i in range(1, elem + 1):
            sticker = driver.find_elements(By.CSS_SELECTOR, str(a) + ' > div > ul > li:nth-child(' + str(i) + ') > a.link > div.image-wrapper > div')
            if len(sticker) == 1:
                pass
            else:
                assert False
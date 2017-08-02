import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("https://dev2-etp.roseltorg.ru")
    #time.sleep(10)
    driver.find_element_by_name("login").send_keys("sanek545")
    driver.find_element_by_name("password").send_keys("1234567")
    driver.find_element_by_xpath("//button[text()='Вход в систему']").click()
    time.sleep(10)

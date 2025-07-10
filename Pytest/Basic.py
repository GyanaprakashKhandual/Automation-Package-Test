import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    # Automatically handles downloading and using the correct ChromeDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_search_box_visible(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    assert search_box.is_displayed()

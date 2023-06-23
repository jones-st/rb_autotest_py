from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def common_setup():
    # Create a WebDriver instance for Chrome
    driver = webdriver.Chrome()
    # Preconditions
    driver.maximize_window()
    driver.get("https://www.redbull.com/")
    driver.implicitly_wait(5)
    cookie = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    cookie.click()
    # Return the WebDriver instance to make it available to the tests
    return driver


@pytest.fixture()
def enter_profile(common_setup):
    driver = common_setup
    login_icon = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div/div/div/'
                                               'header/div[1]/div[2]/div/div')
    login_icon.click()
    driver.implicitly_wait(5)
    email_input = driver.find_element(By.ID, 'email')
    email_input.click()
    email_input.send_keys("joneszauber@gmail.com")
    driver.implicitly_wait(5)
    submit_email_button = driver.find_element(By.XPATH, '//*[@id="lightbox"]/div[2]/div[2]/form/button')
    submit_email_button.click()
    pass_input = driver.find_element(By.ID, 'lb-password')
    pass_input.click()
    pass_input.send_keys("testing")
    driver.implicitly_wait(5)
    submit_button = driver.find_element(By.XPATH, '//*[@id="lightbox"]/div[2]/div[2]/form/button')
    submit_button.click()
    driver.implicitly_wait(5)
    return driver
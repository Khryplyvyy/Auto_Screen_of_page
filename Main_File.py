from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyautogui

driver = webdriver.Chrome()

#(1) open main page
def test_open_main_google_page():
    URL = 'https://www.google.com/'
    driver.get(URL)
    return

#(2) configurate window size and window
def test_set_window_size_position():
    driver.set_window_size(1720, 856)
    driver.set_window_position(0, 0)

#(3) put our text into Google search line
def test_send_keys_into_google_search_line():
    text = driver.find_element(By.XPATH,
                               '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    text.send_keys('Automation testing')
    return

#(4) click on search button
def test_click_on_google_search_button():
    search_button = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", search_button)
    driver.execute_script("arguments[0].click();", search_button)
    return

#(5) make a screenshot of second page
def make_screen():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'D:\Python_3\AQA_OOP\second_page.jpg')
    return

try:
    #1)
    test_open_main_google_page()
    #2)
    test_set_window_size_position()
    #3)
    test_send_keys_into_google_search_line()
    #4)
    test_click_on_google_search_button()
    #5)
    make_screen()

finally:
    time.sleep(5)
    driver.quit()
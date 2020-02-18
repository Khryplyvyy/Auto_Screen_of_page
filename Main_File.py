from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyautogui

driver = webdriver.Chrome()
###################################################################
#........................TEST CASE 1..............................#
###################################################################
#(1) open main page
def test_open_main_google_page():
    URL = 'https://www.google.com/'
    driver.get(URL)


#(2) configurate window size and window position
def test_set_window_size_position():
    driver.set_window_size(1720, 856)
    driver.set_window_position(0, 0)

#(3) put our text into Google search line
def test_send_keys_into_google_search_line():
    text = driver.find_element(By.XPATH,
                               '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    text.send_keys('Automation testing')


#(4) click on search button
def test_click_on_google_search_button():
    search_button = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", search_button)
    driver.execute_script("arguments[0].click();", search_button)


#(5) cheking text into google searchline
def test_assert():
    value = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input')
    value_text = value.get_attribute('value')  # seek element with "Automation testing" text
    assert value_text == 'Automation testing', 'Fully matching is required'


#(6) make a screenshot of second page
def test_make_screen():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'D:\Python_3\AQA_OOP\Auto_Screen_of_page\second_page.jpg')


try:
#class is added for import possibility these function in future
    class General:
        #1)
        test_open_main_google_page()
        #2)
        test_set_window_size_position()
        #3)
        test_send_keys_into_google_search_line()
        #4)
        test_click_on_google_search_button()
        #5)assertion_test
        test_assert()
        #6)
        test_make_screen()


finally:
    time.sleep(5)
    driver.quit()


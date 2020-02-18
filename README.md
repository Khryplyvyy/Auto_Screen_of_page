# Auto_Screen_of_page
 Making a page screenshot by using Selenium WebDriver and Python

An ease automation test script to open some web pages and send any keys to a text line of your browser. The feature of this script is a screenshot that will be saved on your local machine after a new browser window will be opened. The shot will be available when the test session expired.

Used modules and libraries:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pyautogui

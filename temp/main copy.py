import time
import datetime

import pandas as pd
import numpy as np

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions 
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from bs4 import BeautifulSoup

options = ChromeOptions()
options.add_argument("user-data-dir=C:/Users/Tamang/AppData/Local/Google/Chrome/User Data")
options.add_argument("profile-directory=Profile 1")

service = Service(executable_path=r'C:/path/to/chromedriver.exe')

driver = Chrome(service=service, options=options)
driver.get("https://www.google.com")
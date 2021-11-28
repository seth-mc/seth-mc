from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# enter geckodriver path here:
geckodriver_path = ''

d = os.getcwd()
os.chdir(d)
products = pd.read_excel('allproducts.xlsx')
hts = pd.read_csv('htsdata.csv', header=0)



class DataBot(object):

    def __init__(self, items):
        self.products = products
        self.hts = hts
        self.items = items

        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        self.driver = webdriver.Firefox(executable_path=geckodriver_path,
                                        firefox_profile=self.profile,
                                        firefox_options=self.options)
        self.driver.get(self.racky_url)

    def search_items(self):
        urls = []
        prices = []
        names = []
        for item in self.items:
            print(f"Searching for {item}.")

            self.driver.get(self.racky_url)

            search_input = self.driver.find_element_by_id(
                "dgwt-wcas-search-input-1")
            search_input.click()
            search_input.send_keys(item)

            time.sleep(5)

            search_button = self.driver.find_element_by_xpath(
                '/html/body/div[11]/a')
            search_button.click()


items = ['10455']
racky_bot = DataBot(items)
racky_bot.search_items()

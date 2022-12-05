from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python

#driver.get("https://www.google.com")
#driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get('https://beautiful-soup-4.readthedocs.io/en/latest/')

page_soup = BeautifulSoup(driver.page_source, 'lxml') #'html.parser'?

#p_list = page_soup.find_all("p")
#print(p_list)
#page_soup_2 = BeautifulSoup(driver.page_source, 'lxml') #'html.parser'?
#h_list = page_soup.find_all("h1")
#print(h_list)

print(page_soup.get_text())

#stripped_strings


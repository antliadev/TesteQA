from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://www.flyinf.com.br')
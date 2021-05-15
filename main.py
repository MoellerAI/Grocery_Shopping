from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.nemlig.com/'
driver = webdriver.Chrome('/home/mads/Downloads/chromedriver')
driver.get(url)
driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[text()='OK']").click()


groceries = ['tomat', 'agurk', 'løg']

for element in groceries:
    driver.get(f'https://www.nemlig.com/?sortorder=price&search={element}')
    driver.implicitly_wait(2)
    driver.find_element_by_class_name('addtobasket__btn').click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from HelloFresh import HelloFreshIngredients

helloF = HelloFreshIngredients()
groceries = helloF.get_ingredients('https://www.hellofresh.dk/recipes/dild-og-citronpaneret-torsk-608905cd5666714e3261065f')

url = 'https://www.nemlig.com/'
driver = webdriver.Chrome('/home/mads/Downloads/chromedriver')
driver.get(url)
driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[text()='OK']").click()

for element in groceries:
    try:
        driver.get(f'https://www.nemlig.com/?sortorder=price&search={element}')
        driver.implicitly_wait(2)
        driver.find_element_by_class_name('addtobasket__btn').click()
        driver.implicitly_wait(1)
    except:
        print(element)
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/home/mads/Downloads/chromedriver')

url = 'https://www.hellofresh.dk/recipes/'
driver.get(url)
driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[text()='Accept All Cookies']").click()

url = "https://www.hellofresh.dk/recipes/sprod-bbq-kylling-608168b13d429f7be126e67a"

driver.get(url)
driver.implicitly_wait(4)
html = driver.page_source
soup = BeautifulSoup(html)

table = soup.find_all('div', {'class': 'fela-_1qz307e'})
ingredients = []

for ingredient in table:
    ingredients.append(ingredient.find_all('p'))

for ingredient in ingredients:
    print(ingredient[1].get_text())
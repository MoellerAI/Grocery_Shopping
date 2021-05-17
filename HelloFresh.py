from socket import SO_BROADCAST
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class HelloFreshIngredients:
    def __init__(self):
        self.driver = webdriver.Chrome('/home/mads/Downloads/chromedriver')
        self.ingredients = []

    
    def start_page(self):
        url = 'https://www.hellofresh.dk/recipes/'
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//button[text()='Accept All Cookies']").click()

    def get_ingredients(self, url):
        self.start_page()

        self.driver.get(url)
        self.driver.implicitly_wait(4)
        html = self.driver.page_source
        soup = BeautifulSoup(html)
        table = soup.find_all('div', {'class': 'fela-_1qz307e'})
        ingredients = []
        groceries = []
        ammount = []
        

        for ingredient in table:
            ingredients.append(ingredient.find_all('p'))

        for ingredient in ingredients:
            groceries.append(ingredient[1].get_text())
            ammount.append(ingredient[1].get_text())

        self.driver.quit()
        
        return groceries
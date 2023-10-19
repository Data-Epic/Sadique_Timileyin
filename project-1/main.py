import logging
import gspread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os, json
from dotenv import load_dotenv, find_dotenv
load_dotenv()
KEY = json.loads(os.getenv("PROJECT_1202"))


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "https://www.food.com/ideas/top-comfort-food-recipes-6929#c-791290"
driver.get(url=link)

gc = gspread.service_account(KEY)


def open_spreadsheet(sheet_name):
    """
    This opens a spreadsheet already created on Google sheet
    """
    sh = gc.open(sheet_name)
    logging.info("spreadsheet opened")

    def select_spreadsheet(s_name):
        """
        This function  selects the preferred worksheet
        :param s_name: This is the name of the desired worksheet in str format
        """
        worksheet = sh.worksheet(s_name)
        return worksheet
    return select_spreadsheet


def create_spreadsheet(sheet_name):
    """
    This creates a new spreadsheet file in google sheet
    """
    sh = gc.create(sheet_name)
    logging.info("Spreadsheet created")

    def select_spreadsheet(s_name):
        """
        This function  selects the preferred worksheet
        :param s_name: This is the name of the desired worksheet in str format
        """
        worksheet = sh.worksheet(s_name)
        return worksheet
    return select_spreadsheet


def spreadsheet_format(worksheet, col1, col2):
    """
    This functon is for the formatting of the spreadsheet
    :param worksheet: This  accepts a function
    :param col1: This is the name of the start column in the range in str format
    :param col2: This is the name of the end column in the range in str format
    """
    worksheet.format(f"{col1}:{col2}", {'textFormat': {'bold': True}})


# This section provides the names of the meals
names = driver.find_elements(By.TAG_NAME, value='h2')
meals = []
for name in names:
    meals.append(name.text)

# This section provides the links to the recipe
links = driver.find_elements(By.CSS_SELECTOR, value='h2 a')
recipe = []
for link in links:
    recipe.append(link.get_attribute('href'))

spreadsheet = open_spreadsheet("project 1202")
spreadsheet("sheet1")
spreadsheet_format(spreadsheet("sheet1"), "A1", "B1")
spreadsheet("sheet1").update("A1", "Name")
spreadsheet("sheet1").update("B1", "Recipe")
# manual updating
spreadsheet("sheet1").update("A2:B22",
                             [[meals[0], recipe[0]], [meals[1], recipe[1]], [meals[2], recipe[2]],
                              [meals[3], recipe[3]], [meals[4], recipe[4]], [meals[5], recipe[5]],
                              [meals[6], recipe[6]], [meals[7], recipe[7]], [meals[8], recipe[8]],
                              [meals[9], recipe[9]], [meals[10], recipe[10]], [meals[11], recipe[11]],
                              [meals[12], recipe[12]], [meals[13], recipe[13]], [meals[14], recipe[14]],
                              [meals[15], recipe[15]], [meals[16], recipe[16]], [meals[17], recipe[17]],
                              [meals[18], recipe[18]], [meals[19], recipe[19]], [meals[20], recipe[20]]])

# # Automated updating
num = 1
for linked in recipe:
    driver.get(linked)
    num += 1
    recipe_link = linked
    spreadsheet("sheet1").update(f'B{num}', recipe_link)
    logging.info("Worksheet updated")
    meal = driver.find_element(By.TAG_NAME, value="h1").text
    spreadsheet("sheet1").update(f'A{num}', meal)
    logging.info("Worksheet updated")

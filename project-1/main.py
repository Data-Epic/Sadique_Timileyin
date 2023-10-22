import logging
import gspread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import os, json
from dotenv import load_dotenv
load_dotenv()
KEY = os.getenv("PROJECT_1202")
option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
link = "https://www.lusha.com/company-search/accounting/10/canada/193/page/2/"
driver.get(url=link)

gc = gspread.service_account("sadique_timileyin/project-1/my-project.json")


def open_spreadsheet(sheet_name):
    """
    This opens a spreadsheet already created on Google sheet
    """
    sh = gc.open(sheet_name)
    logging.info("spreadsheet opened")
    return sh


def create_spreadsheet(sheet_name):
    """
    This creates a new spreadsheet file in google sheet
    """
    sh = gc.create(sheet_name)
    logging.info("Spreadsheet created")
    return sh


def select_spreadsheet(filename, s_name):
    """
    This function  selects the preferred worksheet
    :param filename:
    :param s_name: This is the name of the desired worksheet in str format
    """
    worksheets = open_spreadsheet(filename).worksheet(s_name)
    return worksheets


def spreadsheet_format(worksheet, col1, col2):
    """
    This functon is for the formatting of the spreadsheet
    :param worksheet: This  accepts a function
    :param col1: This is the name of the start column in the range in str format
    :param col2: This is the name of the end column in the range in str format
    """
    worksheet.format(f"{col1}:{col2}", {'textFormat': {'bold': True}})


def new_worksheet(filename, new_name, rows, cols):
    """
    This function creates a new worksheet within the spreadsheet.
    :param filename: This is the name of the spreadsheet file
    :param new_name: Name of  the new worksheet
    :param rows: Numbers of desired rows
    :param cols: Numbers of desired columns
    :return: A new worksheet
    """
    open_spreadsheet(filename).add_worksheet(new_name, rows, cols)
    logging.info("Worksheet created")


open_spreadsheet("project 1202")
worksheet = select_spreadsheet(filename="project 1202", s_name="Sheet1")
spreadsheet_format(worksheet, "A1", "C1")
worksheet.clear()
worksheet.update("A1", "Company Name")
worksheet.update("B1", "Company Link")
worksheet.update("B1", "Company LinkedIn")

num = 1
linked = []
links = driver.find_elements(By.CSS_SELECTOR, value='.directory-content-box-inner a')
for link in links:
    linked.append(link.get_attribute('href'))
for links in linked:
    num += 1
    driver.get(links)
    company_name = None
    while not company_name:
        try:
            txt = driver.find_element(By.TAG_NAME, value='h1')
            company_name = txt.text
        except NoSuchElementException:
            company_name = "None"
    print(company_name)
    company_link = None
    while not company_link:
        try:
            linke = driver.find_element(By.XPATH, value='/html/body/main/div[1]/div/section[1]/div/div[1]'
                                                        '/div/div[2]/a')
            company_link = linke.get_attribute('href')
        except NoSuchElementException:
            company_link = "None"
    print(company_link)

    linkedin = None
    while not linkedin:
        try:
            texts = driver.find_element(By.CSS_SELECTOR, value='.company-details-socials a')
            linkedin = texts.get_attribute('href')
        except NoSuchElementException:
            linkedin = "None"
    print(linkedin)

    worksheet.update(f"A{num}", company_name)
    worksheet.update(f"B{num}", company_link)
    worksheet.update(f"C{num}", linkedin)


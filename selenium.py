from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Run in background

driver = webdriver.Firefox(service=Service(
    GeckoDriverManager().install()), options=options)
driver.get("https://www.boot.dev/lessons/c465d09d-b53a-4276-978c-cc2c9f4e02ad")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

for a in soup.find_all("a"):
    print(a.get("href"))

driver.quit()

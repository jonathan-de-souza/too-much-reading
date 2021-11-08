from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
goodreadsImportExporPage = driver.get("https://www.goodreads.com/review/import");
print("goodreadsImportExportPage")
print(goodreadsImportExporPage)
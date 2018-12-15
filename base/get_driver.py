from selenium import webdriver
def get_driver():
    driver=webdriver.Firefox()

    driver.get("http://localhost/index.php")
    driver.maximize_window()
    return driver

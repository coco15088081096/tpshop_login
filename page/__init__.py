"""以下为page_tpshop_login的元素定位"""
from selenium.webdriver.common.by import By

loc_login_btn=By.XPATH,"//*[@class='red']"
loc_username=By.ID,"username"
loc_password=By.ID,"password"
loc_code=By.ID,"verify_code"
loc_submit=By.CLASS_NAME,"J-login-submit"
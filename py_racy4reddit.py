from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get(f"https://old.reddit.com/")
actions = ActionChains(driver)
# take username
#username = input("Reddit Username:")
username = "yourusernamehere"
user_field = driver.find_element_by_name("user")
user_field.send_keys(username)
# take password
#password = input("Reddit Password:")
password = "yourpasswordhere"
pass_field = driver.find_element_by_name("passwd")
pass_field.send_keys(password)
# press login
button = driver.find_element_by_class_name("btn")
button.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

l = driver.find_element_by_link_text(username)
l.click()
# # go to id =siteTable
sitetable = driver.find_element_by_id("siteTable")
c = sitetable.text
while c != "":

    # delete = driver.find_elements_by_link_text("delete")
    # v = driver.find_elements_by_link_text("yes")
    # for d in delete:
    #     d.click()
    #     for y in v:
    #         y.click()
    # press delete
    try:
        delete = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "delete"))
        )
        delete.click()
    except:
        driver.quit()
    try:
        v = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "yes"))
        )
        v.click()
    except:
        driver.quit()

    driver.refresh()
    # for y in v:
    #     y.click()
    # driver.implicitly_wait(10)

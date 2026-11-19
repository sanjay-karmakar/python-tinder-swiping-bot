from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/FXZ5RJxop7Qg7oG-fX0qCy_BGB_Er-zB"
FACEBARK_EMAIL = ""
FACEBARK_PASSWORD = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.get(TINDOG_URL)

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(1)
facebark_button = driver.find_element(By.CLASS_NAME, value='btn-facebark')
facebark_button.click()


# Switch to the Facebark popup window
sleep(2)
base_window = driver.window_handles[0]
facebark_window = driver.window_handles[1]
driver.switch_to.window(facebark_window)
print(driver.title)  # "Facebark"

# Fill in the form and submit
email = driver.find_element(By.ID, value='email')
password = driver.find_element(By.ID, value='pass')
email.send_keys(FACEBARK_EMAIL)
password.send_keys(FACEBARK_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to the Tindog window
sleep(2)
driver.switch_to.window(base_window)
print(driver.title)  # "Tindog" or "Tindog | Paw Right™"


# More code above - this is at the end of the previous solution
# Allow location
sleep(2)
allow_location = driver.find_element(By.XPATH, value='//button[text()="Allow"]')
allow_location.click()

# Not interested in notifications
sleep(1)
not_interested = driver.find_element(By.XPATH, value='//button[text()="Not interested"]')
not_interested.click()

# Accept cookies
sleep(1)
accept_cookies = driver.find_element(By.XPATH, value='//button[text()="I Accept"]')
accept_cookies.click()
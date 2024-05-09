import requests
import cv2
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import numpy as np
import time

# Function to click option by word
def click_option_by_word(driver, word):
    options_mapping = {
        "Jobseeker": "30782",
        "Student": "23134510",
        "NO students": "13713913",
        "NBoE 2024": "34896877",
         "family": "13713939",
        "Sondertermin, Special appointment": "23369141"
    }
    option_value = options_mapping.get(word)
    if option_value:
        select_calendar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'CalendarId')))
        driver.execute_script("arguments[0].value = '{}';".format(option_value), select_calendar)
    else:
        print("Word '{}' not found in options mapping.".format(word))


# Function to preprocess the image for better OCR accuracy
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh

# Function to read captcha using OCR
def read_captcha_image(image_url):
    response = requests.get(image_url)
    image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
    preprocessed_image = preprocess_image(image)
    captcha_text = pytesseract.image_to_string(preprocessed_image, config='--psm 6 outputbase digits')
    return captcha_text.strip()




def book_appointment():
    # Initialize the WebDriver with headless mode option
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(options=options)




def click_next_week(driver):
    next_week_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next week']")))
    next_week_button.click()

def has_available_time(driver):
    try:
        return driver.find_element(By.XPATH, "//input[@name='Start']").is_displayed()
    except:
        return False



# Function to click on the "Week before" button
def click_week_before(driver):
    click_week_before = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Week before']")))
    click_week_before.click()

# Function to select the first available time slot
def select_time_slot(driver):
    driver.find_element(By.XPATH, "//input[@name='Start']").click()

#   def click_first_available_time():
#         while True:
#             # Get the page source
#             page_source = driver.page_source
#             # Parse the HTML
#             soup = BeautifulSoup(page_source, 'html.parser')
#             # Find all td tags that contain dates and time slots
#             date_td_tags = soup.find_all('td')
#             # Check for the target date
#             for td in date_td_tags:
#                 date_string = td.text.strip()
#                 print(date_string)
                
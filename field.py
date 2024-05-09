

# # import requests
# # from PIL import Image
# # import pytesseract
# # from io import BytesIO
# # import numpy as np
# # import cv2
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time

# # # Function to preprocess the image for better OCR accuracy
# # def preprocess_image(image):
# #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# #     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# #     thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
# #     return thresh

# # # Function to read captcha using OCR
# # def read_captcha_image(image_url):
# #     response = requests.get(image_url)
# #     image = np.asarray(bytearray(response.content), dtype="uint8")
# #     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
# #     preprocessed_image = preprocess_image(image)
# #     captcha_text = pytesseract.image_to_string(preprocessed_image, config='--psm 6 outputbase digits')
# #     return captcha_text.strip()

# # # Initialize the WebDriver with headless mode option
# # options = webdriver.ChromeOptions()
# # options.headless = False
# # driver = webdriver.Chrome(options=options)

# # # Open the webpage
# # driver.get('https://appointment.bmeia.gv.at')

# # # Fill out the form and navigate through the steps
# # select_office = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'Office')))
# # select_office.send_keys('teheran')

# # next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
# # next_button.click()




# # def click_option_by_word(driver, word):
# #     options_mapping = {
# #         "Jobseeker": "30782",
# #         "students ": "23134510",
# #         "NO students": "13713913",
# #         "NBoE 2024": "34896877",
# #         "family": "13713939",
# #         "Sondertermin, Special appointment": "23369141"
# #     }

# #     option_value = options_mapping.get()
# #     if option_value:
# #         select_calendar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'CalendarId')))
# #         driver.execute_script("arguments[0].value = '{}';".format(option_value), select_calendar)
# #     else:
# #         print("Word '{}' not found in options mapping.".format(word))

# # # select_calendar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'CalendarId')))   ##this is for Sondertermin, Special appointment
# # # driver.execute_script("arguments[0].value = '23369141';", select_calendar)

# # # while True:
# # for _ in range(3):  # Click "Next" button three times
# #     next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
# #     next_button.click()

# # # Choose date and time
# # date_time_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='Start']")))
# # date_time_option.click()

# # next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
# # next_button.click()


# # # Select gender
# # select_gender = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'Sex')))
# # select_gender.send_keys('Female')

# # # Autofill form fields
# # driver.execute_script("""
# #         document.getElementById('Lastname').value = 'REZAEI';
# #         document.getElementById('Firstname').value = 'REZA';
# #         document.getElementById('DateOfBirth').value = '07/25/1974';
# #         document.getElementById('TraveldocumentNumber').value = 'Z00000000';
# #         document.getElementById('Street').value = 'BOSTAN,HAFEZ,FARHANG.ST , SARI';
# #         document.getElementById('Postcode').value = '4818846733';
# #         document.getElementById('City').value = 'SARI';
# #         document.getElementById('Country').value = '3'; // Afghanistan
# #         document.getElementById('Telephone').value = '989112585031';
# #         document.getElementById('Email').value = 'canlmKissyou@gmail.com';
# #         document.getElementById('LastnameAtBirth').value = 'ATEFEH';
# #         document.getElementById('NationalityAtBirth').value = '1'; // Afghanistan
# #         document.getElementById('CountryOfBirth').value = '1'; // Afghanistan
# #         document.getElementById('PlaceOfBirth').value = 'SARI';
# #         document.getElementById('NationalityForApplication').value = '1'; // Afghanistan
# #         document.getElementById('TraveldocumentDateOfIssue').value = '01/23/2023';
# #         document.getElementById('TraveldocumentValidUntil').value = '01/23/2028';
# #         document.getElementById('TraveldocumentIssuingAuthority').value = '1'; // Afghanistan
# #     """)

# #     # Click the GDPR acceptance checkbox
# # checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'DSGVOAccepted')))
# # checkbox.click()
# # while True:
# #     # Read and enter captcha text
# #     captcha_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, '/Captcha?')]")))
# #     captcha_img_url = captcha_img.get_attribute("src")
# #     captcha_text = read_captcha_image(captcha_img_url)

# #     captcha_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'CaptchaText')))
# #     captcha_input.clear()
# #     captcha_input.send_keys(captcha_text)

# #     # Click "Next" button
# #     next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextButton')))
# #     next_button.click()

# #     # Check if successfully navigated to the next page
# #     if "appointmentconfirmation" in driver.current_url:
# #         print("Successfully booked appointment!")
# #         break
# #     else:
# #         print("Failed to book appointment. Retrying...")
# #         driver.refresh()  # Refresh the page and try again

# # # Add a delay to see the process
# # time.sleep(10)

# # # Close the browser window
# # driver.quit()
# # # 

# # import requests
# # from PIL import Image
# # import pytesseract
# # from io import BytesIO
# # import numpy as np
# # import cv2
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# # from allFild import click_option_by_word 


# # # Function to preprocess the image for better OCR accuracy
# # def preprocess_image(image):
# #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# #     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# #     thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
# #     return thresh

# # # Function to read captcha using OCR
# # def read_captcha_image(image_url):
# #     response = requests.get(image_url)
# #     image = np.asarray(bytearray(response.content), dtype="uint8")
# #     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
# #     preprocessed_image = preprocess_image(image)
# #     captcha_text = pytesseract.image_to_string(preprocessed_image, config='--psm 6 outputbase digits')
# #     return captcha_text.strip()



# # # Initialize the WebDriver with headless mode option
# # options = webdriver.ChromeOptions()
# # options.headless = False
# # driver = webdriver.Chrome(options=options)

# # # Open the webpage
# # driver.get('https://appointment.bmeia.gv.at')

# # # Fill out the form and navigate through the steps
# # select_office = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'Office')))
# # select_office.send_keys('teheran')

# # next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
# # next_button.click()



# # # Call the click_option_by_word function with a word from the options_mapping
# # word_to_click = "Sondertermin, Special appointment"
# # option_id = click_option_by_word(driver, word_to_click)

# # # Use the obtained option_id to interact with the webpage
# # if option_id:
# #     select_calendar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'CalendarId')))
# #     driver.execute_script("arguments[0].value = '{}';".format(option_id), select_calendar)


# # for _ in range(3):  # Click "Next" button three times
# #     next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
# #     next_button.click()

# # # Choose date and time
# # date_time_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='Start']")))
# # date_time_option.click()

# # next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
# # next_button.click()


# # # Select gender
# # # select_gender = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'Sex')))
# # # select_gender.send_keys('Female')

# # # Autofill form fields
# # driver.execute_script("""
# #         document.getElementById('Lastname').value = 'REZAEI';
# #         document.getElementById('Firstname').value = 'REZA';
# #         document.getElementById('DateOfBirth').value = '07/25/1974';
# #         document.getElementById('TraveldocumentNumber').value = 'Z00000000';
# #         document.getElementById('Sex').value = '2';
# #         document.getElementById('Street').value = 'BOSTAN,HAFEZ,FARHANG.ST , SARI';
# #         document.getElementById('Postcode').value = '4818846733';
# #         document.getElementById('City').value = 'SARI';
# #         document.getElementById('Country').value = '3'; // Afghanistan
# #         document.getElementById('Telephone').value = '989112585031';
# #         document.getElementById('Email').value = 'canlmKissyou@gmail.com';
# #         document.getElementById('LastnameAtBirth').value = 'ATEFEH';
# #         document.getElementById('NationalityAtBirth').value = '1'; // Afghanistan
# #         document.getElementById('CountryOfBirth').value = '1'; // Afghanistan
# #         document.getElementById('PlaceOfBirth').value = 'SARI';
# #         document.getElementById('NationalityForApplication').value = '1'; // Afghanistan
# #         document.getElementById('TraveldocumentDateOfIssue').value = '01/23/2023';
# #         document.getElementById('TraveldocumentValidUntil').value = '01/23/2028';
# #         document.getElementById('TraveldocumentIssuingAuthority').value = '1'; // Afghanistan
# #     """)

# # # Click the GDPR acceptance checkbox
# # # checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'DSGVOAccepted')))
# # # checkbox.click()
# # while True:
# #     # Read and enter captcha text
# #     captcha_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, '/Captcha?')]")))
# #     captcha_img_url = captcha_img.get_attribute("src")
# #     captcha_text = read_captcha_image(captcha_img_url)

# #     captcha_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'CaptchaText')))
# #     captcha_input.clear()
# #     captcha_input.send_keys(captcha_text)

# #     # Click "Next" button
# #     next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextButton')))
# #     next_button.click()

# #     # Check if successfully navigated to the next page
# #     if "appointmentconfirmation" in driver.current_url:
# #         print("Successfully booked appointment!")
# #     else:
# #         print("Failed to book appointment.")

# # # Add a delay to see the process
# # time.sleep(10)

# # # Close the browser window
# # driver.quit()



# from datetime import datetime
# import datetime
# import time
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time as delay_time

# from allField import *
# import datetime

# # Initialize the WebDriver with headless mode option
# options = webdriver.ChromeOptions()
# options.headless = False
# driver = webdriver.Chrome(options=options)

# try:
#     # Open the webpage
#     driver.get('https://appointment.bmeia.gv.at')
#     time.sleep(2)
#     # Fill out the form and navigate through the steps
#     select_office = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'Office')))
#     select_office.send_keys('teheran')

#     next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
#     next_button.click()
#     time.sleep(2)
#     # Call the click_option_by_word function with a word from the options_mapping
#     word_to_click = "Sondertermin, Special appointment"
#     option_id = click_option_by_word(driver, word_to_click)
#     time.sleep(2)
#     # Use the obtained option_id to interact with the webpage
#     if option_id:
#         select_calendar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'CalendarId')))
#         driver.execute_script("arguments[0].value = '{}';".format(option_id), select_calendar)

#     for _ in range(3):  # Click "Next" button three times
#         next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
#         next_button.click()
#     time.sleep(2)
#     # Choose date and time
        

#     # Define the date range to check for free time
#     target_date = datetime.datetime(2024, 6, 24).date()
#     end_date = datetime.datetime(2024, 7, 31).date()
#     formatted_date = target_date.strftime("%m/%d/%b")
#     formatted_date = end_date.strftime("%m/%d/%b")
    

#     def parse_date_time(label):
#         datetime_str = label["for"].split("_")[1]
#         date_str, time_str = datetime_str.split(" ")[0], datetime_str.split(" ")[1]
#         date = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
#         time = datetime.datetime.strptime(time_str, "%H:%M:%S").time()
#         return date, time
    

  
#     next_week_clicks = 0
#     # Loop to check for available time slots
    
#     true = True

#     while true:
#         # Parse the HTML
#         soup = BeautifulSoup(driver.page_source, "html.parser")
#         # Find all label tags
#         label_tags = soup.find_all("label")
#         # Check availability for each date
#         for label in label_tags:
#             date, time = parse_date_time(label)
#             if date == target_date:
#                 # Click on the corresponding radio button
#                 radio_input_id = label["for"]
#                 radio_input = driver.find_element(By.ID, radio_input_id)
#                 radio_input.click()
#                 true = False
#                 # Optionally, you can break here if you only want to select the first available slot
#                 break
#         else:
#             # Try navigating to the next week
#             try:
#                 next_week_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next week']")))
#                 next_week_button.click()
#                 next_week_clicks += 1
#                 delay_time.sleep(3)  # Delay after clicking "Next week"
#             except:
#                 # Check if next_week_clicks is not zero
#                 if next_week_clicks != 0:
#                     # If next_week_clicks is not zero, go back to the previous week
#                     for _ in range(next_week_clicks):
#                         week_before_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Week before']")))
#                         week_before_button.click()
#                         delay_time.sleep(3)  # Delay after clicking "Week before"
#                     next_week_clicks = 0  # Reset next_week_clicks
                    
                    
#                 if next_week_clicks is None or next_week_clicks == 0:
#                     week_before_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Week before']")))
#                     week_before_button.click()
#                     delay_time.sleep(4)


#                 else:
#                     print("No further weeks available.")
#                   # Delay after loading each page
    
#     true = True
#     next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
#     next_button.click()
#     # time.sleep(2)
#     # Autofill form fields
#     driver.execute_script("""
#         document.getElementById('Lastname').value = 'REZAEI';
#         document.getElementById('Firstname').value = 'REZA';
#         document.getElementById('DateOfBirth').value = '07/25/1974';
#         document.getElementById('TraveldocumentNumber').value = 'Z11110990';
#         document.getElementById('Sex').value = '2';
#         document.getElementById('Street').value = 'BOSTAN,HAFEZ,FARHANG.ST , SARI';
#         document.getElementById('Postcode').value = '4818846733';
#         document.getElementById('City').value = 'SARI';
#         document.getElementById('Country').value = '102'; // Afghanistan
#         document.getElementById('Telephone').value = '989112585031';
#         document.getElementById('Email').value = 'EASYVISA990@GMAIL.COM';
#         document.getElementById('LastnameAtBirth').value = 'ATEFEH';
#         document.getElementById('NationalityAtBirth').value = '111'; // Afghanistan
#         document.getElementById('CountryOfBirth').value = '111'; // Afghanistan
#         document.getElementById('PlaceOfBirth').value = 'SARI';
#         document.getElementById('NationalityForApplication').value = '111'; // Afghanistan
#         document.getElementById('TraveldocumentDateOfIssue').value = '01/23/2023';
#         document.getElementById('TraveldocumentValidUntil').value = '01/23/2028';
#         document.getElementById('TraveldocumentIssuingAuthority').value = '111'; // Afghanistan
#     """)

#     delay_time.sleep(4)

#     # Click the GDPR acceptance checkbox
#     # checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'DSGVOAccepted')))
#     # checkbox.click()

#     while true:
       
#         # Read and enter captcha text
#         captcha_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, '/Captcha?')]")))
#         captcha_img_url = captcha_img.get_attribute("src")
#         captcha_text = read_captcha_image(captcha_img_url)

#         captcha_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'CaptchaText')))
#         captcha_input.clear()
#         captcha_input.send_keys(captcha_text)


#         # Check if successfully navigated to the next page
#         if "appointmentconfirmation" in driver.current_url:
#             print("Successfully booked appointment!")
#             true = False
#             break
#         else:
#             print("Failed to book appointment. Retrying...")
#             delay_time.sleep(1.5)
#             driver.refresh()  # Refresh the page and try again
            
            
#     delay_time.sleep(15)
# finally:
#     # Close the browser window
#     driver.quit()






from datetime import datetime
import datetime
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as delay_time

from allField import *
import datetime

# Initialize the WebDriver with headless mode option
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)

try:
    # Open the webpage
    driver.get('https://appointment.bmeia.gv.at')
    time.sleep(2)
    # Fill out the form and navigate through the steps
    select_office = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'Office')))
    select_office.send_keys('teheran')

    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
    next_button.click()
    time.sleep(2)
    # Call the click_option_by_word function with a word from the options_mapping
    word_to_click = "Sondertermin, Special appointment"
    option_id = click_option_by_word(driver, word_to_click)
    time.sleep(2)
    # Use the obtained option_id to interact with the webpage
    if option_id:
        select_calendar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'CalendarId')))
        driver.execute_script("arguments[0].value = '{}';".format(option_id), select_calendar)

    for _ in range(3):  # Click "Next" button three times
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
        next_button.click()
    time.sleep(2)
    # Choose date and time
        

    # Define the date range to check for free time
    target_date = datetime.datetime(2024, 6, 30).date()
    end_date = datetime.datetime(2024, 7, 5).date()
    formatted_date = target_date.strftime("%m/%d/%b")
    formatted_date = end_date.strftime("%m/%d/%b")
    

    def parse_date_time(label):
        datetime_str = label["for"].split("_")[1]
        date_str, time_str = datetime_str.split(" ")[0], datetime_str.split(" ")[1]
        date = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
        time = datetime.datetime.strptime(time_str, "%H:%M:%S").time()
        return date, time
    

  
    next_week_clicks = 0
    before_week_clicks = 0
    # Loop to check for available time slots
    
    true = True

    while true:
        # Parse the HTML
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # Find all label tags
        label_tags = soup.find_all("label")
        # Check availability for each date
        for label in label_tags:
            date, time = parse_date_time(label)
            print(date)
            if date == target_date or date == end_date or date >=target_date and date <= end_date  :
                # Click on the corresponding radio button
                radio_input_id = label["for"]
                radio_input = driver.find_element(By.ID, radio_input_id)
                radio_input.click()
                true = False
                # Optionally, you can break here if you only want to select the first available slot
                break
        else:
            # Try navigating to the next week
            try:
                next_week_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next week']")))
                next_week_button.click()
                next_week_clicks += 1
                delay_time.sleep(3)  # Delay after clicking "Next week"
            except:
                # Check if next_week_clicks is not zero
                if next_week_clicks != 0:
                    # If next_week_clicks is not zero, go back to the previous week
                    for _ in range(next_week_clicks):
                        
                        week_before_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Week before']")))
                        week_before_button.click()
                        delay_time.sleep(3)  # Delay after clicking "Week before"
                        next_week_clicks = 0  # Reset next_week_clicks

                if next_week_clicks is None or next_week_clicks == 0:
                    week_before_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Week before']")))
                    week_before_button.click()
                    before_week_clicks += 1
                    delay_time.sleep(2)

                if before_week_clicks == 4:
                    back_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Back']")))
                    back_button.click()
                    before_week_clicks = 0
                    
                    delay_time.sleep(2)
                    for _ in range(2):
                        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
                        next_button.click()
                        delay_time.sleep(2)

                    print("No further weeks available.")
        delay_time.sleep(2)  # Delay after loading each page
    
    true = True
   
        
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
    next_button.click()


    # Select gender
    select_gender = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'Sex')))
    select_gender.send_keys('Female')

    # Autofill form fields
    driver.execute_script("""
            document.getElementById('Lastname').value = 'REZAEI';
            document.getElementById('Firstname').value = 'REZA';
            document.getElementById('DateOfBirth').value = '07/25/1974';
            document.getElementById('TraveldocumentNumber').value = 'Z11110990';
            document.getElementById('Sex').value = '2';
            document.getElementById('Street').value = 'BOSTAN,HAFEZ,FARHANG.ST , SARI';
            document.getElementById('Postcode').value = '4818846733';
            document.getElementById('City').value = 'SARI';
            document.getElementById('Country').value = '102'; // Afghanistan
            document.getElementById('Telephone').value = '989112585031';
            document.getElementById('Email').value = 'EASYVISA990@GMAIL.COM';
            document.getElementById('LastnameAtBirth').value = 'ATEFEH';
            document.getElementById('NationalityAtBirth').value = '111'; // Afghanistan
            document.getElementById('CountryOfBirth').value = '111'; // Afghanistan
            document.getElementById('PlaceOfBirth').value = 'SARI';
            document.getElementById('NationalityForApplication').value = '111'; // Afghanistan
            document.getElementById('TraveldocumentDateOfIssue').value = '01/23/2023';
            document.getElementById('TraveldocumentValidUntil').value = '01/23/2028';
            document.getElementById('TraveldocumentIssuingAuthority').value = '111'; // Afghanistan
        """)
    delay_time.sleep(4)        # Click the GDPR acceptance checkbox
    # checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'DSGVOAccepted')))
    # checkbox.click()
    while true:
         # Read and enter captcha text
        captcha_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, '/Captcha?')]")))
        captcha_img_url = captcha_img.get_attribute("src")
        captcha_text = read_captcha_image(captcha_img_url)

        captcha_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'CaptchaText')))
        captcha_input.clear()
        captcha_input.send_keys(captcha_text)
        # Click "Next" button
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextButton')))
        next_button.click()

        # Check if successfully navigated to the next page
        if "appointmentconfirmation" in driver.current_url:
            print("Successfully booked appointment!")
            true = False
            break
        else:
            print("Failed to book appointment. Retrying...")
            delay_time.sleep(1.5)
            driver.refresh()  # Refresh the page and try again

    # Add a delay to see the process
finally:
    # Close the browser window
    driver.quit()

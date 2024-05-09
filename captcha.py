import cv2
import numpy as np
import pytesseract
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Main function to interact with the webpage and extract CAPTCHA text
def main():
    driver = webdriver.Chrome()  # Adjust this path based on your Chrome driver location
    driver.get('YOUR_WEBPAGE_URL')

    while True:
        # Read and enter captcha text
        captcha_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, '/Captcha?')]")))
        captcha_img_url = captcha_img.get_attribute("src")
        captcha_text = read_captcha_image(captcha_img_url)

        captcha_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'CaptchaText')))
        captcha_input.clear()
        captcha_input.send_keys(captcha_text)

# Execute the main function
if __name__ == "__main__":
    main()
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Fetch credentials from environment variables set in GitHub Secrets
NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASSWORD = os.getenv("NAUKRI_PASSWORD")

# Check if credentials are retrieved correctly (for debugging)
if not NAUKRI_EMAIL or not NAUKRI_PASSWORD:
    raise ValueError("Missing Naukri credentials! Check your GitHub Secrets.")

# Start WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open Naukri Login Page
    driver.get("https://www.naukri.com/mnjuser/profile")

    # Step 2: Log in
    time.sleep(3)
    driver.find_element(By.ID, "usernameField").send_keys(NAUKRI_EMAIL)
    driver.find_element(By.ID, "passwordField").send_keys(NAUKRI_PASSWORD)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

    time.sleep(5)  # Wait for page to load

    # Step 3: Navigate to Profile Update Section
    driver.get("https://www.naukri.com/mnjuser/profile/edit")

    time.sleep(3)

    # Step 4: Make Minor Changes (e.g., add a space in the summary)
    #summary_box = driver.find_element(By.XPATH, "//textarea[@name='summary']") #unable to locate element
    #summary_box.clear()
    #summary_box.send_keys("Experienced Data Engineer specializing in PySpark. ")  # Update text
    #summary_box.send_keys(Keys.CONTROL, 's')  # Save profile

    #time.sleep(3)  # Wait for the save operation

    print("Profile updated successfully.")

finally:
    driver.quit()

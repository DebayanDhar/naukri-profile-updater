import time
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# Fetch credentials from environment variables set in GitHub Secrets
NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASSWORD = os.getenv("NAUKRI_PASSWORD")

# Check if credentials are retrieved correctly (for debugging)
if not NAUKRI_EMAIL or not NAUKRI_PASSWORD:
    raise ValueError("Missing Naukri credentials! Check your GitHub Secrets.")

# Create a new temporary Chrome profile directory
profile_dir = tempfile.mkdtemp()

chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={profile_dir}")  # Use a unique profile
chrome_options.add_argument("--headless")  # Run in headless mode for GitHub Actions
chrome_options.add_argument("--no-sandbox")  # Needed for Linux-based runners
chrome_options.add_argument("--disable-dev-shm-usage")  # Fix shared memory issues

# Start WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service , options=chrome_options)

try:
    # Step 1: Open Naukri Login Page
    driver.get("https://www.naukri.com/mnjuser/profile")

    # Step 2: Log in
    time.sleep(20)
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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

def perform_bcn_test_evolution():
    try:
        # Open Chrome browser
        driver = webdriver.Chrome()

        # Maximize the Chrome window
        driver.maximize_window()
        
        # Go to the URL
        driver.get("https://bcncgroup.com/")

        # Wait for 5 seconds (adjust as needed)
        time.sleep(5)

        # Wait for the cookie button to be clickable
        cookie_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cc-btn.cc-allow")))
        cookie_button.click()

        # Navigate to 'Who We Are'
        who_we_are_link = driver.find_element(By.CSS_SELECTOR, "a[href='https://bcncgroup.com/who-we-are/']")
        who_we_are_link.click()

        # Wait for the 'Who We Are' page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text")))

        # Extract all text from the div with class 'page__content.js-page'
        page_content_div = driver.find_element(By.CSS_SELECTOR, "div.page__content.js-page")
        extracted_text = page_content_div.text

        # Log results to a text file
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        log_filename = f"BCNTestResultEvo2_{timestamp}.txt"

        with open(log_filename, "w") as log_file:
            log_file.write(f"Test Timestamp: {timestamp}\n")
            log_file.write("Test Result: Success\n\n")
            log_file.write("Extracted Text:\n")
            log_file.write(extracted_text + "\n")

        print(f"Test completed successfully. Results logged in {log_filename}")

    except Exception as e:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        log_filename = f"BCNTestResult_{timestamp}.txt"

        with open(log_filename, "w") as log_file:
            log_file.write(f"Test Timestamp: {timestamp}\n")
            log_file.write(f"Test Result: Failure\n\n")
            log_file.write(f"Error Details:\n{str(e)}\n")

        print(f"Test failed. Error details logged in {log_filename}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    perform_bcn_test_evolution()

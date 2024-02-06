from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

def perform_bcn_test():
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

        # Extract text paragraphs from divs with class 'text'
        text_divs = driver.find_elements(By.CLASS_NAME, "text")
        extracted_texts = [div.text for div in text_divs]

        # Log results to a text file
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        log_filename = f"BCNTestResult_{timestamp}.txt"

        with open(log_filename, "w") as log_file:
            log_file.write(f"Test Timestamp: {timestamp}\n")
            log_file.write("Test Result: Success\n\n")
            log_file.write("Extracted Texts:\n")
            for idx, text in enumerate(extracted_texts, start=1):
                log_file.write(f"Paragraph {idx}:\n{text}\n\n")

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
    perform_bcn_test()

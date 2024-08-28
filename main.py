import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize WebDriver
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(), options=options)

# Configuration
user_menu_button_xpath = '//button[@aria-label="Open user menu"]'
sign_in_button_xpath = '//button[@data-name="header-user-menu-sign-in"]'
email_button_xpath = '//button[@name="Email"]'
username_field_id = 'id_username'
password_field_id = 'id_password'
submit_button_xpath = '//button[@data-overflow-tooltip-text="Sign in"]'

try:
    # Open the URL
    driver.get('https://in.tradingview.com/')  # Replace with the actual URL if different

    wait = WebDriverWait(driver, 20)  # Wait for up to 20 seconds

    # Wait for the user menu button to be clickable and click it
    user_menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, user_menu_button_xpath)))
    user_menu_button.click()

    # Optional: Wait a bit longer to ensure the menu items are loaded
    time.sleep(3)  # Adjust this delay if necessary

    # Wait for the "Sign in" button to be clickable and click it
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))
    sign_in_button.click()

    # Optional: Wait a bit longer to ensure the next page is loaded
    time.sleep(3)  # Adjust this delay if necessary

    # Wait for the "Email" button to be clickable and click it
    email_button = wait.until(EC.element_to_be_clickable((By.XPATH, email_button_xpath)))
    email_button.click()

    # Enter the username
    username_field = wait.until(EC.visibility_of_element_located((By.ID, username_field_id)))
    username_field.send_keys('wodowen265')

    time.sleep(3)

    # Enter the password
    password_field = wait.until(EC.visibility_of_element_located((By.ID, password_field_id)))
    password_field.send_keys('wodowen265@ikangou.com')

    time.sleep(2)

    # Wait for the "Sign in" button to be clickable and click it
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
    time.sleep(2)
    submit_button.click()
    # Optional: Wait a bit longer to ensure the inputs are filled
    time.sleep(2)

    # Prompt the user to input the XPaths of the elements to capture
    randomip = input("Enter something:")
    xpath_input1 = "/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/span[2]"
    xpath_input2 = "/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div"
    xpath_input3 = "/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div"
    xpath_input4 = "/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/div"
    xpath_input5 = "/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div"

    # Set the loop counter
    loop_counter = 0
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN).perform()

    while loop_counter < 501:
        WebDriverWait(driver, 20).until(
            lambda driverd: driverd.execute_script('return document.readyState') == 'complete')

        try:
            # Locate the specific elements you want to capture based on user input
            element_to_capture1 = driver.find_element(By.XPATH, xpath_input1)
            element_to_capture2 = driver.find_element(By.XPATH, xpath_input2)
            element_to_capture3 = driver.find_element(By.XPATH, xpath_input3)
            element_to_capture4 = driver.find_element(By.XPATH, xpath_input4)
            element_to_capture5 = driver.find_element(By.XPATH, xpath_input5)

            # Extract text directly from the web elements
            extracted_text1 = element_to_capture1.text
            extracted_text2 = element_to_capture2.text
            extracted_text3 = element_to_capture3.text
            extracted_text4 = element_to_capture4.text
            extracted_text5 = element_to_capture5.text

            # Print the extracted text
            print(
                f"{loop_counter + 1} | {extracted_text1} | {extracted_text2} | {extracted_text3} | {extracted_text4} | {extracted_text5}")

            with open('values.txt', 'a', encoding='utf-8') as text_file:
                # Save the extracted texts to a text file
                text_file.write(
                    f"{loop_counter + 1} {extracted_text1} {extracted_text2} {extracted_text3} {extracted_text4} {extracted_text5}\n")
                print('------------------------------------------------')

        except Exception as e:
            print(f"Exception occurred: {e}. Retrying...")
            time.sleep(2)  # Wait a bit before retrying
            loop_counter -= 1  # Decrement the loop counter to retry this iteration

        # Increment the loop counter
        loop_counter += 1

        # Wait for 60 seconds
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_DOWN).perform()

finally:
    # Close the browser
    driver.quit()

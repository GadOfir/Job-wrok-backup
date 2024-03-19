from selenium.common import NoAlertPresentException

from exp import main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


def simple_with_gui():
    params = [
         ('PALM', 4, 'false', 'false', 'both', 9, 20, -1, 'Check GUI'),#4
        #('CLAW', 0, 'true', 'false', 'both', 9, 20, -1, 'Check GUI'),#4
        ('CLAW', 4, 'true', 'true', 'both', 12, 20, 5, 'Check GUI'),
        ('CLAW', 4, 'true', 'true', 'both', 9, 20, 4, 'Check GUI'),
        ('FINGERTIP', 3, 'true', 'true', 'both', 9, 20, 5, 'Check GUI'),
        # Add more test cases here as needed
    ]

    for i, param_set in enumerate(params):
        result = main(*param_set[:-1])  # Exclude the description
        description = param_set[-1]  # Extract the description
        length = len(result)  # Calculate the length of the result

        # Output API test result
        print(f"Test Case {i + 1}: Description: {description}, Result Length on API: {length}")

        # Run test using GUI
        gui_test_result = run_gui_test(length,*param_set)  # Corrected
        print(f"GUI Test Case {i + 1}: {gui_test_result}")  # Output GUI test result


def run_gui_test(length_from_api,*params):
    # Extract parameters
    grip_style, leniency, wireless, lefhand, symmetry, grip_width, hand_length, numberofbuttens, description = params
    result_gui = 0

    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()  # You can use any browser driver here (e.g., Chrome, Firefox)

    try:
        # Navigate to the provided link
        driver.get("https://www.rocketjumpninja.com/mouse-search")

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='h_length']")))

        # Find the input element with the name 'h_length'
        h_length_input = driver.find_element(By.XPATH, "//input[@name='h_length']")
        h_length_input.send_keys(str(hand_length))

        h_width_input = driver.find_element(By.XPATH, "//input[@name='h_width']")
        h_width_input.send_keys(str(grip_width))

        # XPath expressions for radio buttons
        xpath_leniency = f"//input[@class='form_radio' and @name='leniency' and @value='{leniency}']"
        radio_button_leniency = driver.find_element(By.XPATH, xpath_leniency)
        radio_button_leniency.click()

        xpath_grip_type = f"//input[@class='form_radio' and @name='grip_type' and @value='{grip_style}']"
        radio_button_grip_type = driver.find_element(By.XPATH, xpath_grip_type)
        radio_button_grip_type.click()

        xpath_shape = f"//input[@class='form_radio' and @name='shape' and @value='{symmetry}']"
        radio_button_shape = driver.find_element(By.XPATH, xpath_shape)
        radio_button_shape.click()

        if wireless != 'false':
            xpath_wireless_checkbox = f"//input[@type='checkbox' and @name='wireless']"
            checkbox_wireless = driver.find_element(By.XPATH, xpath_wireless_checkbox)
            checkbox_wireless.click()
        if lefhand != 'false':
            xpath_lefthanded_checkbox = "//input[@type='checkbox' and @name='lefthanded']"
            checkbox_lefthanded = driver.find_element(By.XPATH, xpath_lefthanded_checkbox)
            checkbox_lefthanded.click()
        if numberofbuttens != -1:
            xpath_numButtons_input = "//input[@id='numButtons']"
            numButtons_input = driver.find_element(By.XPATH, xpath_numButtons_input)
            numButtons_input.send_keys(str(numberofbuttens))

        xpath_searchButton_button = "//input[@id='searchButton' and @type='button' and @value='SEARCH']"
        xpath_searchButton_button = driver.find_element(By.XPATH, xpath_searchButton_button)
        xpath_searchButton_button.click()

        # Set the value of the input element with the hand length parameter
        #ActionChains(driver).move_to_element(h_length_input).click().send_keys(str(hand_length)).perform()
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print("Alert Text:", alert_text)
        except NoAlertPresentException:
            try:
                row_index = 1
                driver.implicitly_wait(5)  # Wait for up to 10 seconds
                while True:

                    row_xpath = f"//*[@id='resultsTable']/tr[{row_index}]"
                    # Try to find the row
                    row = driver.find_element(By.XPATH, row_xpath)
                    # If found, increment the row index
                    row_index += 1
            except:
                if row_index>3:
                    print("Number of table rows found on GUI:", row_index - 1)
                else:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@name='h_length']")))

                    # Find the element with the specified XPath
                    no_results_element = driver.find_element(By.XPATH, "//*[@id='resultsTable']/tr/td")
                    row_index_temp = row_index
                    row_index = 1

                    # Check if the text of the element is "No results"
                    if no_results_element.text.strip() == "No results":
                        print("No results found.")
                        return "No Results"
                    else:
                        # Proceed with further processing if results are found
                        row_index = row_index_temp
                        print("Number of table rows found on GUI:", row_index - 1)





        return "Pass"  # Replace with actual test result (e.g., "Pass" or "Fail")

    finally:
        result_gui = row_index - 1
        if result_gui == length_from_api:
            return "Pass, API and GUI results match"
        else:
            return "Fail API and GUI results do not match"
        driver.quit()
        # Close the browser



if __name__ == "__main__":
    simple_with_gui()

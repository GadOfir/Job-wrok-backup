from selenium.common import NoAlertPresentException
from selenium.webdriver.support.select import Select

from exp import main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


def guy_valid_values_alert():
    params = [
        ('CLAW', 0, 'false', 'false', 'both', 9, 20, -1, 'Check GUI'),
        ('PALM', 4, 'true', 'true', 'both', 12, 20, 5, 'Check GUI'),
        ('FINGERTIP', 4, 'true', 'true', 'both', 9, 20, 4, 'Check GUI'),
        ('CLAW', 3, 'true', 'true', 'both', 9, 20, 5, 'Check GUI'),
        # Add more test cases here as needed
    ]

    for i, param_set in enumerate(params):
        result = main(*param_set[:-1])  # Exclude the description
        description = param_set[-1]  # Extract the description


        # Run test using GUI
        run_gui_test(*param_set)  # Corrected



def run_gui_test(*params):
    # Extract parameters
    grip_style, leniency, wireless, lefhand, symmetry, grip_width, hand_length, numberofbuttens, description = params
    result_gui = 0

    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()  # You can use any browser driver here (e.g., Chrome, Firefox)

    try:
        # Navigate to the provided link

        driver.get("https://www.rocketjumpninja.com/mouse-search")

        xpath_searchButton_button = "//input[@id='searchButton' and @type='button' and @value='SEARCH']"
        xpath_searchButton_button = driver.find_element(By.XPATH, xpath_searchButton_button)

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='h_length']")))


        select_element = driver.find_element(By.ID, "measurement")
        measurement = Select(select_element)
        #measurement.select_by_value("inches")

        # Find the input element with the name 'h_length'
        teststatus = 0

        h_length_input = driver.find_element(By.XPATH, "//input[@name='h_length']")
        h_length_input.send_keys('XX')
        xpath_searchButton_button.click()
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print("Alert Text:", alert_text)
            alert.accept()
            teststatus = teststatus + 1
        except NoAlertPresentException:
            print("No alert found.")
        driver.implicitly_wait(10)  # Wait for u
        h_length_input.clear()
        h_length_input.send_keys(str(hand_length))

        h_width_input = driver.find_element(By.XPATH, "//input[@name='h_width']")
        h_width_input.send_keys(('XX'))
        xpath_searchButton_button.click()
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print("Alert Text:", alert_text)
            alert.accept()
            teststatus = teststatus + 1
        except NoAlertPresentException:
            print("No alert found.")
        driver.implicitly_wait(10)  # Wait for u
        h_width_input.clear()
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



        xpath_searchButton_button.click()



        driver.implicitly_wait(10)  # Wait for up to 10 seconds
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print("Alert Text:", alert_text)
        except NoAlertPresentException:
            print("No alert found after valid values.")







        return "Pass"  # Replace with actual test result (e.g., "Pass" or "Fail")

    finally:
        if teststatus == 2:
            print("Test Passed")
        else:
            print("Test Failed")

        driver.quit()
        # Close the browser



if __name__ == "__main__":
    guy_valid_values_alert()

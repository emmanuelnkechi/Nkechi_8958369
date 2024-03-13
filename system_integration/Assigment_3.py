# Importing required libraries

# pip install selenium

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Fido.ca homepage
driver.get("https://www.fido.ca/")
time.sleep(8)

# Find the Shop dropdown and click on it
shop_dropdown = driver.find_element("id", "geMainMenuDropdown_0")
shop_dropdown.click()
time.sleep(5)


# Locate Phones from the dropdown and click on it
phones_option = driver.find_element("xpath", "/html/body/div[1]/ge-header/div/header/div/div["
                                             "2]/div/nav/ge-main-menu/div/ge-dropdown/div/div/div/ul/li[1]")
phones_option.click()

# Waiting for the page to navigate to phones section
time.sleep(5)

# Filter Phones by motorola
filter_by_motorola = driver.find_element("xpath", "/html/body/hup-root/rci-main/main/ng-component/r-choose-phone/dsa"
                                                  "-layout/div/div/div[2]/dsa-filter-box/div/div/div[1]/div["
                                                  "2]/fieldset[2]/div/div[4]/ds-checkbox/label")
time.sleep(5)
filter_by_motorola.click()

# Waiting for the page to navigate to phones section
time.sleep(5)

# Locating elements containing the text "Samsung", "iPhone", "TCL" and "Motorola"
phones_row = driver.find_element("xpath", "/html/body/hup-root/rci-main/main/ng-component/r-choose-phone/dsa-layout"
                                          "/div/div/div[3]/div[2]")


# Checking conditions to ensure page shows only Motorola Phones
if "Samsung" in phones_row.text:
    print("Error: Samsung found in the filter!")
elif "iPhone" in phones_row.text:
    print("Error: iPhone found in the filter!")
elif "Google Pixel" in phones_row.text:
    print("Error: Google Pixel found in the filter!")
elif "TCL" in phones_row.text:
    print("Error: TCL found in the filter!")
else:
    print("The filter fetches only Motorola Phones.")

# click on view details button for motorola edge (2023)
view_details_button = driver.find_element("xpath", "/html/body/hup-root/rci-main/main/ng-component/r-choose-phone/dsa"
                                                   "-layout/div/div/div[3]/div[2]/div["
                                                   "1]/r-nac-tile/ds-tile/div/div/div[4]/a")
view_details_button.click()
time.sleep(5)

# on the popup modal, click on getting started
get_started_button = driver.find_element("id", "trident-cta-nac")
get_started_button.click()
time.sleep(5)

# Find the build your plan and click on it
build_plan_button = driver.find_element("xpath", "/html/body/hup-root/rci-main/main/ng-component/ng-component/r"
                                                 "-device-config/dsa-layout[1]/div/div/div[3]/div/div[4]/div/button")
build_plan_button.click()
time.sleep(5)

# Finding the Promo code input and enter random code
promo_code_input = driver.find_element("xpath", "/html/body/hup-root/rci-main/main/ng-component/ng-component/r-build"
                                                "-plan/dsa-layout[4]/div/div/div[2]/r-pom-promotions/div["
                                                "1]/ds-accordion/div/ds-accordion-panel/div/ds-expander/div/div/div"
                                                "/div/div[2]/form/div/ds-form-field/div/div[1]")
# Using JavaScript to set the value of the input field
driver.execute_script("arguments[0].value = '765';", promo_code_input)
time.sleep(2)


# Locate the check button and click to send promo code
check_button = driver.find_element("xpath", "/html/body/hup-root/rci-main/main/ng-component/ng-component/r-build-plan"
                                            "/dsa-layout[4]/div/div/div[2]/r-pom-promotions/div["
                                            "1]/ds-accordion/div/ds-accordion-panel/div/ds-expander/div/div/div/div"
                                            "/div[2]/form/div/button")
check_button.click()

# Waiting for request response
time.sleep(5)

# Wait for the element containing the text to appear
try:
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/hup-root/rci-main/main/ng-component/ng-component/r"
                                                    "-build-plan/dsa-layout[4]/div/div/div[2]/r-pom-promotions/div["
                                                    "1]/ds-accordion/div/ds-accordion-panel/div/ds-expander/div/div"
                                                    "/div/div/div[2]/form/div/ds-form-field/div/div[3]/div"))
    )
    print("Error message found:", error_message.text)
except Exception as e:
    print("Error message not found or took too long to appear")
    time.sleep(5)

# Closing the webdriver
driver.close()

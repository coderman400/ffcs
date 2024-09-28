import time

from data import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm import tqdm  # Progress bar

# List of course sets to validate (each set is a list of tuples containing course code and slots)
course_sets = data
# Setup the WebDriver (Make sure you have the correct path for your chromedriver)
driver = webdriver.Chrome()

# Define the webpage URL
url = "https://ffcsonthego.vatz88.in/#Vellore"  # Replace with actual URL

# Function to process each set of courses
def process_courses(course_set, index):
    # Reload the page for each course set
    driver.get(url)
    time.sleep(2)  # Give time for page to load

    # Add each course from the current set
    for course in course_set:
        course_code, slots = course

        for slot in slots:
            # Find the course input field and enter the course code
            course_input = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.ID, "course-input"))  # Replace with actual field ID
            )

            course_input.clear()
            course_input.send_keys(course_code)
            
            # Toggle advanced options if necessary (depending on the slot input method)
            adv_opts = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.ID, "advanced-toggle"))  # Replace with actual field ID
            )
            adv_opts.click()
            
            slot_input = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, "slot-input"))  # Replace with actual field ID
            )
            driver.execute_script("arguments[0].value = arguments[1];", slot_input, slot)
        
            # Click the 'Add Course' button after entering the details
            add_button = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "add-course-button")) 
            )
            add_button.click()

    # Check for clashes and gather results
    rows = driver.find_elements(By.CSS_SELECTOR, 'tr')

    # Initialize an empty list to store clashing courses
    clashing_courses = []

    # Loop through each row to check for the 'table-danger' class indicating a clash
    for row in rows:
        # Check if the row has the 'table-danger' class
        if "table-danger" in row.get_attribute("class"):
            # Get the course details from the row
            slot = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text  # Adjust based on table structure
            course_code = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
            course_title = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text

            # Append the course details to the clashing_courses list
            clashing_courses.append((slot, course_code, course_title))

    # Write the results to the file
    with open("clashing_courses.txt", "a") as f:
        f.write(f"Course Set {index + 1}:\n")
        if clashing_courses:
            for clash in clashing_courses:
                f.write(f"Clashing Course: Slot: {clash[0]}, Code: {clash[1]}, Title: {clash[2]}\n")
        else:
            f.write("No clashes detected.\n")
        f.write("\n")  # Add an extra line between course sets

    reset_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-danger') and contains(., 'Reset Table')]"))
    )
    reset_button.click()

    # Wait for the modal confirmation button to be clickable and click it
    confirm_reset_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "reset-tt-button"))
    )
    confirm_reset_button.click()


# Process each course set with tqdm for a progress bar
for i, course_set in enumerate(tqdm(course_sets, desc="Processing Course Sets")):
    process_courses(course_set, i)

input()
# Close the WebDriver after all sets are processed
driver.quit()

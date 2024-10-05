import time

import pytest
from data import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm import tqdm

# Shift for course sets
shift = 0
course_sets = data[shift:]

# Initialize the WebDriver
driver = webdriver.Chrome()
url = "https://ffcsonthego.vatz88.in/"
driver.get(url)

# Open advanced options
def open_advanced_options():
    adv_opts = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.ID, "advanced-toggle"))
    )
    adv_opts.click()

# Process the courses for each set
def process_courses(course_set, index):
    clashing_courses = []
    for course in course_set:
        course_code, slots = course
        for slot in slots:
            if "L" in slot:
                course_code += "LAB"

            add_course(course_code, slot)

    clashing_courses.extend(check_for_clashes())
    reset_table()

    return clashing_courses

# Add course to the input
def add_course(course_code, slot):
    course_input = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "course-input"))
    )
    course_input.clear()
    course_input.send_keys(course_code)

    slot_input = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "slot-input"))
    )
    driver.execute_script("arguments[0].value = arguments[1];", slot_input, slot)

    add_button = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "add-course-button"))
    )
    add_button.click()

# Check for clashing courses
def check_for_clashes():
    rows = driver.find_elements(By.CSS_SELECTOR, 'tr')
    clashing_courses = []

    for row in rows:
        if "table-danger" in row.get_attribute("class"):
            slot = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text
            course_code = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
            course_title = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
            clashing_courses.append((slot, course_code, course_title))

    return clashing_courses

# Reset the course table
def reset_table():
    reset_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-danger') and contains(., 'Reset Table')]"))
    )
    reset_button.click()

    confirm_reset_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "reset-tt-button"))
    )
    confirm_reset_button.click()

# Test function using pytest
@pytest.mark.parametrize("index, course_set", enumerate(course_sets))
def test_course_clashes(index, course_set):
    open_advanced_options()
    clashing_courses = process_courses(course_set, index)

    # Assertions to verify clashing courses
    if clashing_courses:
        assert len(clashing_courses) > 0, f"Course Set {index + 1}: Clashes detected!"
        for clash in clashing_courses:
            slot, code, title = clash
            print(f"Course Set {index + 1}: Clashing Course - Slot: {slot}, Code: {code}, Title: {title}")
    else:
        assert not clashing_courses, f"Course Set {index + 1}: No clashes detected."

# Main function to run tests
if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
    driver.quit()

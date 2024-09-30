import time

from data import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm import tqdm

shift = 0

course_sets = data[shift:]

driver = webdriver.Chrome()

url = "https://ffcsonthego.vatz88.in/"

driver.get(url)
adv_opts = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.ID, "advanced-toggle"))  
    )
adv_opts.click()


def process_courses(course_set, index):

    for course in course_set:
        course_code, slots = course

        for slot in slots:
            if "L" in slot:
                course_code += "LAB"

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

    
    rows = driver.find_elements(By.CSS_SELECTOR, 'tr')

    clashing_courses = []

    for row in rows:
        if "table-danger" in row.get_attribute("class"):
            slot = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text  
            course_code = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
            course_title = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
            clashing_courses.append((slot, course_code, course_title))


    with open("clashing_courses.txt", "a") as f:
        key = 1 if shift == 0 else 0
        f.write(f"Course Set {index + shift + key}:\n")
        if clashing_courses:
            for clash in clashing_courses:
                f.write(f"Clashing Course: Slot: {clash[0]}, Code: {clash[1]}, Title: {clash[2]}\n")
        else:
            f.write("No clashes detected.\n")
        f.write("\n")  


    reset_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-danger') and contains(., 'Reset Table')]"))
    )
    reset_button.click()

    
    confirm_reset_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "reset-tt-button"))
    )
    confirm_reset_button.click()


for i, course_set in enumerate(tqdm(course_sets, desc="Processing Course Sets")):
    process_courses(course_set, i)

input()

driver.quit()

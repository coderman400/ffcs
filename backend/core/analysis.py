import json

import matplotlib.pyplot as plt
from data import data

timetables = []

for timetable in data:
    courses = []
    for course in timetable:
        courses.append(course[0])
    timetables.append(courses)        

with open("final.json") as f:
    complete_course = json.load(f)

complete_course = {i:0 for i in list(complete_course.keys())}
course_data = timetables
all_courses = [course for sublist in course_data for course in sublist]

for i in all_courses:
    complete_course[i]+=1

# # Plotting
def plot(complete_course):
    plt.figure(figsize=(10, 6))
    plt.bar(list(complete_course.keys()), complete_course.values())
    plt.xlabel('Courses')
    plt.ylabel('Frequency')
    plt.title('Course Frequency')
    plt.xticks(rotation=90)  # Rotate x-axis labels for readability
    plt.show()

plot(complete_course)
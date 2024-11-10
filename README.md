# FFCS
A website for VIT students to completely automate the semester timetable generation during FFCS ( Fully Flexible Credit System ).

![1](https://github.com/user-attachments/assets/2c5387c2-74ba-42d1-a70c-b6d7b8d2dd4b)


## What is FFCS?
FFCS is a dreaded time for students in VIT where students receive 12-20 courses to choose from and all the faculties, slots and options within.
Each student then tries to painstakingly fit enough courses for their credit requirements in the timetable, carefully avoiding clashing slots and time constraints.
All of this while also trying to make some free time for themselves and not have a timetable with classes scattered through the day.

## Our Solution
Our timetable generator allows students to just upload all the courses offered via simple screenshots from the college website, VTOP.
We extract only the required data from each image and reformat them into a efficient structure **using an AI.**
After additional editing and preference selections from the students, the information is fed into a complex **backtracking algorithm.**
The algorithm considers all the user's needs and constraints along with the choices of slots to try and find the best combinations of courses
and slots to meet the required number of credits. **A task that takes hours of work for students now reduced to ~5 minutes.**

How to use it:  https://docs.google.com/document/d/1FHDIL8mDZ92XuJt-lkB4fGWrdwQLlSpmY2oy7ivKQjA/edit?usp=sharing

## Tech Stack
- React.js and Tailwind CSS for frontend
- FastAPI in the backend
- Gemini API for image extraction and refactoring

## Did it work?
![image](https://github.com/user-attachments/assets/43bb515b-f1c1-4289-a087-d768ee6ca45f)

Over the two days between slots release and registration time, we hit over 700 unique visitors. Which I would consider a success for the first release.
Before the next registration, we're aiming to add a chrome extension for better information extraction as well as other new friendly features.

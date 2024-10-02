import json

#user preferences
morning = False
creditsRequired = 27

# Load courses and slots from JSON files
with open('/home/arvind/ffcs/algo/final.json', 'r') as file:
    data = json.load(file)

# Function to generate a sorting key based on the `morning` preference
def sort_key(slot):
    section = slot[0]  # First element is the section, e.g., 'A1', 'A2', 'B1'
    if morning:
        # Prioritize sections ending with '1' if morning is True
        if section[-1] == '1':
            return (0, section)
        elif section[-1] == '2':
            return (1, section)
    else:
        # Prioritize sections ending with '2' if morning is False
        if section[-1] == '2':
            return (0, section)
        elif section[-1] == '1':
            return (1, section)
    
    # Default priority for other sections
    return (2, section)

# Prepare courses_list as a list of tuples (course_code, sorted_unique_slots)
courses_list = []
for course_code, course_info in data.items():
    slots = set()
    for professor, slot_list in course_info['professors'].items():
        for slot in slot_list:
            slots.add(tuple(slot))  # Convert list to tuple for set uniqueness

    # Sort the slots using the custom key based on morning preference
    sorted_slots = sorted(slots, key=sort_key)
    
    # Append to the course list using the sorted order
    courses_list.append((course_code, list(sorted_slots)))

# Load the available slots table from JSON
with open('/home/arvind/ffcs/algo/slots.json', 'r') as file:
    raw_slots_dict = json.load(file)

# Parse keys and values to a dictionary of tuples
available = {tuple(key.strip("()").split(", ")): value for key, value in raw_slots_dict.items()}

selected = []

time_clash = ['L4','L10','L16','L22','L28',
              'L5','L11','L17','L23','L29',
              'L34','L40','L46','L52','L58',
              'L35','L41','L47','L53','L59',
              'L36','L42','L48','L54','L60']

# Function to check if a course can fit in available slots
def fittable(available, course):
    for slot in course[1]:
        # Split sections and time slots based on '+'
        sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
        sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

        # # Ensure that none of the sections or sub-slots conflict
        conflicting_sections = any(
            section in key and available[key] != '' for key in available for section in sections
        )
        conflicting_sub_slots = any(
            sub_slot in key and available[key] != '' for key in available for sub_slot in sub_slots
        )

        clashes = False
        #FOR SECTIONS
        for section in sections:
            #find corresponding tuple
            for slotTuple in available:
                if(slotTuple[0]==section):
                    #once found the tuple, check the lab slot and derive next lab slot
                    lab_slot = slotTuple[1]
                    next_lab_slot =  f"{lab_slot[0]}{int(lab_slot[1:])+1}"
                    #if the next lab slot is a time clashing slot
                    if(next_lab_slot in time_clash):
                        #find the coresponding tuple of next lab slot
                        for eachTuple in available:
                            if(len(eachTuple)>1):
                                if(eachTuple[1]==next_lab_slot):
                                    break
                        #then check if there is a lab course in the value of that tuple
                        if('LAB' in available[eachTuple]):
                            clashes=True

        for sub_slot in sub_slots:
            #find corresponding tuple
            if(sub_slot in time_clash):
                prev_lab_slot =  f"{sub_slot[0]}{int(sub_slot[1:])-1}"
                #find tuple corresponding to prev lab slot
                for slotTuple in available:
                    if(slotTuple[1]==prev_lab_slot):
                        break
               #once found the tuple, check if it has a THEORY course
                if('THEORY' in available[slotTuple]):
                    clashes=True
                    
        # If both sections and sub-slots are available and not conflicting, consider this slot as fittable
        if not (conflicting_sections or conflicting_sub_slots or clashes):
            return slot

    # If no slot is fittable, return None
    return None

# Function to mark the selected slot as filled in the available slots
def updateTable(available, course, slot):
    course_code = course[0]
    sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
    sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

    # Update every key in `available` that contains any of these sections or sub-slots
    for key in available:
        # Fill in as "course_code THEORY" for matching sections
        if any(section in key for section in sections):
            available[key] = f"{course_code} THEORY"  # Mark section as occupied

        # Fill in as "course_code LAB" for matching sub-slots
        if any(sub_slot in key for sub_slot in sub_slots):
            available[key] = f"{course_code} LAB"  # Mark sub-slot as occupied

# Function to free up the slots in the available slots table
def removeTable(available, course, slot):
    sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
    sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

    # Reset every key in `available` that contains any of these sections or sub-slots
    for key in available:
        if any(section in key for section in sections) or any(sub_slot in key for sub_slot in sub_slots):
            available[key] = ''  # Mark this key as free again

def calculateCredits(selected):
    total_credits = 0
    seen_courses = set()

    for course_code, slot in selected:
        if course_code in seen_courses:
            continue

        seen_courses.add(course_code)
        slot_credits = 0
        sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
        sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

        # Calculate credits for sections
        for section in sections:
            if section.startswith("T"):  # TA1, TA2, etc. are 1 credit
                slot_credits += 1
            else:  # A1, A2, B1, etc. are 2 credits
                slot_credits += 2

        # Calculate credits for sub-slots (L1, L2, etc.)
        for sub_slot in sub_slots:
            if sub_slot.startswith("L"):  # Each L slot (L1, L2, etc.) is 0.5 credit
                slot_credits += 0.5

        # Special case: STS courses
        if course_code.startswith("STS"):
            slot_credits = 1

        total_credits += slot_credits

    return total_credits



def backtrack(selected, available, index, results):
    # Ensure that the STS course is always added first based on the preference
    if not any(course[0].startswith("STS") for course in selected):
        # Look for the first STS course in the list
        for idx, course in enumerate(courses_list):
            if course[0].startswith("STS"):
                # Filter STS slots based on user preference (morning/afternoon)
                preferred_slots = [
                    slot for slot in course[1]
                    if (slot[0][1] == "2") == (morning==False)  # Check second character for morning/afternoon
                ]

                for fitting_slot in preferred_slots:
                    # Add STS course to the selected list and update slots
                    updateTable(available, course, fitting_slot)
                    selected.append((course[0], fitting_slot))

                    # Continue to the next courses from index 0 (reset backtrack)
                    backtrack(selected, available, 0, results)

                    # Backtrack: remove the STS course and reset slots
                    selected.pop()
                    removeTable(available, course, fitting_slot)

                return  # Return after processing the STS course to avoid skipping it

    # Check the base condition: Total credits should equal the limit
    if calculateCredits(selected) == creditsRequired:
        #check if atleast 2 more timing preferred slots than 
        morningSlots=0
        afternoon=0
        for courseTuple in list(selected):
            slot = courseTuple[1][0]
            if(slot[1]=='2'):
                afternoon+=1
            else:
                morningSlots+=1
        if((not morning and afternoon-morningSlots>=2) or (morning and morningSlots-afternoon>=2)):
            results.append(list(selected))  # Store a copy of the current selection
            return

    # No more courses to select if index exceeds list length
    if index >= len(courses_list):
        return

    # Obtain the next course to evaluate from the list
    nextCourse = courses_list[index]

    # Try to fit the next course into available slots
    fitting_slot = fittable(available, nextCourse)
    if fitting_slot:
        # If fitting slot is found, add course to selected and update slots of available
        updateTable(available, nextCourse, fitting_slot)
        selected.append((nextCourse[0], fitting_slot))

        # Recurse to the next course on the list
        backtrack(selected, available, index + 1, results)

        # Backtrack: remove the last added course and the corresponding slots from available
        selected.pop()
        removeTable(available, nextCourse, fitting_slot)

    # If slot couldn't fit, skip it and then try with the next course
    backtrack(selected, available, index + 1, results)


results = []
backtrack(selected, available, 0, results)

# Display all possible results
if results:
    #index, result in the list of results
    for idx, res in enumerate(results):
        afternoon=0
        morningSlots=0
        print(f"Result {idx + 1}: {res}")
        print(f"Number of courses: {len(res)}\n")
        for courseTuple in res:
            slot = courseTuple[1][0]
            if(slot[1]=='2'):
                afternoon+=1
            else:
                morningSlots+=1
        print("Afternoon: ", afternoon, " Morning: ", morningSlots)
        
else:
    print('impossible')

results = "\n".join([f"{result}," for result in results])

with open('result.txt', 'a') as f:
    f.write(results)
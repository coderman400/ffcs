import json

# from config import ROOT_DIR

# slots_json = ROOT_DIR / "core" / "ffcs" / "slots.json"
slots_json = "core/ffcs/slots.json"

class Algorithm:
    def __init__(self,data,morning=True,creditsRequired=27):
        self.morning = morning
        self.creditsRequired = creditsRequired
        self.time_clash  = [
                    'L4','L10','L16','L22','L28',
                    'L5','L11','L17','L23','L29',
                    'L34','L40','L46','L52','L58',
                    'L35','L41','L47','L53','L59',
                    'L36','L42','L48','L54','L60'
                    ]
        
        self.data = data
        print(data)
        print(morning)
        print(creditsRequired)
        self.selected = []
        self.results = []
        self.courses_list = self.prep_courses_list()
        print("prepped course list")
        self.available = self.prep_available_slots()
        print("prepped available slots")
        self.backtrack(self.available,0)
        print("Results",len(self.results))
        self.write()

    def write(self):
        print(self.results)
        results = "\n".join([f"{result}," for result in self.results])
        with open("core/ffcs/output.txt","a") as f:
            f.write(results)


    def sort_key(self,slot):
        print("sorted")
        section = slot[0]  # First element is the section, e.g., 'A1', 'A2', 'B1'
        if self.morning:
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


    def prep_courses_list(self):
        courses_list = []
        for course_code, course_info in self.data.items():
            slots = set()
            for professor, slot_list in course_info['professors'].items():
                for slot in slot_list:
                    slots.add(tuple(slot))  # Convert list to tuple for set uniqueness
            sorted_slots = sorted(slots,key=self.sort_key)
            courses_list.append((course_code, list(sorted_slots)))
        return courses_list
    
    def prep_available_slots(self):
        with open(slots_json, 'r') as file:
            raw_slots_dict = json.load(file)

        # Parse keys and values to a dictionary of tuples
        available = {tuple(key.strip("()").split(", ")): value for key, value in raw_slots_dict.items()}
        return available

    # Function to check if a course can fit in available slots
    def fittable(self,available, course):
        print("fitting course")
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

            for section in sections:
                for slotTuple in available:
                    if(slotTuple[0] == section):
                        lab_slot = slotTuple[1]
                        next_lab_slot = f"{lab_slot[0]}{int(lab_slot[1:])+1}"
                        if(next_lab_slot in self.time_clash):
                            for eachTuple in available:
                                if(len(eachTuple) > 1):
                                    if(eachTuple[1] == next_lab_slot):
                                        break
                            if('LAB' in available[eachTuple]):
                                print("CLASHING")
                                clashes=True
            
            for sub_slot in sub_slots:
                if(sub_slot in self.time_clash):
                    prev_lab_slot = f"{sub_slot[0]}{int(sub_slot[1:])-1}"
                    for slotTuple in available:
                        if(slotTuple[1] == prev_lab_slot):
                            break
                    if('THEORY' in available[slotTuple]):
                        print("CLASHING")
                        clashes=True
            
            if not(conflicting_sections or conflicting_sub_slots or clashes):
                return slot

        # If no slot is fittable, return None
        return None

    # Function to mark the selected slot as filled in the available slots
    def updateTable(self,available, course, slot):
        course_code = course[0]
        sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
        sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

        # Update every key in `available` that contains any of these sections or sub-slots
        for key in available:
            if any(section in key for section in sections):
                available[key] = f"{course_code} THEORY"  # Mark section as occupied

            # Fill in as "course_code LAB" for matching sub-slots
            if any(sub_slot in key for sub_slot in sub_slots):
                available[key] = f"{course_code} LAB"  # Mark sub-slot as occupied

    # Function to free up the slots in the available slots table
    def removeTable(self,available, course, slot):
        sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
        sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

        # Reset every key in `available` that contains any of these sections or sub-slots
        for key in available:
            if any(section in key for section in sections) or any(sub_slot in key for sub_slot in sub_slots):
                available[key] = ''  # Mark this key as free again

    def calculateCredits(self,selected):
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
        print(total_credits)

        return total_credits


    def backtrack(self,available, index):
        # Ensure that the STS course is always added first based on the preference
        if not any(course[0].startswith("STS") for course in self.selected):
            # Look for the first STS course in the list
            for idx, course in enumerate(self.courses_list):
                if course[0].startswith("STS"):
                    # Filter STS slots based on user preference (morning/afternoon)
                    preferred_slots = [
                        slot for slot in course[1]
                        if (slot[0][1] == "2") == (self.morning == False)  # Check second character for morning/afternoon
                    ]

                    for fitting_slot in preferred_slots:
                        # Add STS course to the selected list and update slots
                        self.updateTable(available, course, fitting_slot)
                        self.selected.append((course[0], fitting_slot))

                        # Continue to the next courses from index 0 (reset backtrack)
                        self.backtrack(available, 0)

                        # Backtrack: remove the STS course and reset slots
                        self.selected.pop()
                        self.removeTable(available, course, fitting_slot)
                    print("STS")
                    return  # Return after processing the STS course to avoid skipping it

        # Check the base condition: Total credits should equal 27
        if self.calculateCredits(self.selected) == self.creditsRequired:
            self.results.append(list(self.selected))  # Store a copy of the current selection
            print("found")
            return

        # No more courses to select if index exceeds list length
        if index >= len(self.courses_list):
            print("done courses")
            return

        # Obtain the next course to evaluate from the list
        nextCourse = self.courses_list[index]

        # Try to fit the next course into available slots
        fitting_slot = self.fittable(available, nextCourse)
        if fitting_slot:
            # If fitting slot is found, add course to selected and update slots of available
            self.updateTable(available, nextCourse, fitting_slot)
            self.selected.append((nextCourse[0], fitting_slot))

            print("fitted next slot")
            # Recurse to the next course on the list
            self.backtrack(available, index + 1)

            # Backtrack: remove the last added course and the corresponding slots from available
            self.selected.pop()
            self.removeTable(available, nextCourse, fitting_slot)

        print("trying next course")
        # If slot couldn't fit, skip it and then try with the next course
        self.backtrack(available, index + 1)



# base = Algorithm(json.load(open(r"core\ffcs\final.json")),morning=True,creditsRequired=27)
# print(base.results)
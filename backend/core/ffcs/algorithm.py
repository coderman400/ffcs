import json

from config import ROOT_DIR

slots_json = ROOT_DIR / "core" / "ffcs" / "slots.json"
# slots_json = "core/ffcs/slots.json"

class Algorithm:
    def __init__(self,data):
        self.data = data
        self.selected = []
        self.results = []
        self.courses_list = self.prep_courses_list()
        self.available = self.prep_available_slots()
        self.sts_preference = 0
        self.backtrack(self.available,0)
        self.write()
        self.results = self.sample(6)


    def write(self):
        text = "\n".join([f"{result}," for result in self.results])
        with open("output.txt", "w") as file:
            file.write(text)

    def sample(self,k):
        length = len(self.results)
        partition = length // k
        return [self.results[i] for i in range(0, length, partition)][:k]


    def prep_courses_list(self):
        courses_list = []
        for course_code, course_info in self.data.items():
            slots = set()
            for professor, slot_list in course_info['professors'].items():
                for slot in slot_list:
                    slots.add(tuple(slot))  # Convert list to tuple for set uniqueness
            courses_list.append((course_code, list(slots)))
        return courses_list
    
    def prep_available_slots(self):
        with open(str(slots_json), 'r') as file:
            raw_slots_dict = json.load(file)

        # Parse keys and values to a dictionary of tuples
        available = {tuple(key.strip("()").split(", ")): value for key, value in raw_slots_dict.items()}
        return available

    # Function to check if a course can fit in available slots
    def fittable(self,available, course):
        for slot in course[1]:
            # Split sections and time slots based on '+'
            sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
            sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

            # Check if all sections and sub-slots are free in `available`
            sections_available = all(
                any(section in key and available[key] == '' for key in available) for section in sections
            )
            sub_slots_available = all(
                any(sub_slot in key and available[key] == '' for key in available) for sub_slot in sub_slots
            )

            # # Ensure that none of the sections or sub-slots conflict
            conflicting_sections = any(
                section in key and available[key] != '' for key in available for section in sections
            )
            conflicting_sub_slots = any(
                sub_slot in key and available[key] != '' for key in available for sub_slot in sub_slots
            )

            # If both sections and sub-slots are available and not conflicting, consider this slot as fittable
            if sections_available and sub_slots_available and not (conflicting_sections or conflicting_sub_slots):
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
            if any(section in key for section in sections) or any(sub_slot in key for sub_slot in sub_slots):
                available[key] = course_code  # Mark this key as occupied by the course code

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
                        if (slot[0][1] == "2") == (self.sts_preference == 1)  # Check second character for morning/afternoon
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

                    return  # Return after processing the STS course to avoid skipping it

        # Check the base condition: Total credits should equal 27
        if self.calculateCredits(self.selected) == 27:
            self.results.append(list(self.selected))  # Store a copy of the current selection
            return

        # No more courses to select if index exceeds list length
        if index >= len(self.courses_list):
            return

        # Obtain the next course to evaluate from the list
        nextCourse = self.courses_list[index]

        # Try to fit the next course into available slots
        fitting_slot = self.fittable(available, nextCourse)
        if fitting_slot:
            # If fitting slot is found, add course to selected and update slots of available
            self.updateTable(available, nextCourse, fitting_slot)
            self.selected.append((nextCourse[0], fitting_slot))

            # Recurse to the next course on the list
            self.backtrack(available, index + 1)

            # Backtrack: remove the last added course and the corresponding slots from available
            self.selected.pop()
            self.removeTable(available, nextCourse, fitting_slot)

        # If slot couldn't fit, skip it and then try with the next course
        self.backtrack(available, index + 1)




# final = r"core/ffcs/final.json"
# base = Algorithm(json.load(open(final,"r")))
# print(len(base.results))
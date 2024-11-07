import json

# from config import HERE

class CourseScheduler:
    def __init__(self, morning:bool, credits_required, data, slots_file="core/ffcs/slots.json"):
        # HERE(__file__,self.__init__)
        self.morning = morning
        self.credits_required = credits_required

        # Load courses and slots from JSON files
        self.data = data

        with open(slots_file, 'r') as file:
            raw_slots_dict = json.load(file)

        # Initialize available slots table
        self.available = {tuple(key.strip("()").split(", ")): value for key, value in raw_slots_dict.items()}

        self.selected = []  # Selected courses
        self.results = []   # Store final results
        self.time_clash = [
            'L4', 'L10', 'L16', 'L22', 'L28',
            'L5', 'L11', 'L17', 'L23', 'L29',
            'L34', 'L40', 'L46', 'L52', 'L58',
            'L35', 'L41', 'L47', 'L53', 'L59',
            'L36', 'L42', 'L48', 'L54', 'L60'
        ]

        # Prepare courses_list as a list of tuples (course_code, sorted_unique_slots)
        self.courses_list = []
        self.mandatory_courses_list=[]
        self.projects_list=[]
        non_mandatory_courses_list=[]
        for course_code, course_info in self.data.items():
            
            slots = set()
            for professor, slot_list in course_info['professors'].items():
                for slot in slot_list:
                    slots.add(tuple(slot))  # Convert list to tuple for set uniqueness

            # Sort the slots using the custom key based on morning preference
            sorted_slots = sorted(slots, key=self.sort_key)
            if(course_info['mandatory']):
                self.mandatory_courses_list.append((course_code, list(sorted_slots)))
            if(not course_info['mandatory']):
                non_mandatory_courses_list.append((course_code, list(sorted_slots)))
            if(course_info['project']):
                self.projects_list.append((course_code, list(sorted_slots)))

        self.courses_list = self.mandatory_courses_list + non_mandatory_courses_list

    # Function to generate a sorting key based on the `morning` preference
    def sort_key(self, slot):
        section = slot[0]
        if self.morning:
            if section[-1] == '1':
                return (0, section)
            elif section[-1] == '2':
                return (1, section)
        else:
            if section[-1] == '2':
                return (0, section)
            elif section[-1] == '1':
                return (1, section)

        return (2, section)

    def fittable(self, available, course):
        fittableSlots = []
        for slot in course[1]:
            sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
            sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

            conflicting_sections = any(
                section in key and available[key] != '' for key in available for section in sections
            )
            conflicting_sub_slots = any(
                sub_slot in key and available[key] != '' for key in available for sub_slot in sub_slots
            )

            clashes = False
            for section in sections:
                for slotTuple in available:
                    if slotTuple[0] == section:
                        lab_slot = slotTuple[1]
                        next_lab_slot = f"{lab_slot[0]}{int(lab_slot[1:]) + 1}"
                        if next_lab_slot in self.time_clash:
                            for eachTuple in available:
                                if len(eachTuple) > 1 and eachTuple[1] == next_lab_slot:
                                    break
                            if 'LAB' in available[eachTuple]:
                                clashes = True

            for sub_slot in sub_slots:
                if sub_slot in self.time_clash:
                    prev_lab_slot = f"{sub_slot[0]}{int(sub_slot[1:]) - 1}"
                    for slotTuple in available:
                        if slotTuple[1] == prev_lab_slot:
                            break
                    if 'THEORY' in available[slotTuple]:
                        clashes = True

            if not (conflicting_sections or conflicting_sub_slots or clashes):
                fittableSlots.append(slot)

        return fittableSlots

    def update_table(self, available, course, slot):
        course_code = course[0]
        sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
        sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

        for key in available:
            if any(section in key for section in sections):
                available[key] = f"{course_code} THEORY"

            if any(sub_slot in key for sub_slot in sub_slots):
                available[key] = f"{course_code} LAB"

    def remove_table(self, available, course, slot):
        sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
        sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

        for key in available:
            if any(section in key for section in sections) or any(sub_slot in key for sub_slot in sub_slots):
                available[key] = ''

    def calculate_credits(self, selected):
        total_credits = 0
        seen_courses = set()

        for course_code, slot in selected:
            if course_code in seen_courses:
                continue

            seen_courses.add(course_code)
            slot_credits = 0
            sections = slot[0].split("+") if "+" in slot[0] else [slot[0]]
            sub_slots = slot[1].split("+") if len(slot) > 1 and "+" in slot[1] else [slot[1]] if len(slot) > 1 else []

            for section in sections:
                slot_credits += 1 if section.startswith("T") else 2

            for sub_slot in sub_slots:
                if sub_slot.startswith("L"):
                    slot_credits += 0.5

            if course_code.startswith("STS"):
                slot_credits = 1
            
            if course_code in [course_code for course_code,_ in self.projects_list]:
                slot_credits += 1

            total_credits += slot_credits

        return total_credits

    def backtrack(self, index,depth=0):
        MAX_DEPTH =  200
        if len(self.results) == 120 or depth>MAX_DEPTH:
            return
        if self.calculate_credits(self.selected) >= self.credits_required and self.calculate_credits(self.selected) <= 27:
    
            morningSlots = sum(1 for courseTuple in self.selected if courseTuple[1][0][1] == '1')
            afternoon = len(self.selected) - morningSlots
            if (not self.morning and afternoon - morningSlots >= 2) or (self.morning and morningSlots - afternoon >= 2):
                if all(mandatory_course[0] in [selected[0] for selected in self.selected] for mandatory_course in self.mandatory_courses_list):
                    self.results.append(list(self.selected))
                    return

        if index >= len(self.courses_list):
            return

        if not any(course[0].startswith("STS") for course in self.selected):
            for idx, course in enumerate(self.courses_list):
                if course[0].startswith("STS"):
                    fitting_slots = self.fittable(self.available, course)
                    if(len(fitting_slots)>0):
                        self.update_table(self.available,course,fitting_slots[0])
                        self.selected.append((course[0], fitting_slots[0]))

        next_course = self.courses_list[index]
        
        if(next_course[0].startswith("STS")):
            self.backtrack(index+1, depth + 1)
        else:
            fitting_slots = self.fittable(self.available, next_course)
            if len(fitting_slots) > 0:
                for fitting_slot in fitting_slots:
                    self.update_table(self.available, next_course, fitting_slot)
                    self.selected.append((next_course[0], fitting_slot))
                    self.backtrack(index + 1,depth + 1)
                    self.selected.pop()
                    self.remove_table(self.available, next_course, fitting_slot)

            self.backtrack(index + 1, depth + 1)

    def generate_schedules(self):
        self.backtrack(0)
        return self.results

# Example usage
# with open("restructured_data.json","r") as file:
#     data = json.load(file)


# scheduler = CourseScheduler(morning=False, credits_required=21, data=data)
# results = scheduler.generate_schedules()

# # Display results
# if results:
#     for idx, res in enumerate(results):
#         print(f"Result {idx + 1}: {res}")
# else:
#     print("Impossible")

# results = "\n".join([f"{result}," for result in results])

# with open('result.txt', 'w') as f:
#     f.write(results)

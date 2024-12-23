
class Response:
    def __init__(self,data,base,projects):
        self.results = data
        self.base = base
        self.projects_list = projects
        self.samples = self.sample(30)
        self.response = self.make_response(self.samples)
        

    def sample(self,sample_size):
        """Sample k timetables from the results"""
        if len(self.results) > 0:
            length = len(self.results)
            if length > sample_size:
                partition = length// sample_size
            else:
                partition = 1
            return [self.results[i] for i in range(0, length, partition)][:sample_size if length > sample_size else length]
        else:
            return []
    
    def get_course(self,course_code):
        """Get the course details from the base"""
        for course in self.base:
            if course["code"] == course_code:
                return course
            
    def make_response(self,data):
        """Structure the data for the response"""
        if not data:
            return {"slots":[]}
        final = {"slots" : []}
        flatten = lambda data : [(x,"+".join(y).split("+")) for x,y in data]

        for index,timetable in enumerate(data):
            credits = self.calculate_credits(timetable,self.projects_list)
            data = flatten(timetable)
            response = {slot:course for course,slots in data for slot in slots}
            info = []
            
            for course_code,slot in self.samples[index]:
                course = self.get_course(course_code)
                info.append({"slot":slot,"title":course["title"],"code":course["code"]})
            response["info"] = info
            response["credits"] = credits

            final["slots"].append(response)

        return final
    
    def calculate_credits(self, selected,projects):
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

            if course_code in [course_code for course_code in self.projects_list]:
                slot_credits += 1

            total_credits += slot_credits

        return total_credits
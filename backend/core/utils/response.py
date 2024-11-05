
class Response:
    def __init__(self,data,base):
        self.results = data
        self.base = base
        self.samples = self.sample(30)
        print(self.samples)
        self.response = self.make_response(self.samples)

    def sample(self,k):
        """Sample k timetables from the results"""
        length = len(self.results)
        partition = (length//2) // k
        return [self.results[i] for i in range(0, length, partition)][:k]    
    
    def get_course(self,course_code):
        """Get the course details from the base"""
        for course in self.base:
            if course["code"] == course_code:
                return course
            
    def make_response(self,data):
        """Structure the data for the response"""
        final = {"slots" : []}
        flatten = lambda data : [(x,"+".join(y).split("+")) for x,y in data]

        for index,timetable in enumerate(data):
            data = flatten(timetable)
            response = {slot:course for course,slots in data for slot in slots}
            info = []
            
            for course_code,slot in self.samples[index]:
                course = self.get_course(course_code)
                info.append({"slot":slot,"title":course["title"],"code":course["code"]})
            response["info"] = info

            final["slots"].append(response)

        return final
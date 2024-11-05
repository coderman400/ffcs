
class Response:
    def __init__(self,data):
        self.results = data
        self.sample = self.sample(30)
        self.response = self.make_response(self.sample)

    def sample(self,k):
        """Sample k timetables from the results"""
        length = len(self.results)
        partition = (length//2) // k
        return [self.results[i] for i in range(0, length, partition)][:k]    
    
    def make_response(self,data):
        """Structure the data for the response"""
        final = {"slots" : []}
        flatten = lambda data : [(x,"+".join(y).split("+")) for x,y in data]

        for timetable in data:
            data = flatten(timetable)
            response = {slot:course for course,slots in data for slot in slots}
            final["slots"].append(response)

        return final
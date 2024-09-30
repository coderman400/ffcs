from ..ffcs.algorithm import Algorithm
import json

class Pipeline:
    def __init__(self,data = None,morning=True,creditsRequired=27):
        self.data = data
        print(self.data.keys())
        self.results = []
        self.base = Algorithm(self.data,
                            morning=morning,
                            creditsRequired=creditsRequired)
        self.results += self.base.results
        print(len(self.results))

        self.sample = self.sample(6)
        self.response = self.make_response(self.sample)
        print(self.response)

    def sample(self,k):
        length = len(self.results)
        partition = length // k
        return [self.results[i] for i in range(0, length, partition)][:k]    
    
    def make_response(self,data):
        final = {"slots" : []}
        flatten = lambda data : [(x,"+".join(y).split("+")) for x,y in data]

        for timetable in data:
            data = flatten(timetable)
            response = {slot:course for course,slots in data for slot in slots}
            final["slots"].append(response)
        print(len(final["slots"]))
        return final
    

# with open(r"core\ffcs\final.json",'r') as f:
#     data = json.load(f)

# base = Pipeline(data=data)


# image_paths = ['C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\1.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\2.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\3.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\4.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\5.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\6.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\7.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\8.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\9.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\10.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\11.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\12.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\13.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\14.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\15.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\16.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\17.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\18.jpg', 'C:\\Users\\laksh\\OneDrive\\Desktop\\Web Development\\FFCS\\backend\\uploads\\19.jpg']

# base = Pipeline(image_paths=image_paths)
# print(base.response)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Slot
from .forms import CourseForm,SlotsForm
from .serializers import CourseSerializer, SlotSerializer
from django.views.decorators.csrf import csrf_exempt
import pprint
import re

class CourseView(APIView):

    pretty = lambda self,msg :[pprint.pprint(msg),print("\n")]

    def get(self,request):
        courses = Course.objects.all()
        data = {
            "courses" : [
                {
                "code" : course.code,
                "title": course.title,
                "slots" : [{
                    "prof" : slot.prof,
                    "theory_slots" : slot.theory_slots,
                    "lab_slots" : slot.lab_slots
                    } for slot in Slot.objects.filter(course=course) ]
                } for course in courses
            ]
        }
        return Response(data,status=status.HTTP_200_OK)

    def post(self,request):
        self.session_courses:list[Course] = []
        data = request.data 
        courses = data["courses"]
        self.pretty(courses)
        for course in courses:
            saved_course = self.save_course(course)
            if not isinstance(saved_course,Course):
                return saved_course
            self.session_courses.append(saved_course)
            
            for slot_set in course["slots"]:
                saved_slot = self.save_slot(saved_course,slot_set)
                if not isinstance(saved_slot,Slot):
                    return saved_slot
        return Response("Success",status=status.HTTP_201_CREATED)
    
    def save_course(self,course):
        course_data = {
            "title" : course["title"],
            "code" : course["code"]
        }
        form = CourseForm(course_data)

        if form.is_valid():     
            instance, created = Course.objects.get_or_create(**form.cleaned_data)
            return instance
        elif "Course with this Code already exists." in form.errors.get("code",[]):
            return Course.objects.get(code = course["code"])
        else:
            return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def save_slot(self,course,slot_set):
        theory_slots,lab_slots = self.split_slots(slot_set["slots"].split(","))
        slots_data = {
            "course" : course.code,
            "prof" : slot_set["prof"],
            "theory_slots" : theory_slots,
            "lab_slots" : lab_slots,
        }
        form = SlotsForm(slots_data)

        if form.is_valid():
            slot = Slot.objects.create(**form.cleaned_data)
            return slot
        elif "Slot with this Course and Prof already exists." in form.errors.get("__all__",[]):
            return Slot.objects.get(course=course.code,prof=slot_set["prof"])
        else:
            return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)
        


    def split_slots(self,slots:list):
        pattern = r"^L[1-9][0-9]?(\+L[1-9][0-9]?){1,6}$"
        isLabSlot = lambda slot : re.match(pattern,slot)
        lab_slots = [i for i in slots if isLabSlot(i)]
        theory_slots = [i for i in  slots if i not in lab_slots]

        return (theory_slots,list(lab_slots))

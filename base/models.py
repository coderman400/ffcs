from django.db import models


class CourseType(models.TextChoices):
    PROGRAM_CORE = "PC","program core"
    PROGRAM_ELECTIVE = "PE","program elective"
    UNI_CORE = "UC","university core"
    UNI_ELECTIVE = "UE","university elective"
    LANGUAGE = "FLP","foreign language basket"
    SOFTSKILLS = "STS","softskills"

class EmbeddedStatus(models.TextChoices):
    ETL = "ETL","Embedded Theory and Lab"
    TH = "TH","Theory only"
    LO = "LO","Lab only"

class Course(models.Model):
    code = models.CharField(max_length=8,primary_key=True)
    title = models.CharField(max_length=100,blank=True)
    course_type = models.CharField(
        max_length=3,
        choices=CourseType.choices,
        default=CourseType.PROGRAM_CORE,
        blank=True,
    )
    embedded_status = models.CharField(
        max_length=3,
        choices=EmbeddedStatus.choices,
        default=EmbeddedStatus.ETL,
        blank=True,
    )

    def __str__(self) -> str:
        return  f"{self.code}:{self.title}"
    
class Slot(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="slots")
    prof = models.CharField(max_length=100)
    theory_slots = models.JSONField(blank=True,default=list,null=True)
    lab_slots = models.JSONField(blank=True,default=list,null=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course', 'prof'], name='unique_course_prof')
        ]
    def __str__(self) -> str:
        return f"{self.course.code} -> {self.prof}"

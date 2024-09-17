from rest_framework import serializers
from .models import Course, Slot

class CourseSerializer(serializers.ModelSerializer):
    slots = serializers.SerializerMethodField()  # Use a method to include slots

    class Meta:
        model = Course
        fields = ['code', 'title', 'slots']

    def get_slots(self, obj):
        # Serialize related slots using SlotSerializer
        slots = Slot.objects.filter(course=obj)
        return SlotSerializer(slots, many=True).data

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['course','prof','theory_slots','lab_slots']

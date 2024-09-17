from django.urls import path
from .views import CourseView

urlpatterns = [
    path('courses/', CourseView.as_view(), name='course-list'),
    # Add other URL patterns here
]

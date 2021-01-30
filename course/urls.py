from django.urls import path
from course import views 
urlpatterns = [
    path('androidCourse',views.android_course),
    path('webCourse',views.web_course),
]

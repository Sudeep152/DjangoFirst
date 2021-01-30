from django.urls import path
from fees import views

urlpatterns = [
    path('androidFee',views.androidfee),
    path('webfee',views.webfee),
]

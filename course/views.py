from django.shortcuts import render

# Create your views here.
def android_course(request):
    return render(request,'course/android.html')

def web_course(request):
    return render(request,'course/web.html')
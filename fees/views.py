from django.shortcuts import render

# Create your views here.
def androidfee(request):
    return render(request,'fees/androidfee.html')

def webfee(request):
    return render(request,'fees/webfee.html')
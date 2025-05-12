from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Home/home.html')

def changepass(request):
    return render(request, 'Home/changepass.html')
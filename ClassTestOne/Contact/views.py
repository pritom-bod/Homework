from django.shortcuts import render

# Create your views here.
def Contact(request):
    return render(request, 'Contact/contact.html')

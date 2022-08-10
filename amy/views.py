from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, "amy/index.html")

def all_attendees(request):
	return render(request, "amy/security.html")
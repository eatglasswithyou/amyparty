from django.shortcuts import render
from .models import Attendee

# Create your views here.

def index(request):
	return render(request, "amy/index.html")

def all_attendees(request):
	attendees = Attendee.objects.all()
	return render(request, "amy/security.html", {
		"attendees": attendees
		})

def thanks(request):
	return render(request, "amy/thanks.html")
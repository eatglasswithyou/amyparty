from django.shortcuts import render
from django.http import JsonResponse

from .models import Attendee
from django.views.decorators.csrf import csrf_exempt

import pdb
# Create your views here.

def index(request):
	return render(request, "amy/index.html")

def all_attendees(request):
	attendees = Attendee.objects.all()
	return render(request, "amy/security.html", {
		"attendees": attendees
		})

@csrf_exempt
def thanks(request):
	print(request)
	try:
		if request.method == "POST":
			att = Attendee(title=request.POST.get('name', 'no'),
				email = request.POST.get('email', 'no'),
				size = request.POST.get('count', 'no'),
				rsvp = request.POST.get('att', 'no'),
				consent = request.POST.get('covid', 'no'))
			print(att)
			att.save()
			return JsonResponse({'type': 'success'})
	except Exception as e:
		return JsonResponse({'type': 'error', 'reason': str(e)})
			
		

	return render(request, "amy/thanks.html")
from django.shortcuts import render

# Create your views here.
from .models import User

def home(request):
	
	if request.method == 'GET':
		# Serve blank page 
		return render(request, 'home.html')
	else:
		# method == POST 
		

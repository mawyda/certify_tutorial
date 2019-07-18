# views.py

from django.shortcuts import render

from random import randint, choice 
import string 

def home(request):
	return render(request, 'home.html')
	
def access(request):
	firstname = request.GET['firstname']
	lastname = request.GET['lastname']
	fullname = (firstname + ' ' + lastname).title()
	status, code = get_status()
	
	return render(request, 'access.html', {'data': fullname,
											'status': status,
											'code': code}
										)

def get_status():
	rando = randint(1, 10)
	if rando % 2 == 0:
		code = access_code()
		return 'GRANTED', code
	else:
		return 'DENIED', ''

def access_code():
	'''Generates random access code'''
	selection = string.ascii_lowercase + string.digits 
	code = ''
	for i in range(10):
		code += choice(selection)
	
	print(code)
	return code 

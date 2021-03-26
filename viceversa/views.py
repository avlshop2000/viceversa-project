from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('This is about page!')

def home(request):
	return render(request, 'home.html')

def reverse(request):
	get_my_text = request.GET['usertext']
	# print (get_my_text)
	reverse_text = get_my_text[::-1]
	return render(request, 'reverse.html', {'usertext': get_my_text, 'reversedtext': reverse_text})
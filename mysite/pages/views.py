from django.shortcuts import render

#function for the main page
def mainPage(request):
	return render(request, 'about.html')

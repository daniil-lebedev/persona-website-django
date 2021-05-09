from django.shortcuts import render
from .models import Blogs
#main page
def blogPage(request):
	"""rendering the webpae with db queries"""
	blogs = Blogs.objects.all()
	context =  {"blogs":blogs}
	return render(request, 'blog.html', context)

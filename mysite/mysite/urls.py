from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	#url for the main page
	path('', include('pages.urls')),

	#url for the blogs page
	path('blog/', include('blog.urls')),

	#url for the admin page
    path('admin/', admin.site.urls),
]

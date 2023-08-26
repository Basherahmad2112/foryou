
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from  django.urls  import  path, include # new

urlpatterns = [
	path('', include('blog.urls')),  #new
	path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
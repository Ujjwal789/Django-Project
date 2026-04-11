
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Views.home, name = 'Home'),
    path('about/',Views.about, name = 'about'),
    path('contact/', Views.contact, name = 'contact'),
     path('first/', include('first.urls')),
     path("__reload__/", include("django_browser_reload.urls")),
    #  path('', include('first.urls')), to enclude the urls of the main app 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

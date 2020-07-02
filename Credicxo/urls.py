from django.contrib import admin
from django.urls import path,include
import banks
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('banks/',include('banks.api_urls'))
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

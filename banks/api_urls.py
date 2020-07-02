from django.contrib import admin
from rest_framework import routers
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path,include
from .views import *

urlpatterns = [
    path('read_all_data_from_csv/',test),
    path('get_branch_by_ifsc/',getBranchDetailsByIFSC.as_view()),
    path('get_branch_by_bank_name_and_city/',getBranchDetailsByBankNameAndCity.as_view()),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
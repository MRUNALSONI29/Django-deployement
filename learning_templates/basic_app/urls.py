from basic_app import views
from django.urls import re_path

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^other/',views.other,name='other'),
    re_path(r'^relative/',views.relative,name='relative')
]

from django.contrib import admin
from django.urls import path

from . import views

app_name="matrimony"

urlpatterns = [
    path('', views.ProfileListView, name='profile_list'),
    path('<int:profile_id>', views.ProfileDetailView, name='profile_detail'),
    path('<int:profile_id>/delete', views.ProfileDeleteView, name='delete'),
    path('contact', views.ContactView, name='contact'),
    path('new_profile', views.ProfileFormView, name='new_profile'),
    path('father_profile', views.FatherProfileView, name='father_profile'),

]
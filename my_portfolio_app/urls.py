from django.urls import path
from .views import home,list_projects,ContactView,about

urlpatterns = [
    path('',home,name='home'),
    path('projects',list_projects,name='list_projects'),
    path('contact',ContactView.as_view(),name='contact'),
    path('about',about,name='about'),
]

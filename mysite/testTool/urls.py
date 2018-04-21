from django.urls import path
from . import views

# app_name = 'testTool'
urlpatterns = [
    path('', views.index),
    path('student/submit/', views.confirm_action, name='confirm_action'),
    path('student/submit/successful/', views.submit_page, name='submit_action'),
]
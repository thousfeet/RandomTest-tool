from django.urls import path, include

from testTool import views

urlpatterns = [
    path('', views.index)
]
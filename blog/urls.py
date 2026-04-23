from django.urls import path
from . import views

#create a list of url patterns that when a url is visited it is tied to a function call

urlpatterns = [
    path('', views.post_list,name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'), 
]
from django.urls import path

from .views import DoctorsView, UsersView, TestView

app_name = 'data'
urlpatterns = [
    path('doctors/', DoctorsView.as_view()),
    path('users/', UsersView.as_view()),
    path('test/', TestView.as_view()),

]

from django.urls import path
from profiles_api import views

urlpatterns = [
    path('example-view/', views.ExampleApiView.as_view()),
]
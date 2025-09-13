from django.urls import path, include 

from rest_framework.routers import DefaultRouter

# from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('example-viewset', views.ExampleViewSet, base_name='example-viewset')

# router = DefaultRouter()
# router.register('example-viewset' views.ExampleViewSet, base_name="example-viewset")

urlpatterns = [
    path('example-view/', views.ExampleApiView.as_view()),
    path('', include(router.urls))
]
"""categoriestree app URL Configuration"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from categoriestree import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)

app_name = 'categoriestree'
urlpatterns = [
    path('', include(router.urls)),
]

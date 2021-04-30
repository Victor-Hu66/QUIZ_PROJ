from django.urls import path
from .views import Category

urlpatterns = [
    path("", Category.as_view(), name="category"), #take__init hatası alıyorsak as_view eksiktir..
]
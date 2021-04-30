from django.urls import path
from .views import CategoryList, CategoryDetail, QuizDetail

urlpatterns = [
    path("", CategoryList.as_view(), name="category"), #take__init hatası alıyorsak as_view eksiktir..
    path("<category>", CategoryDetail.as_view(), name="category-detail"),
    path("question/<title>", QuizDetail.as_view(), name="question"),
]


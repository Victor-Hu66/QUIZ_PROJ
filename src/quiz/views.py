from django.shortcuts import render
from rest_framework import generics
from .models import Category, Quiz, Question
from .serializers import CategorySerializer, CategoryDetailSerializer, QuestionSerializer
class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    
    def get_queryset(self):  #queryset i override ettik
        queryset = Quiz.objects.all()
        category = self.kwargs["category"] #backend, frontend 
        queryset = queryset.filter(category__name=category) # __ child modelinden parenta ulaşmak için
        return queryset
class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(quiz__title=title)
        return queryset
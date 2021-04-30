from django.shortcuts import render
from rest_framework import generics
from .models import Category, Quiz
from .serializers import CategorySerializer, CategoryDetailSerializer
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
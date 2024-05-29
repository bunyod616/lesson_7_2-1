from django.shortcuts import render
from rest_framework.response import Response
from .serializers import CategoryProductSerializers, ProductSerializers
from .models import Category, Product
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# Create your views here.


class ListCreateCategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryProductSerializers


class RetrieveCategoryAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryProductSerializers


class UpdateCategoryAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryProductSerializers


class DeleteCategoryAPIView(DestroyAPIView):
    queryset = Category.objects.all()


#Boogs viewlari

class ListCreateProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class RetrieveProductAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class UpdateProductAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class DeleteProductAPIView(DestroyAPIView):
    queryset = Product.objects.all()

















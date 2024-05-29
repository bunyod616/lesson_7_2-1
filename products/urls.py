from django.urls import path
from .views import (
    ListCreateCategoryAPIView,
    RetrieveCategoryAPIView,
    UpdateCategoryAPIView,
    DeleteCategoryAPIView,
    ListCreateProductAPIView,
    RetrieveProductAPIView,
    UpdateProductAPIView,
    DeleteProductAPIView
)

urlpatterns = [
    path('categories/', ListCreateCategoryAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', RetrieveCategoryAPIView.as_view(), name='category-retrieve'),
    path('categories/<int:pk>/update/', UpdateCategoryAPIView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', DeleteCategoryAPIView.as_view(), name='category-delete'),
    # path('categories/<int:pk>/', RetrieveUpdateDestroyCategoryAPIView.as_view(), name='category-detail'),
    # path('goods/<int:pk>/', RetrieveUpdateDestroyGoodsAPIView.as_view(), name='goods-detail'),
    path('goods/', ListCreateProductAPIView.as_view(), name='goods-list-create'),
    path('goods/<int:pk>/', RetrieveProductAPIView.as_view(), name='goods-retrieve'),
    path('goods/<int:pk>/update/', UpdateProductAPIView.as_view(), name='goods-update'),
    path('goods/<int:pk>/delete/', DeleteProductAPIView.as_view(), name='goods-delete'),
]
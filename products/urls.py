from django.contrib import admin
from django.urls import include, path

from products.views import GetAllProductsApiView, AddProductApiView, GetProductByIDApiView, GetProductsBySearchApiView

urlpatterns = [
    path('getallproducts/', GetAllProductsApiView.as_view()),
    path('getproduct/<id>', GetProductByIDApiView.as_view()),
    path('getproducts/search/', GetProductsBySearchApiView.as_view()),
    path('addproduct/', AddProductApiView.as_view())
]

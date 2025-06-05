from django.urls import path
from catalog.views import (HomeView, ContactsView, ProductDetailView, ProductCreateView, ProductDeleteView,
                           ProductUpdateView)
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
]

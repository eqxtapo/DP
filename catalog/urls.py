from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (HomeView, ContactsView, ProductDetailView, ProductCreateView, ProductDeleteView,
                           ProductUpdateView, CategoryListView, ProductsByCategoryListView)
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_details'),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("category/", CategoryListView.as_view(), name="category"),
    path("category/<str:category_name>/",ProductsByCategoryListView.as_view(),name="products_by_category"),
]

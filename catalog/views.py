from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, UpdateView
from catalog.models import Product, Category
from catalog.forms import ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from catalog.service import get_products_from_cache, get_products_by_category


class HomeView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()

class ContactsView(LoginRequiredMixin, TemplateView):
    template_name = "catalog/contacts.html"


class CategoryListView(ListView):
    """Страница категории"""

    model = Category
    template_name = "catalog/categories_list.html"


class ProductsByCategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get(self, request, category_name):
        category_name = get_object_or_404(Category, name=category_name)
        products = get_products_by_category(category_name)

        return render(
            request,
            "catalog/products_by_category.html",
            {"catalog": category_name, "products": products},
        )


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied("У Вас отсутствуют права, обратитесь к администратору!")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied("У Вас отсутствуют права, обратитесь к администратору!")


    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied("У Вас отсутствуют права, обратитесь к администратору!")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied
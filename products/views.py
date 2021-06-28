from django.shortcuts import render

from products.models import Product, ProductCategory
from common.views import CommonContextMixin

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

# функции = контроллер = представления = вьюшки/вьюхи


class ProductIndexView(CommonContextMixin, TemplateView):
    title = 'GeekShop'
    template_name = 'products/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductIndexView, self).get_context_data(**kwargs)
        context['header'] = 'GeekShop Store'
        return context


class ProductsListView(CommonContextMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'GeekShop - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

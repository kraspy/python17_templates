from django.views.generic import ListView, DetailView

from .models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

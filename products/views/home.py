from django.shortcuts import render
from products.models import Product


def home(request):

    featured_products = Product.objects.filter(is_featured=True)

    context = {
        "products": featured_products,
    }

    return render(request, "home.html", context)
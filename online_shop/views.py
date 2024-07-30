from django.shortcuts import render
from online_shop.models import Product


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'online_shop/home.html', context)


def product_detail(request, id):
    product = Product.objects.get(pk=id)
    products = Product.objects.exclude(pk=id)
    context = {
        'products': products,
        'product': product,
    }
    return render(request, 'online_shop/detail.html', context)


from django.shortcuts import render, get_object_or_404
from online_shop.models import Product


def online_shop(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = product.comments.all()
    return render(request, 'online_shop/detail.html', {
        'product': product,
        'comments': comments,
    })

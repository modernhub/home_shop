from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from app.settings import GOODS_ON_PAGE

from goods.models import Products


def catalog(request, category_slug):
    page = request.GET.get('page', 1)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, GOODS_ON_PAGE)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Home - Каталог',
        'goods': current_page,  
        'slug_url':category_slug
    }
    return render(request, "goods/catalog.html", context=context)


def product(request, product_slug = False, product_id = False):
    if product_id:
        product = Products.objects.get(id=product_id)
        context = {
        'product': product
        }
    else:
        product = Products.objects.get(slug=product_slug)
        context = {
            'product': product
        }

    return render(request, "goods/product.html", context=context)

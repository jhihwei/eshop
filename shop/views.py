from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Page_Content, Product
from vip.models import VIP_User
from django.views.decorators.csrf import csrf_exempt

def category_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop_v2/category/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

@csrf_exempt
def product_list(request, category_slug='enzyme', vip_class='z', ):
    products = Product.objects.filter(available=True)
    category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)
    if request.method == 'POST':
        print(request.POST.get('line_id'))
        vip_user = VIP_User.objects.filter(line_id = request.POST.get('line_id')).exists()
        if vip_user:
            for i, p in enumerate(products):
                products[i].price = int(products[i].price) *0.2

    return render(request, 'shop_v2/category/product/list.html',
                  {'products': products})
def vip(request):
    return render(request, 'shop_v2/vip.html')

def vip_product_list(request, category_slug='enzyme', vip_class='a'):
    products = Product.objects.filter(available=True)
    category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)
    for i, p in enumerate(products):
        products[i].price = int(products[i].price) *0.2
    return render(request, 'shop_v2/category/product/list.html',
                  {'products': products,
                   'discount': 0.3})


def product_detail(request, product_id, slug, vip_class='z'):
    product = get_object_or_404(Product,
                                id=product_id,
                                slug=slug,
                                available=True)
    if vip_class is not 'z':
        product.price = int(product.price) *0.2

    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop_v2/category/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def page_content(request, slug=1):
    page_content = get_object_or_404(Page_Content, slug=slug)
    return render(request,
                  'shop_v2/page_content.html',
                  {'page_content': page_content})

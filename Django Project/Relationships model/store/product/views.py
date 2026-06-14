from django.shortcuts import render, get_object_or_404
from product.models import Product
# Create your views here.
def product_list_page(request):
    product = Product.objects.all()
    return render(request, 'product/product_list.html', {
        'products':product
    })

# def details_page(request, id):
#     details = get_object_or_404(Product,pk = id)
#     return render(request, 'product/details_page.html')
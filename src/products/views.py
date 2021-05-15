from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = { 
        'form': form
    }
    return render(request, "products/product_create.html", context)

#Raw HTML Form
# def product_create_view(request):
#     context = {}
#     return render(request, "products/product_create.html", context)


#pure Django Form
# def product_create_view(request):
#     my_from = RawProductForm()
#     if request.method == "POST":
#         my_from = RawProductForm(request.POST)
#         if my_from.is_valid():
#             Product.objects.create(**my_from.cleaned_data)
#             my_from = RawProductForm()
#         else:
#             print(my_from.errors)
#     context = {
#         "form": my_from
#     }
#     return render(request, "products/product_create.html", context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

  
def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


#initial values for forms

def render_initial_data(request):
    initial_data={
        'title' : "initial title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)
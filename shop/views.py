from .forms import CategoryForm, ProductForm, WarrantyForm, CustomerForm, OrderForm
from .models import Category, Product, Warranty, Customer, Order
from django.shortcuts import render, redirect
def home(request):
    return render(request, "shop/home.html")

def catalog(request):
    return render(request, "shop/catalog.html")

def about(request):
    return render(request, "shop/about.html")

def categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm()
    items = Category.objects.all()
    return render(request, "shop/categories.html", {"form": form, "items": items})

def products(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()
    items = Product.objects.all()
    return render(request, "shop/products.html", {"form": form, "items": items})
def warranties(request):
    if request.method == "POST":
        form = WarrantyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("warranties")
    else:
        form = WarrantyForm()
    items = Warranty.objects.all()
    return render(request, "shop/warranties.html", {"form": form, "items": items})
def customers(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customers")
    else:
        form = CustomerForm()
    items = Customer.objects.all()
    return render(request, "shop/customers.html", {"form": form, "items": items})
def orders(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("orders")
    else:
        form = OrderForm()
    items = Order.objects.all()
    return render(request, "shop/orders.html", {"form": form, "items": items})
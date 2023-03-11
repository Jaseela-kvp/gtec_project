from django.shortcuts import render
from main.models import Category,Product

# Create your views here.
def index(request):
    categories = Category.objects.all().order_by('name')   
    products = Product.objects.all().order_by('name')   

    return render(request,'index.html', {'categories': categories})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def shop(request):
    return render(request,'shop.html')

def shopSingle(request):
    return render(request,'shopSingle.html')
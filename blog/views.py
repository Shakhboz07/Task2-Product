from django.shortcuts import redirect, render
from blog.forms import ProductModelForm

from blog.models import Products

# Create your views here.

def index_page(request):
    product = Products.objects.all()
    context = {
        "products":product
    }
    return render(request, 'index.html',context)

def form_page(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        form.is_valid()
        form.save()
        return redirect('index_page')
    return render(request, 'form.html')
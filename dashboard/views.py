from django.shortcuts import render,redirect 
from django.contrib.auth.decorators import login_required 
from .models import Product , Order
from .forms import ProductForm ,OrderForm
from django.contrib.auth.models import User 
from django.contrib import messages 



# Create your views here.
@login_required 
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else :
        form = OrderForm()
    
    
    context = {
        'orders':orders,
        'form':form,
        'products':products,
    }
    return render(request,'dashboard/index.html',context)

@login_required  
def staff(request):
    workers=User.objects.all()
    workers_count = workers.count()
    context = {
        'workers':workers,
        'workers_count':workers_count,
    }
    return render(request,'dashboard/staff.html',context)

@login_required 
def staff_view(request,pk):
    worker = User.objects.get(id=pk)
    context ={
        'worker':worker,
    }
    return render(request,'dashboard/staff_view.html',context)

@login_required  
def products(request):
    
    items = Product.objects.all()
    products_count = items.count()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid(): 
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.warning(request,f'{product_name} has been added ')
            return redirect('dashboard-products')
        
    else: 
        form =ProductForm() 
    context = {
        'items':items,
        'form':form,
        'products_count':products_count,
    } 
    return render(request,'dashboard/products.html',context)
@login_required  
def orders(request):
    
    myOrder = Order.objects.all()
    order_count = myOrder.count()
    
    context = {
        'myOrder':myOrder,
        'orders_count':order_count,
    }
        
    return render(request,'dashboard/orders.html',context)
@login_required 
def product_delete(request,pk):
    item=Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    return render(request,'dashboard/product_delete.html')
@login_required 
def product_update(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else :
        form = ProductForm(instance=item)
    
    context={
        'form':form,
        
    }
    
    return render(request,'dashboard/product_update.html',context)

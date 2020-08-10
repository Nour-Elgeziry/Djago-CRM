# classes that url go to to trigger and render templates
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    #total orders
    total_orders = orders.count()
    #total delivered orders
    delivered = orders.filter(status='Delivered').count()
     #total pending orders
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers':customers, 
    'total_orders':total_orders, 
    'delivered':delivered,
    'pending':pending}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    
    return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk):
    #get customer with specific id
    customer = Customer.objects.get(id=pk)
    #get order for specific customer
    orders = customer.order_set.all()
    #get customer total orders
    total_order = orders.count()
    context = {'customer':customer, 'orders':orders, 'total_order':total_order }
    return render(request, 'accounts/customer.html', context)
    
def createOrder(request):
    form = OrderForm()
    #check for POST requests
    if request.method == 'POST':
        #store information in form
        form = OrderForm(request.POST)
        #check if the form is valid
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
    
    
def updateOrder(request, pk):
    #get order id from dahsboard template(html file)
    order = Order.objects.get(id = pk)
    #use the instance of the order to prefill form info
    form = OrderForm(instance=order)   
    #save the updated form
    #check for POST requests
    if request.method == 'POST':
        #store information in form
        form = OrderForm(request.POST,instance=order)
        #check if the form is valid
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request,pk):
    order = Order.objects.get(id = pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    
    context = {'order':order}
    return render(request,  'accounts/delete_order.html', context )
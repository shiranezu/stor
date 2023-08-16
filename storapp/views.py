from django.shortcuts import render, redirect
from .models import Customer, Order
from .forms import AddNewItem,  AddNewCustomer, Login
from django.contrib.auth import authenticate, login

def display_customers(request):
    customers = Customer.objects.all()
    return render(request, "customer.html", {"customers": customers})

def display_orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})

def add_new_customer(request):
    form = AddNewCustomer()
    if request.method == "POST":
        form = AddNewCustomer(request.POST)
        # print(request.POST['first_name'])
        # print(request.POST['last_name'])
        # print(request.POST['email'])
        if form.is_valid():
            result = form.save()
            result.save()
            return redirect('/orders/')
    return render(request, "forms.html", {"forms": form})

def add_new_item(request):
    form = AddNewItem()
    if request.method == 'POST':
        form = AddNewItem(request.POST)

        if form.is_valid():
            result = form.save()
            result.save()
            return redirect('storapp:customers')
    return render(request, "item.html", {"forms": form})

def login_form(request):
    form = Login()
    if request.method == 'POST':
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user  = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect('storapp:customers')
            else:
                    return render(request, 'login.html', {'form':form, 'messages':'login failed'})
    return render(request, 'login.html', {'form':form, 'messages': 'login successful'})
        
            

            


# Create your views here.

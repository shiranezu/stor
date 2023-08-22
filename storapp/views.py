from django.shortcuts import render, redirect
from .models import Customer, Order
from .forms import AddNewItem,  AddNewCustomer, Login, Item
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# @login_required(login_url = '/login/')
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
                # print("hello")
                login(request, user)
                return redirect('/orders/')
            else:
                    return render(request, 'login.html', {'form':form, 'messages':'login failed'})
    return render(request, 'login.html', {'form':form, 'messages': 'login successful'})
        
# def logout(request):
#     logout(request)
#     return redirect('/login/')
            

def get_specific_item(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'pk.html', {'item':item})



# Create your views here.

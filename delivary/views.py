from django.http import HttpResponse # type: ignore
from django.shortcuts import redirect, render # type: ignore


from django.conf import settings # type: ignore
import razorpay # type: ignore


from .forms import MenuForm, ResForm

from .models import Cart, Customer, Menu, Restaurants
from django.contrib import messages # type: ignore

# Create your views here.

def index(request):
    return render(request,'delivary/index.html')

def sign_in(request):
    return render(request,'delivary/sign_in.html')

def sign_up(request):
    return render(request,'delivary/sign_up.html')

def handle_signin(request):
    li = Restaurants.objects.all()
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        try:
            cus = Customer.objects.get(username=username, password=password)
            if username == 'admin':
                return render(request,'delivary/success.html')
            else:
                return render(request, 'delivary/cusdisplay_res.html',{'username':username,'li':li})
        except:
            return render(request, 'delivary/failed.html')

    
    
def handle_signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        try:
            cus=Customer.Objects.get(username=username, password=password)
        except:
            cus=Customer(username=username,password=password,email=email,mobile=mobile,address=address)
            cus.save()
        # data={
        #     'username':username,
        #     'password':password,
        #     'email':email,
        #     'mobile':mobile,
        #     'address':address,
        # }
        return render(request,'delivary/sign_in.html')
    else:
        return HttpResponse('Invalid response')
    

def add_res(request):
    form=ResForm(request.POST or None)
    if form.is_valid():
        res_name=request.POST.get('res_name')
        try:
            res=Restaurants.objects.get(res_name=res_name)
        except:
            form.save()
            return redirect('delivary:display_res')
    return render(request,'delivary/add_res.html',{'form':form})

def display_res(request):
    li = Restaurants.objects.all()
    return render(request,'delivary/display_res.html',{'li':li})



def view_menu(request, id):
    res=Restaurants.objects.get(pk=id)
    menu = Menu.objects.filter(res=res)
    return render(request,'delivary/view_menu.html',{'res':res,'menu':menu})


def add_menu(request, id):
    form = MenuForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('delivary:view_menu', id)
    return render(request,'delivary/menu_form.html',{'form':form})



def delete_menu(request,id):
    item=Menu.objects.get(pk=id)
    res_id = item.res.id
    item.delete()
    return redirect('delivary:view_menu',res_id)


def cusdisplay_res(request,username):
    customer = Customer.objects.get(username=username)
    li = Restaurants.objects.all()
    return render(request,'delivary/cusdisplay_res.html',{'li':li, 'username':username})


def cusmenu(request, id,username):
    res = Restaurants.objects.get(pk=id)
    menu=Menu.objects.filter(res=res)   
    return render(request, 'delivary/cusmenu.html',{'res':res, 'menu':menu, 'username':username})


def show_cart(request, username):
    customer = Customer.objects.get(username=username)
    cart = Cart.objects.filter(customer = customer).first()
    items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0
    return render(request, 'delivary/show_cart.html',{'items':items, 'total_price':total_price,'username':username})

def delete_res(request,id):
    res=Restaurants.objects.get(pk=id)
    res.delete()
    return redirect('delivary:display_res')


def update_res(request, id):
    res=Restaurants.objects.get(pk=id)
    form = ResForm(request.POST or None, instance=res)  

    if request.method == 'POST':
        if form.is_valid():
            form.save()  
            return redirect('delivary:display_res')  

    return render(request, 'delivary/add_res.html', {'form': form, 'restaurant': res})

def add_to_cart(request,username, menuid):
    customer = Customer.objects.get(username=username)
    item = Menu.objects.get(pk=menuid)
    cart, created = Cart.objects.get_or_create(customer=customer)
    cart.items.add(item)
    messages.success(request, f"{item.item_name} added") 
    return redirect('delivary:cusmenu', id=item.res.id, username=username)

def checkout(request, username):
    customer = Customer.objects.get(username = username)
    cart = Cart.objects.filter(customer = customer).first()
    cart_items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0

    if total_price == 0:
        return render(request, 'delivary/checkout.html',{'error':'Your cart is Empty'})

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    order_data = {
        'amount':int(total_price * 100),
        'currency':'INR',
        'payment_capture':'1',
    }
    order = client.order.create(data = order_data)
    return render(
        request, 'delivary/checkout.html',
        {'username':username,
        'cart_items':cart_items,
        'total_price':total_price,
        'razorpay_key_id':settings.RAZORPAY_KEY_ID,
        'order_id':order['id'],
        'amount':total_price,
        }
    )

def orders(request, username):
        customer = Customer.objects.get(username = username)
        cart = Cart.objects.filter(customer=customer).first()
        cart_items = cart.items.all() if cart else []
        total_price = cart.total_price() if cart else 0

        if cart:
            cart.items.clear()

        return render(request, 'delivary/orders.html',{
        'username':username,
        'cart_items':cart_items,
        'total_price':total_price,
        'customer':customer
        })
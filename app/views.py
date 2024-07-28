from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from . models import Cart, Customer, Product
from django.db.models import Count
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required #chat





# Create your views here.
def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")


class CategoryView(View): #if you are using the class so you are pass the parameter as a viewe
      def get(self,request,val):           
           product = Product.objects.filter(category=val)
           title=Product.objects.filter(category=val).values('title')
           return render(request,"app/category.html",locals())
      
class CategoryTitle(View) :
    def get(self, request, val):
        product =Product.objects.filter(title=val)
        title= Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html" , locals())      
      
class ProductDetail(View): #check here for any error 1:53:49
    def  get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())  

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form. save()
            messages.success(request, "Congratulations! User Register Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/customerregistration.html',locals())
    
class ProfileView(View) :
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html',locals())  
      
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']  # Assuming you have a Customer model defined
   
            reg = Customer(user=user,name=name,locality=locality,city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulation Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/profile.html',locals())
    
def address(request):
    add = Customer.objects.filter(user=request.user) #only login user can see the data like thr root user
    return render(request,'app/address.html',locals())

# @login_required #chat
# def address(request):
#     if request.method == "POST":
#         form = AddressForm(request.POST)
#         if form.is_valid():
#             address = form.save(commit=False)
#             address.user = request.user
#             address.save()
#             return redirect('profile')
#     else:
#         form = AddressForm()

#     return render(request, 'app/address.html', {'form': form})


class updateAddress(View):
    def get(self,request,pk):#here hte pk is indicate the primary key
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,'app/updateAddress.html',locals())
    
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.mobile=form.cleaned_data['mobile']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulations Profile Update Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect("address")
    
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity * p.product.discounted_price
        amount=amount + value
    totalamount= amount + 40
    return render(request, 'app/addtocart.html',locals())

class checkout(View):
    def get(self,request):
        return render(request,'app/checkout.html',locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        
        # Update the quantity of the product in the cart
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()

        # Calculate the total amount and total amount including shipping
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value        
        totalamount = amount + 40  # Assuming 40 is the fixed shipping cost

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }

        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        
        # Update the quantity of the product in the cart
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()

        # Calculate the total amount and total amount including shipping
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value        
        totalamount = amount + 40  # Assuming 40 is the fixed shipping cost

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        
        return JsonResponse(data)
    

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        
        # Update the quantity of the product in the cart
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value        
        totalamount = amount + 40  # Assuming 40 is the fixed shipping cost

        data = {
            'amount': amount,
            'totalamount': totalamount
        }
        
        return JsonResponse(data)
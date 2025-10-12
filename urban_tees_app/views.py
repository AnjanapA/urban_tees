from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from .models import Product,User
import os
from .forms import LoginForm,RegisterForm,UserInfoForm
from django.contrib import messages

# Create your views here.
# def login(request):
#     return render(request,'login.html')

def main(request):
    return render(request,'main.html')

def user_layout(request):
    return render(request,'user_layout.html')

def admin_view_product(request):
    return render(request,'admin_view_product.html')

def admin_operations(request):
    return render(request,'admin_operations.html')

def image_preview(request):
    if request.method == 'POST':
        n=""
        f=request.FILES['file_name']
        if f:
            n=os.path.join('static/images/',f.name)
        else:
            n=""
        return render(request,'admin_add_product.html',{'item':n})
    return render(request,'admin_add_product.html',{'item':''})

def admin_layout(request):
    return render(request,'admin_layout.html')

def admin_add_product(request):
    n=""
    upload=""
    context={}
    if request.method == 'POST':
        product_title=request.POST.get('product_title')
        product_description=request.POST.get('product_description')
        old_price=int(request.POST.get('old_price'))
        category=request.POST.get('category')
        offer=int(request.POST.get('offer'))

# product_size
        small_size=request.POST.get('small_size')
        medium_size=request.POST.get('medium_size')
        large_size=request.POST.get('large_size')
        extralarge_size=request.POST.get('extralarge_size')

        # product_size=request.POST.get('product_size')
        # product_quantity=int(request.POST.get('product_quantity'))
        # new_price=int(request.POST.get('new_price'))


        new_price=old_price*(offer/100)
        file1=request.FILES['file_name_1']
        file2=request.FILES['file_name_2']
        file3=request.FILES['file_name_3']
        file4=request.FILES['file_name_4']
        upload_path_1=os.path.join(settings.MEDIA_IMG,file1.name)
        upload_path_2=os.path.join(settings.MEDIA_IMG,file2.name)
        upload_path_3=os.path.join(settings.MEDIA_IMG,file3.name)
        upload_path_4=os.path.join(settings.MEDIA_IMG,file4.name)

        with open(upload_path_1,'wb+') as destination:
            for chunk in file1.chunks():
                destination.write(chunk)
        with open(upload_path_2,'wb+') as destination:
            for chunk in file2.chunks():
                destination.write(chunk)
        with open(upload_path_3,'wb+') as destination:
            for chunk in file3.chunks():
                destination.write(chunk)
        with open(upload_path_4,'wb+') as destination:
            for chunk in file4.chunks():
                destination.write(chunk)

        if file1:
            n1=os.path.join('/images/',file1.name)
        if file2:
            n2=os.path.join('/images/',file2.name)
        if file3:
            n3=os.path.join('/images/',file3.name)
        if file4:
            n4=os.path.join('/images/',file4.name)
                
            context=Product(
            item_image1=n1,
            item_image2=n2,
            item_image3=n3,
            item_image4=n4,
            item_name=product_title,
            item_description=product_description,
            old_price=old_price,
            new_price=new_price,
            offer=offer,
            category=category,
            small_size=small_size,
            medium_size=medium_size,
            large_size=large_size,
            extralarge_size=extralarge_size

            )

        context.save()

        upload='file uploaded successfully'
    else:
        upload = "No file uploaded."

    return render(request,'admin_add_product.html',{'upload':upload})

def admin_view_product(request):
    item_details=Product.objects.all()
    return render(request,'admin_view_product.html',{'item':item_details})

def category_product(request, category=None):
    categories = ['mens', 'womens', 'girls', 'boys']
    if category in categories:
        item_details = Product.objects.filter(category=category)
    else:
        item_details = Product.objects.all()
    
    return render(request, 'admin_view_product.html', {
        'item':item_details,
        'category': category,
    })


def admin_edit(request,id):
    item_details=Product.objects.get(id=id)
    return render(request,'admin_edit_product.html',{'context':item_details,'id':id})


def admin_edit_product(request,id):
    if request.method == 'POST':
        product_title=request.POST.get('product_title')
        product_description=request.POST.get('product_description')
        old_price=int(request.POST.get('old_price'))
        category=request.POST.get('category')
        offer=int(request.POST.get('offer'))

# product_size
        small_size=request.POST.get('small_size')
        medium_size=request.POST.get('medium_size')
        large_size=request.POST.get('large_size')
        extralarge_size=request.POST.get('extralarge_size')

        new_price=old_price*(offer/100)

        context=Product.objects.filter(id=id).update(
            item_name=product_title,
            item_description=product_description,
            old_price=old_price,
            new_price=new_price,
            offer=offer,
            category=category,
            small_size=small_size,
            medium_size=medium_size,
            large_size=large_size,
            extralarge_size=extralarge_size

            )

        upload='changes updated successfully'
    else:
        upload = "No changes."


    return redirect('admin_view_product')



def admin_delete_product(request, id):
    if request.method == 'POST':
        id=int(request.POST.get('id'))
    context=Product.objects.filter(id=id).delete()
    return redirect('admin_view_product')

# user
def web_home(request):
    item_details = Product.objects.all()

    return render(request, 'web_home.html',{'item':item_details})

def home(request):
    item_details = Product.objects.all()

    return render(request, 'home.html',{'item':item_details})

def account(request):
    return render(request, 'account.html')

def logout(request):
    return redirect('web_home')

def register(request):
    if request.method == 'POST':
            reg_form=RegisterForm(request.POST)
            print("register")

            if reg_form.is_valid():
                password =reg_form.cleaned_data['password']
                confirm =reg_form.cleaned_data['confirm_password']
                if password == confirm:
                    myuser = User.objects.create(
                        phone=reg_form.cleaned_data['phone'],
                        username=reg_form.cleaned_data['username'],
                        email=reg_form.cleaned_data['email'],
                        password=password
                    )
                    messages.success(request, "Account created successfully!")
                    return redirect('login')
                
                else:
                    messages.error(request, "Passwords do not match")
                    return render(request,'account.html',{'form':reg_form,'value':'register'})
            return render(request,'account.html',{'form':reg_form,'value':'register'})
    else:
        
        reg_form1=RegisterForm()
        return render(request,'account.html',{'form1':reg_form1,'value':'register'})


def login(request):
    if request.method == 'POST':
        if request.POST.get('loginvalid')=="login":
            return redirect('home')
        else:
                
            form=LoginForm(request.POST)

            if form.is_valid():
                email = form.cleaned_data['email']
                try:
                    myuser=User.objects.get(email=email)
                    password = form.cleaned_data['password']
                    if myuser.password==password:
                        request.session['user_id']=myuser.id
                        return redirect('home')
                    else:
                        messages.error(request,'Invalid username or password.')
                except User.DoesNotExist:
                    messages.error(request,'user not exist.')
        return render(request,'account.html',{'form':form,'value':'login'})
    else:
        form=LoginForm()
        return render(request,'account.html',{'form':form,'value':'login'})


def userinfo(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            return render(request, 'home.html', {'data': cleaned_data})
    else:
        form = UserInfoForm()

    return render(request, 'userinfo.html', {'form': form})


def user_products(request, category=None):
    categories = ['mens', 'womens', 'girls', 'boys']
    if category in categories:
        item_details = Product.objects.filter(category=category)
    else:
        item_details = Product.objects.all()
    
    return render(request, 'user_products.html', {
        'item':item_details,
        'category': category,
    })
def user_single_product(request, id):
    item_details=Product.objects.get(id=id)
    return render(request, 'user_single_product.html', {'item':item_details})


def user_order_review(request, id):
    item_details=Product.objects.get(id=id)
    return render(request, 'user_order_review.html', {'item':item_details})

def user_payment(request, id):
    item_details=Product.objects.get(id=id)
    return render(request, 'user_payment.html', {'item':item_details})

def myorder_page(request):
    return render(request, 'myorder_page.html')

def cart_slide(request,id):
    item_details=Product.objects.get(id=id)
    return render(request, 'home.html', {'item':item_details})


def wishlist_page(request):
    
    return render(request, 'wish_list.html')


def cart_page(request):
    return render(request, 'cart_page.html')



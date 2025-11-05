from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.conf import settings
from .models import Product,User,Order,Wishlist,Cart
import os
from .forms import LoginForm,RegisterForm,UserInfoForm,SendOTPForm,VerifyOTPForm,EmailForm,PasswordForm
from django.contrib import messages
from django.core.mail import send_mail
import random
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf.urls import handler404
from django.contrib.auth import authenticate, login, logout
from datetime import time
from django.urls import reverse
from django.contrib.auth import get_user_model
# from django.contrib.sites.models import Site

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

handler404 = 'urban_tees.urls.custom_404_view'

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

#@login_required(login_url='/login/')

def admin_view_product(request):
    # item_details=Product.objects.all()
    # return render(request,'admin_view_product.html',{'item':item_details})
    # , category=None
    # categories = ['mens', 'womens', 'girls', 'boys']
    # if category in categories:
    #     item_details = Product.objects.filter(category=category)
    # else:
    item_details = Product.objects.all()

    paginator = Paginator(item_details,4) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_view_product.html', {'item':item_details,'page_obj': page_obj})
    # return render(request, 'user_products.html', {
    #     'item':item_details,
    #     'category': category,
    # })

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

# here

def new_password(request):
   

    verify_form=EmailForm()
    return render(request,'new_password.html',{'form':verify_form})

def send_email(request):
    if request.method=='POST':
        email=request.POST.get('email')
        otp=random.randint(100000,999999)
        print(otp)
        request.session['otp'] = otp
        request.session['email'] = email
        send_mail(
            subject='OTP Code for email verification ',
            message=f'Your OTP is: {otp}',
            from_email='urbantees2k25@gmail.com',
            recipient_list=[email],
        )
    verify_form=EmailForm()
    return render(request,'new_password.html',{'form':verify_form})

def verify_emailotp(request):
    if request.method == 'POST':
        # emailotp_form=EmailForm(request.POST)
        entered_otp =request.POST.get('otp')
        session_otp = str(request.session.get('otp'))
        if entered_otp == session_otp:
            messages.success(request,'Email varified successfully.')
            
        else:
            messages.error(request,'Could not verify email')

        verifyotp_form=PasswordForm()
        return render(request, 'new_password.html',{'form':verifyotp_form})

def password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        re_password = request.POST.get('re_password')

        if new_password == re_password:
            email = request.session.get('email')
            print(email)

            try:
                myuser = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
                return redirect('forgot_password')

            myuser.set_password(new_password)
            myuser.save()

            messages.success(request, 'Password has been changed successfully.')
            return redirect('login_acc')
        else:
            messages.error(request, 'Passwords do not match.')

    forgot_form = PasswordForm()
    return render(request, 'new_password.html', {'form': forgot_form})

def send_otp(request,email,username):
    otp=random.randint(100000,999999)
    print(otp)
    request.session['otp'] = otp
    request.session['username'] = username
    request.session['email'] = email

    send_mail(
        subject='OTP Code',
        message=f'Your OTP is: {otp}',
        from_email='urbantees2k25@gmail.com',
        recipient_list=[email],
    )


                
def register(request):
    if request.method == 'POST':
        reg_form=SendOTPForm(request.POST)
        print(reg_form)
        if reg_form.is_valid():
            username=reg_form.cleaned_data['user_name']
            email=reg_form.cleaned_data['email']
            send_otp(request,email,username)
            print(send_otp)
            return redirect('verify_otp')
        else:
            return render(request,'account.html',{'form':reg_form,'value':'register'})
            
    else:
        reg_form1=SendOTPForm()
        return render(request,'account.html',{'form1':reg_form1,'value':'register'})

def resend(request):
    otp=random.randint(100000,999999)
    print(otp)
    request.session['otp'] = otp
    email=request.session.get('email')
    username=request.session.get('username')
    request.session['email'] = email
    send_mail(
        subject='OTP Code',
        message=f'Your OTP is: {otp}',
        from_email='urbantees2k25@gmail.com',
        recipient_list=[email],
    )

    otp_form=VerifyOTPForm()
    return render(request,'verify_otp.html',{'form':otp_form,'value':'verify'})

def verify_otp(request):
    if request.method == 'POST':
        otp_form=VerifyOTPForm(request.POST)
        if request.POST.get('verify_otp')=="verify":
            if otp_form.is_valid():
                entered_otp = otp_form.cleaned_data['otp']
                session_otp = str(request.session.get('otp'))
                if entered_otp == session_otp:
                    messages.success(request,'Email varified successfully.')
                    return redirect('final_register')
                # return render(request,'verify_otp.html',{'form':otp_form,'value':'verify'})
        else:
            messages.error(request,'Could not verify email')

            return render(request,'verify_otp.html',{'form':otp_form,'value':'verify'})
    else:
        
        otp_form=VerifyOTPForm()
        return render(request,'verify_otp.html',{'form':otp_form,'value':'verify'})
    


def final_register(request):
    if request.method == 'POST':
        final_form=RegisterForm(request.POST)


        if final_form.is_valid():
            username=request.session.get('username')
            email=request.session.get('email')
            phone =final_form.cleaned_data['phone']
            # address =final_form.cleaned_data['address']
            # place =final_form.cleaned_data['place']
            # city =final_form.cleaned_data['city']
            # pincode =final_form.cleaned_data['pincode']
            role =final_form.cleaned_data['role']
            # activity =final_form.cleaned_data['activity']
            password =final_form.cleaned_data['password']
            confirm =request.POST.get('confirm_password')
            # print(password)
            # print(confirm)
            if password == confirm:
                myuser = User.objects.create_user(
                    username=email,
                    email=email,
                    phone=final_form.cleaned_data['phone'],
                    address='',
                    place='',
                    city='',
                    pincode='',
                    role="user",
                    activity='',
                    password=password,
                    user_name=username
                )
                print(myuser)
                messages.success(request, "Account created successfully!")
                return redirect('login_acc')
            messages.error(request, "Passwords do not match!")
        else:
            messages.error(request,'There is an error creating account')

            return render(request,'final_register.html',{'form':final_form,'value':'register'})
    else:
        
        # final_form=RegisterForm()
        username=request.session.get('username')
        email=request.session.get('email')
        final_form = RegisterForm(initial={
            'username': username, 
            'email': email,
            })
        
        return render(request,'final_register.html',{'form':final_form,'value':'register'})
    
def is_user(request):
    if request.user.role=="user":
        return True
    return False

def is_admin(request):
    if request.user.role=="admin":
        return True
    return False



def login_acc(request):
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        # if form1.is_valid():
        email = request.POST.get('email')
        password = request.POST.get('password')
        # email = form1.cleaned_data['email']
        # password = form1.cleaned_data['password']
        # print(email,password)
        # user=User.objects.get(email=email)
        myuser = authenticate(username=email,password=password)  
        if myuser:
            login(request,myuser)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')

        return render(request, 'account.html', {'form': form1, 'value': 'login'})
    
    else:
        form1 = LoginForm()
    return render(request, 'account.html', {'form': form1, 'value': 'login'})


def logout_acc(request):
    logout(request)
    return redirect('login')


def userinfo(request):
    if request.method == 'POST':
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        city=request.POST.get('city')
        place=request.POST.get('place')
        pincode=request.POST.get('pincode')

        id=request.user.id

        u_info=User.objects.filter(id=id).update(
            gender=gender,
            address=address,
            city=city,
            place=place,
            pincode=pincode

        )

    return render(request, 'userinfo.html')


#@login_required

def user_products(request, category=None):
    categories = ['mens', 'womens', 'girls', 'boys']
    if category in categories:
        item_details = Product.objects.filter(category=category)
    else:
        item_details = Product.objects.all()
        print(item_details)
    print(item_details)
    return render(request, 'user_products.html', {'item': item_details})

# def user_products(request, category=None):
#     categories = ['mens', 'womens', 'girls', 'boys']
#     if category in categories:
#         item_details = Product.objects.filter(category=category)
#     else:
#         item_details = Product.objects.all()
#         return render(request, 'user_products.html', {'item':item_details})
#     return render(request, 'user_products.html', {
#         'item':item_details,
#         'category': category,
#     })

#@login_required(login_url='/login/')
def user_single_product(request, id):
    if is_user(request)==True:

        item_details=Product.objects.get(id=id)
        return render(request, 'user_single_product.html', {'item':item_details})

#@login_required(login_url='/login/')
def user_order_review(request, id):
    item_details=Product.objects.get(id=id)
    return render(request, 'user_order_review.html', {'item':item_details})

def user_payment(request, id):
    item_details=Product.objects.get(id=id)
    return render(request, 'user_payment.html', {'item':item_details})

def cart_payment(request, product_id):
    item_details=Cart.objects.get(product_id=product_id)
    return render(request, 'user_payment.html', {'item':item_details})

def myorder_page(request):
    return render(request, 'user_myorder_page.html')

def cart_slide(request,id):
    item_details=Product.objects.get(id=id)
    return render(request, 'cart_slide.html', {'item':item_details})


# def wishlist_page(request):
#     wishlist_items = Wishlist.objects.all
#     return render(request, 'wish_list.html', {'wishlist_items': wishlist_items})
#@login_required
def wishlist_page(request):
    if request.method == "POST":
        product_id = request.POST.get('id')
        action = request.POST.get('action', 'add')

        if product_id:
            wishlist = request.session.get('wishlist', [])

            if action == 'add':
                if product_id not in wishlist:
                    wishlist.append(product_id)
            elif action == 'remove':
                if product_id in wishlist:
                    wishlist.remove(product_id)
                    messages.success(request, "Product removed from your wishlist")
            request.session['wishlist'] = wishlist

            return JsonResponse({'status': 'success', 'wishlist_count': len(wishlist)})
        
        return JsonResponse({'status': 'error', 'message': 'No product ID'})

    wishlist_ids = request.session.get('wishlist', [])
    wishlist_items = Product.objects.filter(id__in=wishlist_ids)
    return render(request, 'wish_list.html', {'wishlist_items': wishlist_items})



#@login_required
def cart_page(request):
    user = request.user

    if request.method == "POST":
        product_id = request.POST.get('id')
        action = request.POST.get('action')
        size = request.POST.get('size')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        # total_price=price*quantity

        if not product_id:
            messages.success(request, "no matched items!")

        if action == 'add':
            existing = Cart.objects.filter(user_id=user.id, product_id=product_id, size=size).first()
            if existing:
                existing.quantity += int(quantity)
                existing.save()
            else:
                product = Product.objects.get(id=product_id)
                Cart.objects.create(
                    user_id=user.id,
                    product_id=product_id,
                    product_name=product.item_name,
                    product_price=price,
                    quantity=quantity,
                    size=size
                )
            return JsonResponse({'status': 'success'})

        elif action == 'remove':
            Cart.objects.filter(user_id=user.id, product_id=product_id).delete()
            # messages.success(request, "Product removed from your cart!")
            return JsonResponse({'status': 'success'})
            # return render(request,'cart_page.html')

        return JsonResponse({'status': 'error', 'message': 'Invalid action'})
    cart_items = Cart.objects.filter(user_id=user.id)
    return render(request, 'cart_page.html', {'cart_items': cart_items})

#@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user_myorder_page.html', {'orders': orders})

def popup(request):
    return render(request, 'popup.html')    


def otp_time():
    now=time.now()
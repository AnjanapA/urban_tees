from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from .models import Product
import os
import json


# Create your views here.
def login(request):
    return render(request,'login.html')

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
            n2=os.path.join('static/images/',file2.name)
        if file3:
            n3=os.path.join('static/images/',file3.name)
        if file4:
            n4=os.path.join('static/images/',file4.name)
                
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
        product_size=request.POST.get('product_size')
        product_quantity=int(request.POST.get('product_quantity'))
        old_price=int(request.POST.get('old_price'))
        offer=int(request.POST.get('offer'))
        category=request.POST.get('category')

        new_price=old_price*(offer/100)

        f=request.FILES['file_name']
        n=os.path.join('static/images/',f.name)

        context=Product.objects.filter(id=id).update(
        item_image=n,
        item_name=product_title,
        item_description=product_description,
        item_size=product_size,
        item_quantity=product_quantity,
        new_price=new_price,
        old_price=old_price,
        offer=offer,
        category=category
        )

        upload='changes updated successfully'
    else:
        upload = "No changes."


    return render(request,'admin_edit_product.html',{'context':context,'upload':upload})

def admin_delete_layout(request,id):
  
  if request.method=='POST':

    id=int(request.POST.get('id'))

    context=Product.objects.filter(id=id).delete()
    return render(redirect,'/admin_view_product.html/')



# user
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

def wishlist_page(request):
    return render(request, 'wish_list.html')


def cart_page(request):
    return render(request, 'add_to_cart.html')

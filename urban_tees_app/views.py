from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from .models import Product
import os


# Create your views here.
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
        return render(request,'admin_add_layout.html',{'item':n})
    return render(request,'admin_add_layout.html',{'item':''})

def admin_layout(request):
    return render(request,'admin_layout.html')

def admin_add_layout(request):
    n=""
    upload=""
    context={}
    if request.method == 'POST':
        product_title=request.POST.get('product_title')
        product_description=request.POST.get('product_description')
        product_size=request.POST.get('product_size')
        product_quantity=int(request.POST.get('product_quantity'))
        old_price=int(request.POST.get('old_price'))
        category=request.POST.get('category')
        offer=int(request.POST.get('offer'))
        # new_price=int(request.POST.get('new_price'))
        new_price=old_price*(offer/100)
        f=request.FILES['file_name']
        upload_path=os.path.join(settings.MEDIA_IMG,f.name)
        with open(upload_path,'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        
        if f:
            n=os.path.join('static/images/',f.name)
                
            context=Product(
            item_image=n,
            item_name=product_title,
            item_description=product_description,
            item_size=product_size,
            item_quantity=product_quantity,
            old_price=old_price,
            new_price=new_price,
            offer=offer,
            category=category

            )

        context.save()

        upload='file uploaded successfully'
    else:
        upload = "No file uploaded."

    return render(request,'admin_add_layout.html',{'upload':upload})

def admin_view_layout(request):
    item_details=Product.objects.all()
    return render(request,'admin_view_layout.html',{'item':item_details})

def category_product(request,category):
    # item_details=Product.objects.all()
    item=Product(
        id='id',  
        item_image='n',
        item_name='product_title',
        item_description='product_description',
        item_size='product_size',
        item_quantity='product_quantity',
        new_price='new_price',
        old_price='old_price',
        offer='offer',
        category='category'
        )
    if request.method=='POST':
        category=request.POST.get('select_category')
        item=Product.objects.get(category=category)
    return render(request,'admin_view_layout.html',{'item':item,'category':category})

def admin_edit(request,id):
    item_details=Product.objects.get(id=id)
    return render(request,'admin_edit_layout.html',{'context':item_details,'id':id})


def admin_edit_layout(request,id):
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


    return render(request,'admin_edit_layout.html',{'context':context,'upload':upload})

def admin_delete_layout(request,id):
  
  if request.method=='POST':

    id=int(request.POST.get('id'))

    context=Product.objects.filter(id=id).delete()
    return render(redirect,'/admin_view_layout.html/')

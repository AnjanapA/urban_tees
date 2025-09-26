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

def admin_add_layout(request):
    n=""
    upload=''
    context={}
    if request.method == 'POST':
        product_title=request.POST.get('product_title')
        product_description=request.POST.get('product_description')
        old_price=int(request.POST.get('old_price'))
        category=request.POST.get('category')
        offer=int(request.POST.get('offer'))
        new_price=int(request.POST.get('new_price'))

        f=request.FILES['file_name']
        upload_path=os.path.join(settings.MEDIA_IMG,f.name)
        with open(upload_path,'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        
        if f:
            n=os.path.join('images/',f.name)
            upload='file uploaded successfully'

            
            
        context=Product(
        item_image=n,
        item_name=product_title,
        item_description=product_description,
        old_price=old_price,
        new_price=new_price,
        offer=offer,
        category=category

        )

        context.save()

    return render(request,'admin_add_layout.html',{'item':n})



def admin_edit(request):
  
  item_details=Product.objects.all()
  item=Product(
    id=0,  
    item_image='',
    item_name='',
    item_description='',
    new_price='',
    old_price='',
    offer='',
    category=''
    )
  return render(request,'admin_edit_layout.html',{'context':item_details,'item':item})


def admin_edit_layout(request):
  
  item_details=Product.objects.all()
  item=Product(
    id=0 , 
    item_image='',
    item_name='',
    item_description='',
    new_price='',
    old_price='',
    offer='',
    category=''
    )
  if request.method=='POST':
      id=request.POST.get('select_id')
      item=Product.objects.get(id=id)
  return render(request,'admin_edit_layout.html',{'context':item_details,'item':item})

def admin_update_layout(request,id):
    if request.method == 'POST':
        product_title=request.POST.get('product_title')
        product_description=request.POST.get('product_description')
        old_price=int(request.POST.get('old_price'))
        offer=int(request.POST.get('offer'))
        category=request.POST.get('category')

        new_price=old_price*(offer/100)

        f=request.FILES['file_name']
        upload_path=os.path.join(settings.MEDIA_IMG,f.name)
        with open(upload_path,'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        
        if f:
            n=os.path.join('static/images/',f.name)
            upload='file uploaded successfully'


        context=Product.objects.filter(id=id).update(
        item_image=n,
        item_name=product_title,
        item_description=product_description,
        new_price=new_price,
        old_price=old_price,
        offer=offer,
        category=category
        )

    return render(request,'admin_edit_layout.html')

def admin_delete_layout(request,id):
  
  if request.method=='POST':

    id=int(request.POST.get('id'))

    context=Product.objects.filter(id=id).delete()
  return redirect('/admin_edit_layout/')

from django.urls import path
from . import views

urlpatterns = [

path('main',views.main,name='main'),

path('admin_operations',views.admin_operations,name='admin_operations'),

path('image_preview',views.image_preview,name='image_preview'),

path('admin_layout',views.admin_layout,name='admin_layout'),
path('admin_add_product',views.admin_add_product,name='admin_add_product'),
path('admin_view_product',views.admin_view_product,name='admin_view_product'),

path('admin_edit/<int:id>',views.admin_edit,name='admin_edit'),
path('admin_edit_product/<int:id>',views.admin_edit_product,name='admin_edit_product'),
path('admin_delete_product/<int:id>',views.admin_delete_product,name='admin_delete_product'),


# user

path('',views.web_home,name='web_home'),
path('custom_404_view',views.custom_404_view,name='custom_404_view'),
path('web_home',views.web_home,name='web_home'),
path('account',views.account,name='account'),
path('home',views.home,name='home'),

path('new_password',views.new_password,name='new_password'),
# path('verify_email',views.verify_email,name='verify_email'),
path('password',views.password,name='password'),
path('verify_email',views.verify_emailotp,name='verify_emailotp'),
path('send-email',views.send_email,name='send_email'),

path('logout',views.logout,name='logout'),
path('userinfo',views.userinfo,name='userinfo'),
path('login',views.login_acc,name='login_acc'),
path('register',views.register,name='register'),
path('send_otp/<str:email>/', views.send_otp, name='send_otp'),
path('verify_otp', views.verify_otp, name='verify_otp'),
path('final_register', views.final_register, name='final_register'),
path('resend', views.resend, name='resend'),

path('cart_slide/<int:id>/',views.cart_slide,name='cart_slide'),
path('logout',views.logout_acc,name='logout'),
path('user_orders', views.user_orders, name='user_orders'),

path('user_layout',views.user_layout,name='user_layout'),
path('user_products', views.user_products, name='user_products'),
path('user_products/<str:category>/', views.user_products, name='user_category_products'),
path('user_single_product/<int:id>/', views.user_single_product, name='user_single_product'),
path('wishlist_page/', views.wishlist_page, name='wishlist_page'),
path('cart_page', views.cart_page, name='cart_page'),
path('user_order_review/<int:id>/', views.user_order_review, name='user_order_review'),

path('cart_payment/<str:product_id>/', views.cart_payment, name='cart_payment'),

path('user_payment/<int:id>/', views.user_payment, name='user_payment'),
path('myorder_page', views.myorder_page, name='myorder_page'),

path('popup', views.popup, name='popup'),

]


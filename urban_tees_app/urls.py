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
path('web_home',views.web_home,name='web_home'),
path('account',views.account,name='account'),
path('login',views.login,name='login'),
path('register',views.register,name='register'),
path('home',views.home,name='home'),
path('logout',views.logout,name='logout'),
path('userinfo',views.userinfo,name='userinfo'),



path('user_layout',views.user_layout,name='user_layout'),
path('user_products', views.user_products, name='user_products'),
path('user_products/<str:category>/', views.user_products, name='user_category_products'),
path('user_single_product/<int:id>/', views.user_single_product, name='user_single_product'),
path('wishlist_page', views.wishlist_page, name='wishlist_page'),
path('cart_page', views.cart_page, name='cart_page'),


]


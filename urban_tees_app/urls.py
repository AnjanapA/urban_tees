from django.urls import path
from . import views

urlpatterns = [
path('main',views.main,name='main'),
path('admin_view_product',views.admin_view_product,name='admin_view_product'),


path('admin_operations',views.admin_operations,name='admin_operations'),
path('image_preview',views.image_preview,name='image_preview'),
path('admin_add_layout',views.admin_add_layout,name='admin_add_layout'),
path('admin_edit_layout',views.admin_edit_layout,name='admin_edit_layout'),
path('admin_edit_layout/<int:id>',views.admin_edit_layout,name='admin_edit_layout'),
path('admin_update_layout',views.admin_update_layout,name='admin_update_layout'),
path('admin_delete_layout/<int:id>',views.admin_delete_layout,name='admin_delete_layout'),
path('user_layout',views.user_layout,name='user_layout'),

]


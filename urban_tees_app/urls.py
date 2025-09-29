from django.urls import path
from . import views

urlpatterns = [
path('main',views.main,name='main'),

path('admin_operations',views.admin_operations,name='admin_operations'),

path('image_preview',views.image_preview,name='image_preview'),

path('admin_layout',views.admin_layout,name='admin_layout'),
path('admin_add_layout',views.admin_add_layout,name='admin_add_layout'),
path('admin_view_layout',views.admin_view_layout,name='admin_view_layout'),

path('admin_edit/<int:id>',views.admin_edit,name='admin_edit'),
path('admin_edit_layout',views.admin_edit_layout,name='admin_edit_layout'),
path('admin_delete_layout/<int:id>',views.admin_delete_layout,name='admin_delete_layout'),
path('user_layout',views.user_layout,name='user_layout'),

]


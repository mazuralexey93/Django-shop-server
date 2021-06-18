from django.urls import path

from admins.views import index, admin_users, admin_users_delete, admin_users_update, admin_users_create, admin_users_undelete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users', admin_users, name='admin_users'),
    path('users/create', admin_users_create, name='admin_users_create'),
    path('users/update/<int:id>/', admin_users_update, name='admin_users_update'),
    path('users/delete/<int:id>/', admin_users_delete, name='admin_users_delete'),
    path('users/undelete/<int:id>/', admin_users_undelete, name='admin_users_undelete'),

]

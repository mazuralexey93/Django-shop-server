from django.urls import path

from admins.views import index, UserListView, admin_users_delete, admin_users_update, UserCreateView,\
    admin_users_undelete, admin_categories, admin_categories_create, admin_categories_update, admin_categories_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:id>/', admin_users_update, name='admin_users_update'),
    path('users/delete/<int:id>/', admin_users_delete, name='admin_users_delete'),
    path('users/undelete/<int:id>/', admin_users_undelete, name='admin_users_undelete'),

    path('categories/', admin_categories, name='admin_categories'),
    path('categories/create', admin_categories_create, name='admin_categories_create'),
    path('categories/update/<int:id>/', admin_categories_update, name='admin_categories_update'),
    path('categories/delete/<int:id>/', admin_categories_delete, name='admin_categories_delete'),

]

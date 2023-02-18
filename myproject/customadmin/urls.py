from django.urls import path
from . import views

urlpatterns = [
    path("",views.admin_login,name='admin_login'),
    path("home",views.index,name='admin_home'),
    path('users',views.show_users,name='user_admin_home'),
    path('logout',views.logout,name='logout'),
    path('user_edit!<id>',views.edit_user,name='edit_user'),
    path("user_delete!<id>",views.delete_user,name="delete_user"),
    path('search_user',views.searched_user,name='product_search_page'),
    path('add_user',views.add_user,name='add_user')
]

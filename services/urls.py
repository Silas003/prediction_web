from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('create/',views.create,name='create'),
    path('logout/',views.logoutpage,name='logout'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    
]
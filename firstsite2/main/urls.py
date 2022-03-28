from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('my_works', views.my_works, name='my_works'),
    path('shop', views.shop, name='shop'),
    path('add_post', views.add_post, name='add_post'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]

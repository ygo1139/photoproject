"""Djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),

    path('post/', views.CreatePhotoView.as_view(), name='post'),

    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),

    path('photos/<int:category>',
         views.CategoryView.as_view(),
         name='photos_cat'),

    path('user-list/<int:user>',
         views.UserView.as_view(),
         name='user_list'),

    path('photo-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'photo_detail'
         ),

    path('mypage/',
         views.MypageView.as_view(),
         name = 'mypage'
         ),

    path('photo/<int:pk>/delete/',
         views.PhotoDeleteView.as_view(),
         name ='photo_delete'),

]


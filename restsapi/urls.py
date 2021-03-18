"""restsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest.views import UserViewSet, GroupViewSet, CategoryViewset, RegisterView
from rest import views
# from .views import Postlist, Postdetail
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'category', CategoryViewset)
router.register(r'register', RegisterView)
urlpatterns = [
    path('', views.ApiRoot.as_view(), name='apiroot'),
    # path('', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.UserList.as_view(), name='users'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='userdetail'),
    path('admin/', admin.site.urls),
    path('postlist/', views.Postlist.as_view(), name='postlist'),
    path('post_detail/<int:pk>/', views.Postdetail.as_view(), name='post_detail'),
    path('category/', views.CategoryList.as_view(), name='category'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('cats/', views.CategoryCreate.as_view(), name='cats'),
]


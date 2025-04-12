"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from.import views

urlpatterns = [
    # path('post', views.post_view, name='post'), 
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('fraud',views.fraud,name='fraud'),
    path('user_login',views.user_login,name='user_login'),
    path('dfraud',views.dfraud,name='dfraud'),
    path('insertuser',views.insertuser,name='insertuser')
    # path('cause',views.cause,name='cause'),
    # path('insertFir',views.insertFir,name='insertFir'),
    # path('insertcause',views.insertcause,name='insertcause')
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

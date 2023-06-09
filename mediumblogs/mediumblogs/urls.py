"""
URL configuration for mediumblogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mediumapp import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('listview/',views.post_list),
    # path('',views.post_list),

    path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/listview/',
views.post_detail, name='post_detail'),
    # path('<int:pk>/', views.post_detail,),

    # path('listview/<int:pk>/', views.post_detail),
    # path('detailview/',views.post_detail)


]

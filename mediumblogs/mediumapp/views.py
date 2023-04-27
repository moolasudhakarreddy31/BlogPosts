from django.shortcuts import render
from mediumapp.models import Post




# Create your views here.



def post_list(request):
    posts=Post.objects.all()
    return render(request,'mediumapp/listview.html',{'posts':posts})
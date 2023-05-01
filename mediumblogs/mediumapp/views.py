from django.shortcuts import render,get_object_or_404
from mediumapp.models import Post
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger



# Create your views here.


# def post_list(request):
#     posts=Post.objects.all()
#     paginator=paginator(post_list,6)
#     page_number=request.GET.get('page')
#     try:
#         post_list=paginator.page(page_number)
#     except PageNotAnInteger:
#         post_list=paginator.page(1)
#     except EmptyPage:
#         post_list=paginator.page(paginator.num_pages)
#         return render(request,'mediumapp/listview.html',{'posts':posts})

from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'mediumapp/listview.html', {'posts': post_list})


def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,
                        #    slug=slug,
                           status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    
    return render(request,'mediumapp/detailview.html',{'post':post})






from django.core.mail import send_mail
from mediumapp.forms import EmailSendForm

def mail_send_view(request,id):
    post=get_object_or_404(post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form .is_valid():
            cd=form.cleaned_data
            send_mail('subject','message','reddy@blog.com',[cd['to']])
            sent=True

        else:
            form=EmailSendForm()
        return render(request,'mediumapp/sharebymail.html',{'post':post,'form':form,'sent':sent})
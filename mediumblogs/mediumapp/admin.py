from django.contrib import admin
from mediumapp.models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish',
                  'created','updated','status']            #This line is in admin page display's this fields
    search_fields=('title','body')                          #serach fields
    raw_id_fields=('author',)                               #serach auther id number
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}                 #This line is in admin page display's title fields as siug fiels














admin.site.register(Post,PostAdmin)
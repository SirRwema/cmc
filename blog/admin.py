from django.contrib import admin
from .models import BlogPost,BlogIndex


admin.site.register(BlogPost)
admin.site.register(BlogIndex)
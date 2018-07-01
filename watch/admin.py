from django.contrib import admin
from .models import Profile,Business,Neighbourhood,Post
# Register your models here.
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(Post)
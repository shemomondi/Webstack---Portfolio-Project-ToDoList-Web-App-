from django.contrib import admin
from  .models import todo
from .models import Profile

# Register your models here.    
admin.site.register(todo)


admin.site.register(Profile)
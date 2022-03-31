from django.contrib import admin
from .models import Book, Category, Type, Comment

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Comment)

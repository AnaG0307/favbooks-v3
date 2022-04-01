from django.contrib import admin
from .models import Book, Category, Type, Comment, Sub_Category


# Class to show book information on the displayed list in the Admin Site
# and order by author


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'author',
        'title',
        'book_category',
        'book_sub_category',
        'book_type',
        'cover',
    )

    ordering = ('author',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'book_category',
        'book_friendly_category',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'book_sub_category',
        'book_friendly_sub_category',
    )


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'book_type',
        'book_friendly_type',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, SubCategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Comment)

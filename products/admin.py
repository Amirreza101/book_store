from multiprocessing.resource_tracker import register

from django.contrib import admin

from products.models import Books, Category


# Register your models here.

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'language', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']
    prepopulated_fields = {
        'slug' : ['title']
    }

    @admin.register(Category)
    class CategoryAdmin(admin.ModelAdmin):
        list_display = ['name', 'slug']

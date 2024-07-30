from django.contrib import admin

from online_shop.models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)

from django.contrib import admin
from online_shop.models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'created_at')
    list_filter = ('product',)
    search_fields = ('text',)

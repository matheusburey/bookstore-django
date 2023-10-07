from django.contrib import admin

# Register your models here.
from core.models import Author, Book, Category, Order, OrderItem, PublishingCompany

admin.site.register(Category)
admin.site.register(PublishingCompany)
admin.site.register(Author)
admin.site.register(Book)


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

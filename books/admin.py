from django.contrib import admin
from .models import Author,Book,Review

class Authoradmin(admin.ModelAdmin):
    list_display=['name','brith_date']
    list_filter=['name','brith_date']
    search_fields=['name']

# Register your models here.
admin.site.register(Author,Authoradmin)
admin.site.register(Book)
admin.site.register(Review)

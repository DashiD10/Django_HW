from django.contrib import admin
from .models import Order, Master, Service, Review


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration', 'is_popular']
    list_filter = ['is_popular']
    search_fields = ['name', 'description']
    list_editable = ['is_popular']


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'experience', 'is_active']
    list_filter = ['is_active', 'experience']
    search_fields = ['name', 'phone']
    filter_horizontal = ['services']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'phone', 'master', 'status', 'appointment_date', 'date_created']
    list_filter = ['status', 'date_created', 'master']
    search_fields = ['client_name', 'phone']
    filter_horizontal = ['services']
    date_hierarchy = 'date_created'
    list_editable = ['status']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'master', 'rating', 'is_published', 'created_at']
    list_filter = ['rating', 'is_published', 'master']
    search_fields = ['client_name', 'text']
    list_editable = ['is_published']
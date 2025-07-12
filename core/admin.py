from django.contrib import admin
from .models import Order, Master, Service, Review


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    """Административная панель для модели Master."""
    list_display = ('name', 'phone', 'experience', 'is_active')
    list_filter = ('is_active', 'experience')
    search_fields = ('name', 'phone')
    filter_horizontal = ('services',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Административная панель для модели Service."""
    list_display = ('name', 'price', 'duration', 'is_popular')
    list_filter = ('is_popular',)
    search_fields = ('name', 'description')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Административная панель для модели Order."""
    list_display = ('client_name', 'phone', 'master', 'status', 'appointment_date', 'date_created')
    list_filter = ('status', 'date_created', 'master')
    search_fields = ('client_name', 'phone')
    filter_horizontal = ('services',)
    date_hierarchy = 'appointment_date'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Административная панель для модели Review."""
    list_display = ('client_name', 'master', 'rating', 'is_published', 'created_at')
    list_filter = ('rating', 'is_published', 'created_at', 'master')
    search_fields = ('client_name', 'text')

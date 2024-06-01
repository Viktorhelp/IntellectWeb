from django.contrib import admin
from .models import Equipment
from .models import SalesRequest

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'type', 'model', 'serial_number', 'mac_address', 'responsible_person')



@admin.register(SalesRequest)
class SalesRequestAdmin(admin.ModelAdmin):
    list_display = ('company', 'order_number', 'inclusion_date', 'city', 'street', 'apartment_number', 'contact_person', 'equipment')
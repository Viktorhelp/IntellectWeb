from django.urls import path
from .views import home_view, login_view, register_view
from .import views
from .views import cable_list_view, add_cable_view
from .views import sales_request_list, add_sales_request




urlpatterns = [
    path('home/', home_view, name='home'),  # URL для главной страницы
    path('', login_view, name='login'),  # URL для страницы входа
    path('register/', register_view, name='register'),  # URL для страницы регистрации
    path('vodafon/', views.vodafon_view, name='vodafon'), #URL для перехода на Водафон
    path('inclusion/', views.inclusion_view, name='inclusion'),#URL для перехода на список заявок
    path ('stock/', views.stock_view, name='stock'), #URL для перехода на склад
    path('add_warehouse/', views.add_warehouse_view, name='add_warehouse'),
    path('add_cable/', add_cable_view, name='add_cable'),
    path('cable/', views.cable_list_view, name='cable_list'),  # URL для списка кабелей
    path('export-to-excel/', views.export_to_excel_view, name='export_to_excel'), #URL для выгрузки в ексель 
    path('add_sales_request/', add_sales_request, name='add_sales_request'),
    path('sales_request_list/', sales_request_list, name='sales_request_list'),
    path('network_equipment/', views.network_equipment, name='network_equipment'),
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('edit_equipment/<int:pk>/', views.edit_equipment, name='edit_equipment'),
    path('export_equipment_to_excel/', views.export_equipment_to_excel, name='export_equipment_to_excel'),
    ]

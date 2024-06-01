
from django import forms
from .models import Warehouse  # модель Warehouse для хранения информации о складах
from .models import Cable
from .models import SalesRequest
from .models import Equipment

# Поля, которые будут отображаться в форме для добавления склада
#Модель для хранения информации склада
class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields =['name', 'address', 'phone']  

#Поля, которые будут отображаться в форме для добавления кабеля
#Модель для кабеля 
class CableForm(forms.ModelForm):
    class Meta:
        model = Cable
        fields = ['company', 'order_number', 'inclusion_date', 'city', 'street', 'apartment_number', 'contact_person', 'equipment'] 


#Форма для отображения новой заявки
#Поля которые отображаються при заполении формы добавления новой заявки
class SalesRequestForm(forms.ModelForm):
    class Meta:
        model = SalesRequest
        fields = ['company', 'order_number', 'inclusion_date', 'city', 'street', 'apartment_number', 'contact_person', 'equipment', ] 



class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'

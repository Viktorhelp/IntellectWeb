
import re
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import WarehouseForm
from .forms import CableForm
from .models import Cable
import pandas as pd
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from .models import SalesRequest
from .forms import SalesRequestForm
from .forms import EquipmentForm
from .forms import Equipment
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, Permission
from .forms import EquipmentForm
from django.shortcuts import get_object_or_404
from .models import CommonRequest







#Обработка вход наглавную страницу
def home_view(request):
    # is_vodafone - это флаг, который определяет, вошел ли пользователь в Водафон
    is_vodafone = True  # Установления  значение в соответствии с  логикой
    # is_ukrtelekom - это флаг, который определяет, вошел ли пользователь в Укртелком
    is_ukrtelekom = True  # Здесь Установленно значения в соответствии с логикой
    is_kyivstar = True #установленно значения в соответствии с логикой
    is_datagrup =True #Установленно значения в соответсвии с логикой 
    return render(request, 'home.html', {'is_vodafone': is_vodafone, 'is_ukrtelekom': is_ukrtelekom, 'is_kyivstar': is_kyivstar, 'is_datagrup': is_datagrup })


#Обработка логина входа. 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Аутентификация пользователя
            user = authenticate(username=username, password=password)
            if user is not None:
                # Вход выполнен успешно
                login(request, user)
                return redirect('home')  # Перенаправление на страницу Home
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


#Обработка регистрации 
def register_view(request):
    return render(request, 'registration/register.html')

# Обработка страницы Водафон
def vodafon_view(request):
    return render(request, 'vodafon.html')

#Обработка включения 
def inclusion_view(request):
    return render(request, 'inclusion.html' )

#Обработка складов
def stock_view(request):
    return render(request, 'stock.html')

#Форма для обработки склада
def add_warehouse_view(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            # Если форма корректна, сохраняем данные склада в базу данных
            form.save()
            # После сохранения перенаправляем пользователя на страницу со складами или куда-либо еще
            return redirect('stock')  # 'stock' - это имя URL для страницы со складами
    else:
        # Если запрос не POST, создаем пустую форму для добавления склада
        form = WarehouseForm()
    
    # Отображаем страницу добавления склада с формой
    return render(request, 'add_warehouse.html', {'form': form})



# Отображения страницу для добавления кабеля
def add_cable_view(request):
    if request.method == 'POST':
        form = CableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cable_list')  # Перенаправление на страницу cable_list.html
    else:
        form = CableForm()
    return render(request, 'add_cable.html', {'form': form})



# Обработка списка кабеля 
def cable_list_view(request):
    cables = Cable.objects.all()
    return render(request, 'cable_list.html', {'cables': cables})

#Обработка вывода екселя. 
def export_to_excel_view(request):
    try:
        # Получение всех объектов Cable из базы данных
        cables = Cable.objects.all()    

        # Создание списка словарей с данными кабелей
        data = [{'Наименование': cable.name, 'Артикул': cable.article, 'Метраж': cable.length} for cable in cables]

        # Создание DataFrame
        df = pd.DataFrame(data)

        # Создание объекта ExcelWriter и запись данных DataFrame в файл Excel
        with pd.ExcelWriter('cable.xlsx') as excel_writer:
            df.to_excel(excel_writer, index=False)

        # Возврат HttpResponse с содержимым файла Excel
        with open('cable.xlsx', 'rb') as file:
            file_content = file.read()
            response = HttpResponse(file_content, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=cable.xlsx'  # Заголовок для скачивания файла
        return response

    except Exception as e:
        return HttpResponse('An error occurred while exporting to Excel. Please try again later.')



#Обработка вывода список заявок продаж 
def sales_request_list(request):
    sales_requests = SalesRequest.objects.all()
    common_requests = CommonRequest.objects.all()
    return render(request, 'sales_request_list.html', {'sales_requests': sales_requests, 'common_requests': common_requests})



# Обработка добавления новой заявки в заявки продаж
def add_sales_request(request):
    if request.method == 'POST':
        form = SalesRequestForm(request.POST)
        if form.is_valid():
            sales_request = form.save(commit=False)
            sales_request.save()

            # Создайте новую общую заявку на основе данных заявки продаж
            common_request = CommonRequest(
                name=sales_request.company,
                order_number=sales_request.order_number,
                date=sales_request.date,
                address=sales_request.address,
                location=sales_request.location,
                contact_person=sales_request.contact_person
            )
            common_request.save()

            return redirect('sales_request_list')  # Изменено на redirect('sales_request_list')

    else:
        form = SalesRequestForm()

    return render(request, 'add_sales_request.html', {'form': form})



#Обработка сетевого оборудования 
def network_equipment(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment_table.html',  {'equipment': equipment})


#Обработка сетевого оборудования 
@login_required
def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            print("Equipment added successfully")  # Временный вывод в консоль
            return redirect('network_equipment')
        else: 
            print("Form is invalid:", form.errors)  # Временный вывод ошибок в консоль

    else:
        form = EquipmentForm()

    return render(request, 'add_equipment.html', {'form': form})


#Обработка для редактирования оборудования 
def edit_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('network_equipment')
    else:
        form = EquipmentForm(instance=equipment)

    return render(request, 'edit_equipment.html', {'form': form})


#Обработка выгрузки в Ексель оборудования 
def export_equipment_to_excel(request):
    # Получение данных об оборудовании
    equipment = Equipment.objects.all()
    
    # Создание DataFrame с данными об оборудовании
    data = {
        'Name': [eq.name for eq in equipment],
        'Status': [eq.status for eq in equipment],
        'Type': [eq.type for eq in equipment],
        'Model': [eq.model for eq in equipment],
        'Serial Number': [eq.serial_number for eq in equipment],
        'MAC Address': [eq.mac_address for eq in equipment],
        'Responsible Person': [eq.responsible_person for eq in equipment],
    }
    df = pd.DataFrame(data)
    
    # Создание объекта ExcelWriter и запись данных DataFrame в файл Excel
    with pd.ExcelWriter('equipment.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    
    # Отправка файла Excel в ответе HTTP
    with open('equipment.xlsx', 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=equipment.xlsx'
    
    return response

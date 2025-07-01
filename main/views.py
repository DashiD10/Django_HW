from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

# Тестовые данные для заявок
ORDERS_DATA = [
    {
        'id': 1,
        'client_name': 'Иван Петров',
        'phone': '+7 (999) 123-45-67',
        'date': '2025-01-15',
        'time': '14:00',
        'services': ['Стрижка', 'Борода'],
        'master': 'Алексей Смирнов',
        'status': 'new',
        'status_display': 'Новая',
        'notes': 'Клиент просит короткую стрижку'
    },
    {
        'id': 2,
        'client_name': 'Михаил Козлов',
        'phone': '+7 (888) 987-65-43',
        'date': '2025-01-16',
        'time': '16:30',
        'services': ['Стрижка', 'Укладка'],
        'master': 'Дмитрий Волков',
        'status': 'confirmed',
        'status_display': 'Подтверждена',
        'notes': 'Постоянный клиент'
    },
    {
        'id': 3,
        'client_name': 'Сергей Николаев',
        'phone': '+7 (777) 555-33-22',
        'date': '2025-01-17',
        'time': '12:00',
        'services': ['Борода', 'Усы'],
        'master': 'Алексей Смирнов',
        'status': 'completed',
        'status_display': 'Выполнена',
        'notes': 'Требует особый подход к бороде'
    }
]

def landing(request):
    """
    Главная страница (лендинг) барбершопа
    """
    context = {
        'page_title': 'Главная',
        'services': [
            {'name': 'Мужская стрижка', 'price': '1500 ₽'},
            {'name': 'Стрижка бороды', 'price': '800 ₽'},
            {'name': 'Укладка', 'price': '500 ₽'},
            {'name': 'Комплекс', 'price': '2500 ₽'},
        ],
        'masters': [
            {'name': 'Алексей Смирнов', 'experience': '5 лет'},
            {'name': 'Дмитрий Волков', 'experience': '3 года'},
        ]
    }
    return render(request, 'landing.html', context)

def thanks(request):
    """
    Страница благодарности за поданную заявку
    """
    context = {
        'page_title': 'Спасибо за заявку',
    }
    return render(request, 'thanks.html', context)

def is_staff_user(user):
    """
    Проверка, является ли пользователь сотрудником
    """
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff_user)
def orders_list(request):
    """
    Список заявок (доступен только для staff пользователей)
    """
    context = {
        'page_title': 'Список заявок',
        'orders': ORDERS_DATA,
    }
    return render(request, 'orders_list.html', context)

@user_passes_test(is_staff_user)
def order_detail(request, order_id):
    """
    Детальная информация о заявке
    """
    # Ищем заявку по ID
    order = None
    for o in ORDERS_DATA:
        if o['id'] == order_id:
            order = o
            break
    
    if not order:
        raise Http404("Заявка не найдена")
    
    context = {
        'page_title': f'Заявка #{order_id}',
        'order': order,
    }
    return render(request, 'order_detail.html', context)

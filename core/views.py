from django.shortcuts import render

# Данные из задания
masters = [
    {"id": 1, "name": "Эльдар 'Бритва' Рязанов"},
    {"id": 2, "name": "Зоя 'Ножницы' Космодемьянская"},
    {"id": 3, "name": "Борис 'Фен' Пастернак"},
    {"id": 4, "name": "Иннокентий 'Лак' Смоктуновский"},
    {"id": 5, "name": "Раиса 'Бигуди' Горбачёва"},
]

services = [
    "Стрижка под 'Горшок'",
    "Укладка 'Взрыв на макаронной фабрике'",
    "Королевское бритье опасной бритвой",
    "Окрашивание 'Жизнь в розовом цвете'",
    "Мытье головы 'Душ впечатлений'",
    "Стрижка бороды 'Боярин'",
    "Массаж головы 'Озарение'",
    "Укладка 'Ветер в голове'",
    "Плетение косичек 'Викинг'",
    "Полировка лысины до блеска"
]

# Статусы и заказы (полный список из задания)
STATUS_NEW = 'новая'
STATUS_CONFIRMED = 'подтвержденная'
STATUS_CANCELLED = 'отмененная'
STATUS_COMPLETED = 'выполненная'

orders = [
    # ... полный список заказов из задания
]

def landing(request):
    context = {
        'masters': masters,
        'services': services
    }
    return render(request, 'landing.html', context)

def thanks(request):
    return render(request, 'core/thanks.html')

def orders_list(request):
    context = {
        'orders': orders
    }
    return render(request, 'core/orders_list.html', context)

def order_detail(request, order_id):
    order = None
    for o in orders:
        if o['id'] == order_id:
            order = o
            break
    
    # Найти мастера по master_id
    master = None
    if order:
        for m in masters:
            if m['id'] == order['master_id']:
                master = m
                break
    
    context = {
        'order': order,
        'master': master
    }
    return render(request, 'core/order_detail.html', context)



# Create your views here.

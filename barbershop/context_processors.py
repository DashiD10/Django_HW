from datetime import datetime

def menu_context(request):
    """
    Контекстный процессор для передачи данных меню во все шаблоны
    """
    menu_items = [
        {'name': 'Главная', 'url': 'landing', 'anchor': False},
        {'name': 'О нас', 'url': '#about', 'anchor': True},
        {'name': 'Услуги', 'url': '#services', 'anchor': True},
        {'name': 'Мастера', 'url': '#masters', 'anchor': True},
        {'name': 'Запись', 'url': '#booking', 'anchor': True},
    ]
    
    # Добавляем пункт для staff пользователей
    if request.user.is_authenticated and request.user.is_staff:
        menu_items.append({'name': 'Заявки', 'url': 'orders_list', 'anchor': False})
    
    return {
        'site_name': 'Барбершоп "Стальная Борода"',
        'menu_items': menu_items,
    }
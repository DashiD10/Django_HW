def menu_context(request):
    """Add menu-related context to all templates"""
    return {
        'site_name': 'Steel Beard Barbershop',
        'current_year': 2025,
    }

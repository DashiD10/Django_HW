from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def landing(request):
    """Main landing page with barbershop information"""
    return render(request, 'barbershop/landing.html')

def thanks(request):
    """Thank you page after order submission"""
    return render(request, 'barbershop/thanks.html')

@user_passes_test(lambda u: u.is_staff)
def orders_list(request):
    """List of orders - staff only"""
    # Add your test data here
    orders = [
        {
            'id': 1,
            'client_name': 'John Doe',
            'date': '2025-01-15',
            'services': ['Haircut', 'Beard trim'],
            'master': 'Mike',
            'status': 'new'
        },
        # Add more test orders
    ]
    return render(request, 'barbershop/orders_list.html', {'orders': orders})

@user_passes_test(lambda u: u.is_staff)
def order_detail(request, order_id):
    """Order detail view - staff only"""
    # Add your test data here
    order = {
        'id': order_id,
        'client_name': 'John Doe',
        'phone': '+1234567890',
        'date': '2025-01-15',
        'time': '14:00',
        'services': ['Haircut', 'Beard trim'],
        'master': 'Mike',
        'status': 'new',
        'notes': 'Customer prefers short haircut'
    }
    return render(request, 'barbershop/order_detail.html', {'order': order})

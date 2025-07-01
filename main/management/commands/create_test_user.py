from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Создает тестового пользователя для демонстрации'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@barbershop.com',
                password='admin123',
                is_staff=True
            )
            self.stdout.write(
                self.style.SUCCESS('Тестовый пользователь создан: admin/admin123')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Пользователь admin уже существует')
            )

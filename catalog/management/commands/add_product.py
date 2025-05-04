from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Добавление продукта в базу данных'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'catalog_fixture.json')
        category, _ = Category.objects.get_or_create(name='Ягоды')

        products = [
            {'name': 'Малина', 'description': 'Красная', 'category': category, 'purchase_price': '25', 'created_at': '2025-05-04', 'updated_at': '2025-05-04'},
            {'name': 'Клубника', 'description': 'Красная', 'category': category, 'purchase_price': '30', 'created_at': '2025-05-04', 'updated_at': '2025-05-04'}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Добавление продукта прошло успешно: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже существует: {product.name}'))

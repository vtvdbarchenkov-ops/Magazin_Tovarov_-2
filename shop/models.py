from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.TextField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    def __str__(self):
        return self.name
class Warranty(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name='Товар')
    date = models.DateField(verbose_name='Дата начала гарантии')
    service_center = models.CharField(max_length=100, verbose_name='Сервисный центр')
    def __str__(self):
        return self.product.name
class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=11, verbose_name="Телефон")
    def __str__(self):
        return self.name
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Покупатель")
    products = models.ManyToManyField(Product, verbose_name="Товары")
    def __str__(self):
        return self.customer.name
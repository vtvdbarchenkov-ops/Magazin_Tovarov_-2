from django import forms
from .models import Category, Product, Warranty, Customer, Order
from datetime import datetime


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Название должно быть больше 3 символов")
        return name


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Название должно быть больше 3 символов")
        return name


class WarrantyForm(forms.ModelForm):
    class Meta:
        model = Warranty
        fields = ['product', 'date', 'service_center']

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.now().date():
            raise forms.ValidationError("Дата должна быть больше текущей даты")
        return date


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'email', 'phone']

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith(('@gmail.com', '@yandex.ru', '@mail.ru', '@yahoo.com', '@outlook.com', '@hotmail.com', '@icloud.com')):
            raise forms.ValidationError("Email должен быть на gmail.com, yandex.ru, mail.ru, yahoo.com, outlook.com, hotmail.com или icloud.com")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.startswith('+7') or len(phone) != 11:
            raise forms.ValidationError("Телефон должен начинаться с +7 и быть 11 цифр")
        return phone


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'products']

    def clean_customer(self):
        customer = self.cleaned_data['customer']
        if not customer.name or not customer.last_name or not customer.email or not customer.phone:
            raise forms.ValidationError("Поля Имя, Фамилия, Email и Телефон обязательны для заполнения")
        return customer

    def clean_products(self):
        products = self.cleaned_data['products']
        if not products:
            raise forms.ValidationError("Необходимо выбрать хотя бы один товар")
        return products

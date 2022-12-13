from django.db import models
from django.contrib.auth.models import User

GENDERS = [
    ('М', 'мужчина'),
    ('Ж', 'женщина'),
]

TAGS = [
    ('Г', 'горячий'),
    ('П', 'постоянный'),
    ('В', 'вип'),
    ('С', 'скандальный'),
    ('Н', 'новый'),
]

class Client(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField("Роль", default="Клиент", max_length=30, blank=True)
    surname = models.CharField("Фамилия", max_length=30, blank=True)
    name = models.CharField("Имя", max_length=30, blank=True)
    patronymic = models.CharField("Отчество", max_length=30, blank=True)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=15, blank=True)
    e_mail = models.CharField("Почтовый адрес", max_length=50, blank=True)
    gender = models.CharField("Пол", max_length=50, blank=True, choices=GENDERS)
    DOR = models.DateField("Дата регистрации", null=True, blank=True)
    photo = models.ImageField("Фото", null=True, blank=True)
    tag = models.CharField("Тег", max_length=50, blank=True, choices=TAGS)

    def __str__(self):
        return f'{self.user} - {self.surname} {self.name} - {self.tag}'

class Service(models.Model):
    title = models.CharField("Услуга", max_length=100, blank=True)
    description = models.CharField("Описание", max_length=100, blank=True)
    price = models.PositiveIntegerField("Цена", max_length=100, blank=True)
    duration = models.PositiveIntegerField("Длительность (часов)", max_length=100, blank=True)
    photo = models.ImageField("Фото")

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    title = models.CharField("Категория", max_length=100, blank=True)

    def __str__(self):
        return self.title

class Production(models.Model):
    title = models.CharField("Производитель", max_length=100, blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField("Продукт", max_length=100, blank=True)
    description = models.CharField("Описание", max_length=100, blank=True)
    price = models.PositiveIntegerField("Цена", blank=True)
    weight = models.PositiveIntegerField("Вес",  blank=True)
    size = models.PositiveIntegerField("Обьем в см. куб.", blank=True)
    category = models.ForeignKey(ProductCategory, verbose_name="Категория", on_delete=models.CASCADE)
    production = models.ForeignKey(Production, verbose_name="Производитель", on_delete=models.CASCADE)
    photo = models.ImageField("Фото")

    def __str__(self):
        return self.title
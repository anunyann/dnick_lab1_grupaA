from django.db import models
from django.contrib.auth.models import User


class Market(models.Model):
    name = models.CharField(max_length=200)
    number_of_markets = models.IntegerField()
    opening_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opening_time = models.TimeField()
    closing_time = models.TimeField()


    def __str__(self):
        return f"{self.name}"

class ContactInfo(models.Model):
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    market = models.OneToOneField(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street} {self.street_number} {self.phone_number}, {self.email}"

class Employee(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    ssn = models.CharField(max_length=13)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Product(models.Model):
    TYPE_CHOICES = [
        ("F", "Food"),
        ("D", "Drink"),
        ("B", "Bakery"),
        ("C", "Cosmetics"),
        ("H", "Hygiene")
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    is_domestic = models.BooleanField()
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} {self.code}"

class MarketProduct(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.market.name} - {self.product.name} {self.quantity}"

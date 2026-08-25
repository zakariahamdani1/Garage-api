from django.db import models
from django.core.validators import MinValueValidator

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cars")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Mechanic(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Repair(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="repairs")
    mechanic = models.ForeignKey(Mechanic, on_delete=models.PROTECT, related_name="repairs")
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car} - {self.description}"
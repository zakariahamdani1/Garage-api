from rest_framework import serializers
from .models import Customer, Car, Mechanic, Repair

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "make", "model", "year", "vin", "owner", "created_at"]

class CustomerSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ["id", "name", "phone", "email", "cars"]

class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = ["id", "name", "phone"]

class RepairSerializer(serializers.ModelSerializer):
    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Description cannot be empty."
            )
        return value
    class Meta:
        model = Repair
        fields = ["id","car", "mechanic", "description", "cost", "created_at"]
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import generics

from .models import Customer, Car, Mechanic, Repair
from .serializers import CustomerSerializer, CarSerializer, MechanicSerializer, RepairSerializer


# ******** Customers List *********************

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

# ************** Car List ***********************

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

# ************** Mechanic List ***********************

class MechanicListCreateView(generics.ListCreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class MechanicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

# **************** Repair List ************************

class RepairListCreateView(generics.ListCreateAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class RepairDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

# *********** Car Repairs ******************

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def car_repairs(request, pk):
    car = get_object_or_404(Car, pk=pk)
    repairs = car.repairs.all()
    serializer = RepairSerializer(repairs, many=True)

    return Response(serializer.data)

# ************* Customer Cars ********************

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def customer_cars(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    cars = customer.cars.all()
    serializer = CarSerializer(cars, many=True)

    return Response(serializer.data)


# **************** Mechanic Repairs ********************

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def mechanic_repairs(request, pk):
    mechanic = get_object_or_404(Mechanic, pk=pk)

    repairs = mechanic.repairs.all()
    serializer = RepairSerializer(repairs, many=True)

    return Response(serializer.data)
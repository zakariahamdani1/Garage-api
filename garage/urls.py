from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    CarListCreateView,
    CarDetailView,
    MechanicListCreateView,
    MechanicDetailView,
    RepairListCreateView,
    RepairDetailView,
    CustomerListCreateView,
    CustomerDetailView,  
    car_repairs,
    customer_cars,
    mechanic_repairs,
    )


urlpatterns = [
    path("login/", obtain_auth_token),

    path("customers/", CustomerListCreateView.as_view()),
    path("customers/<int:pk>/", CustomerDetailView.as_view()),
    
    path("cars/", CarListCreateView.as_view()),
    path("cars/<int:pk>/", CarDetailView.as_view()),
    path("cars/<int:pk>/repairs/", car_repairs),
    path("customers/<int:pk>/cars/", customer_cars),

    path("mechanics/", MechanicListCreateView.as_view()),
    path("mechanics/<int:pk>/", MechanicDetailView.as_view()),
    path("mechanics/<int:pk>/repairs/", mechanic_repairs),

    path("repairs/", RepairListCreateView.as_view()),
    path("repairs/<int:pk>/", RepairDetailView.as_view()),
]
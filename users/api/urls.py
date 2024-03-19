from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customers',CustomerViewset)
router.register(r'customer-interaction',CustomerInteractionViewset)
router.register(r'employees',EmployeeViewset)
router.register(r'roleset',RoleViewset)
router.register('employee-travel-allowance',EmployeeTravelAllowanceViewset)

urlpatterns = [
    path('api/register/',Register.as_view(),name='register'),
    path('api/login/',Login.as_view(),name='login'),
    path('api/logout/',Logout.as_view(),name='logout'),
    path('api/',include(router.urls))
]

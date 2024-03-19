from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
  list_display = ["role_id", "name"]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
  list_display = ["name", "username","role"]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ["customer_id", "name","employee"]
@admin.register(CustomerInteraction)
class CutomerInteractionAdmin(admin.ModelAdmin):
  list_display = ["prospect_status","outcome","visiting_date"]

@admin.register(EmployeeTravelAllowance)
class EmployeeTravelAllowanceAdmin(admin.ModelAdmin):
  list_display = [i.name for i in EmployeeTravelAllowance._meta.fields]
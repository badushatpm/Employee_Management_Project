from django.contrib import admin

from core_app.models import Employee


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'address', 'designation')

    fields = ['name', 'age', 'address', 'designation']


admin.site.register(Employee, EmployeeAdmin)

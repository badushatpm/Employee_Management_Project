from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name

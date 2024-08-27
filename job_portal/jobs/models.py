from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib import admin
from django.db import IntegrityError
from django.contrib import messages

class CustomUser(AbstractUser):
    domain = models.CharField(max_length=100)
    is_experienced = models.BooleanField(default=False)
    resume = models.FileField(upload_to='resumes/')
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add related_name here
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Add related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Job(models.Model):
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    average_package = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField
    is_for_experienced = models.BooleanField(default=False)
    registered_users = models.ManyToManyField(CustomUser, blank=True, related_name='registered_jobs')

    def __str__(self):
        return f"{self.company_name} - {self.role}"

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class JobAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except IntegrityError as e:
            messages.error(request, "Failed to add the job due to a foreign key constraint error.")

admin.site.register(Job, JobAdmin)


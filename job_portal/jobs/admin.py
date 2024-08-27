from django.contrib import admin
from .models import Job, Company , messages , IntegrityError # Import your models

class JobAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except IntegrityError as e:
            messages.error(request, "Failed to add the job due to a foreign key constraint error.")
admin.site.unregister(Job)
admin.site.register(Job, JobAdmin)  # Ensure this is only called once
admin.site.register(Company)

from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'hospital_affiliation', 'consultation_fee', 'is_active', 'created_at')
    list_filter = ('specialization', 'is_active', 'hospital_affiliation', 'created_at')
    search_fields = ('name', 'email', 'license_number', 'hospital_affiliation')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Professional Information', {
            'fields': ('specialization', 'license_number', 'years_of_experience', 
                      'hospital_affiliation', 'consultation_fee', 'availability_hours')
        }),
        ('Additional Information', {
            'fields': ('bio', 'is_active')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

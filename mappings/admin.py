from django.contrib import admin
from .models import PatientDoctorMapping

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'is_primary', 'is_active', 'assigned_date')
    list_filter = ('is_primary', 'is_active', 'assigned_date', 'doctor__specialization')
    search_fields = ('patient__name', 'doctor__name', 'patient__email', 'doctor__email')
    readonly_fields = ('assigned_date', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Assignment Information', {
            'fields': ('patient', 'doctor', 'assigned_date')
        }),
        ('Assignment Details', {
            'fields': ('notes', 'is_primary', 'is_active')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

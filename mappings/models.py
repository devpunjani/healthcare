from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient_mappings')
    assigned_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True, help_text="Additional notes about the assignment")
    is_primary = models.BooleanField(default=False, help_text="Is this the primary doctor for the patient?")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('patient', 'doctor')
        ordering = ['-assigned_date']

    def __str__(self):
        return f"{self.patient.name} -> Dr. {self.doctor.name}"

    def save(self, *args, **kwargs):
        # Ensure only one primary doctor per patient
        if self.is_primary:
            PatientDoctorMapping.objects.filter(
                patient=self.patient, 
                is_primary=True
            ).exclude(pk=self.pk).update(is_primary=False)
        super().save(*args, **kwargs)

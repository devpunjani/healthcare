from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer, DoctorListSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorListSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'doctor', 'patient_details', 'doctor_details',
            'assigned_date', 'notes', 'is_primary', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ('id', 'assigned_date', 'created_at', 'updated_at')

    def validate(self, attrs):
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')
        
        # Check if the patient belongs to the current user
        request = self.context.get('request')
        if request and patient.created_by != request.user:
            raise serializers.ValidationError("You can only assign doctors to your own patients.")
        
        # Check if mapping already exists (for create operation)
        if not self.instance:
            if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
                raise serializers.ValidationError("This doctor is already assigned to this patient.")
        
        return attrs

class PatientDoctorMappingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ['patient', 'doctor', 'notes', 'is_primary']

    def validate(self, attrs):
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')
        
        # Check if the patient belongs to the current user
        request = self.context.get('request')
        if request and patient.created_by != request.user:
            raise serializers.ValidationError("You can only assign doctors to your own patients.")
        
        # Check if mapping already exists
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError("This doctor is already assigned to this patient.")
        
        return attrs

class PatientDoctorMappingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ['notes', 'is_primary', 'is_active']

class DoctorsByPatientSerializer(serializers.ModelSerializer):
    doctor_details = DoctorListSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'doctor', 'doctor_details', 'assigned_date', 
            'notes', 'is_primary', 'is_active'
        ]

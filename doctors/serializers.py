from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'email', 'phone', 'specialization', 
            'license_number', 'years_of_experience', 'hospital_affiliation',
            'consultation_fee', 'availability_hours', 'bio', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_years_of_experience(self, value):
        if value < 0:
            raise serializers.ValidationError("Years of experience cannot be negative.")
        if value > 70:
            raise serializers.ValidationError("Years of experience seems unrealistic.")
        return value

    def validate_consultation_fee(self, value):
        if value < 0:
            raise serializers.ValidationError("Consultation fee cannot be negative.")
        return value

class DoctorCreateSerializer(DoctorSerializer):
    class Meta(DoctorSerializer.Meta):
        pass

class DoctorUpdateSerializer(DoctorSerializer):
    class Meta(DoctorSerializer.Meta):
        pass

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'specialization', 'hospital_affiliation',
            'consultation_fee', 'years_of_experience', 'is_active'
        ]

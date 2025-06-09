from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id', 'name', 'email', 'phone', 'date_of_birth', 
            'gender', 'address', 'medical_history', 
            'emergency_contact', 'emergency_phone', 
            'created_by', 'created_at', 'updated_at'
        ]
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def validate_email(self, value):
        # Check if email is unique for the current user
        user = self.context['request'].user
        queryset = Patient.objects.filter(email=value, created_by=user)
        
        # If updating, exclude current instance
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
            
        if queryset.exists():
            raise serializers.ValidationError("A patient with this email already exists.")
        return value

class PatientCreateSerializer(PatientSerializer):
    class Meta(PatientSerializer.Meta):
        pass

class PatientUpdateSerializer(PatientSerializer):
    class Meta(PatientSerializer.Meta):
        pass

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from patients.models import Patient
from doctors.models import Doctor
from .serializers import (
    PatientDoctorMappingSerializer, PatientDoctorMappingCreateSerializer,
    PatientDoctorMappingUpdateSerializer, DoctorsByPatientSerializer
)

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Users can only see mappings for their own patients
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        ).select_related('patient', 'doctor')

    def get_serializer_class(self):
        if self.action == 'create':
            return PatientDoctorMappingCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return PatientDoctorMappingUpdateSerializer
        return PatientDoctorMappingSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                # Return full mapping details
                mapping = PatientDoctorMapping.objects.get(pk=serializer.instance.pk)
                response_serializer = PatientDoctorMappingSerializer(mapping)
                
                return Response({
                    'message': 'Doctor assigned to patient successfully',
                    'mapping': response_serializer.data
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                'error': 'Assignment failed',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                'error': 'Internal server error',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            page = self.paginate_queryset(queryset)
            
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                'message': 'Patient-doctor mappings retrieved successfully',
                'mappings': serializer.data,
                'count': queryset.count()
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'error': 'Internal server error',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            patient_name = instance.patient.name
            doctor_name = instance.doctor.name
            self.perform_destroy(instance)
            
            return Response({
                'message': f'Dr. {doctor_name} removed from patient {patient_name} successfully'
            }, status=status.HTTP_200_OK)
        
        except PatientDoctorMapping.DoesNotExist:
            return Response({
                'error': 'Mapping not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                'error': 'Internal server error',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def doctors_by_patient(self, request, patient_id=None):
        """Get all doctors assigned to a specific patient"""
        try:
            # Verify patient belongs to current user
            patient = get_object_or_404(
                Patient, 
                id=patient_id, 
                created_by=request.user
            )
            
            mappings = PatientDoctorMapping.objects.filter(
                patient=patient,
                is_active=True
            ).select_related('doctor')
            
            serializer = DoctorsByPatientSerializer(mappings, many=True)
            
            return Response({
                'message': f'Doctors for patient {patient.name} retrieved successfully',
                'patient': {
                    'id': patient.id,
                    'name': patient.name,
                    'email': patient.email
                },
                'doctors': serializer.data,
                'count': mappings.count()
            }, status=status.HTTP_200_OK)
        
        except Patient.DoesNotExist:
            return Response({
                'error': 'Patient not found or you do not have permission to view this patient'
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                'error': 'Internal server error',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def bulk_assign(self, request):
        """Assign multiple doctors to a patient"""
        try:
            patient_id = request.data.get('patient_id')
            doctor_ids = request.data.get('doctor_ids', [])
            notes = request.data.get('notes', '')
            
            if not patient_id or not doctor_ids:
                return Response({
                    'error': 'patient_id and doctor_ids are required'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Verify patient belongs to current user
            patient = get_object_or_404(
                Patient, 
                id=patient_id, 
                created_by=request.user
            )
            
            created_mappings = []
            errors = []
            
            for doctor_id in doctor_ids:
                try:
                    doctor = Doctor.objects.get(id=doctor_id)
                    
                    # Check if mapping already exists
                    if not PatientDoctorMapping.objects.filter(
                        patient=patient, 
                        doctor=doctor
                    ).exists():
                        mapping = PatientDoctorMapping.objects.create(
                            patient=patient,
                            doctor=doctor,
                            notes=notes
                        )
                        created_mappings.append(mapping)
                    else:
                        errors.append(f'Dr. {doctor.name} is already assigned to this patient')
                        
                except Doctor.DoesNotExist:
                    errors.append(f'Doctor with ID {doctor_id} not found')
            
            # Serialize created mappings
            serializer = PatientDoctorMappingSerializer(created_mappings, many=True)
            
            response_data = {
                'message': f'{len(created_mappings)} doctors assigned successfully',
                'created_mappings': serializer.data,
                'created_count': len(created_mappings)
            }
            
            if errors:
                response_data['errors'] = errors
                response_data['error_count'] = len(errors)
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        except Patient.DoesNotExist:
            return Response({
                'error': 'Patient not found or you do not have permission to access this patient'
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                'error': 'Internal server error',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

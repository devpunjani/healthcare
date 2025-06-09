# Django Healthcare Backend

A comprehensive healthcare backend system built with Django, Django REST Framework, and PostgreSQL. This system provides secure user authentication and management of patient and doctor records with proper API endpoints.

## Features

- **User Authentication**: JWT-based authentication with registration and login
- **Patient Management**: Full CRUD operations for patient records
- **Doctor Management**: Complete doctor profile management
- **Patient-Doctor Mapping**: Assign and manage doctor-patient relationships
- **Security**: JWT authentication, user-specific data access
- **Database**: PostgreSQL with proper relationships and constraints
- **API Documentation**: RESTful API endpoints with proper error handling

## Tech Stack

- **Backend**: Django 4.2, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Environment**: Python 3.8+

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - User login

### Patients
- `GET /api/patients/` - List all patients (user's own)
- `POST /api/patients/` - Create new patient
- `GET /api/patients/{id}/` - Get patient details
- `PUT /api/patients/{id}/` - Update patient
- `DELETE /api/patients/{id}/` - Delete patient

### Doctors
- `GET /api/doctors/` - List all doctors
- `POST /api/doctors/` - Create new doctor
- `GET /api/doctors/{id}/` - Get doctor details
- `PUT /api/doctors/{id}/` - Update doctor
- `DELETE /api/doctors/{id}/` - Delete doctor
- `GET /api/doctors/specializations/` - Get available specializations

### Patient-Doctor Mappings
- `GET /api/mappings/` - List all mappings
- `POST /api/mappings/` - Assign doctor to patient
- `DELETE /api/mappings/{id}/` - Remove doctor from patient
- `GET /api/mappings/patient/{patient_id}/` - Get doctors for specific patient
- `POST /api/mappings/bulk_assign/` - Assign multiple doctors to patient

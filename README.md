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

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- pip (Python package manager)

### Installation

1. **Clone the repository**
   \`\`\`bash
   git clone <repository-url>
   cd django-healthcare-backend
   \`\`\`

2. **Create virtual environment**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Setup environment variables**
   \`\`\`bash
   cp .env.example .env
   # Edit .env file with your database credentials
   \`\`\`

5. **Setup PostgreSQL database**
   \`\`\`sql
   CREATE DATABASE healthcare_db;
   \`\`\`

6. **Run migrations**
   \`\`\`bash
   python manage.py makemigrations
   python manage.py migrate
   \`\`\`

7. **Create superuser (optional)**
   \`\`\`bash
   python manage.py createsuperuser
   \`\`\`

8. **Load sample data (optional)**
   \`\`\`bash
   # Run the SQL scripts in the scripts folder
   \`\`\`

9. **Start the server**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

The API will be available at `http://localhost:8000/api/`

## Environment Variables

Create a `.env` file with the following variables:

\`\`\`env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your-password-here
DB_HOST=localhost
DB_PORT=5432
\`\`\`

## API Usage Examples

### Register a new user
\`\`\`bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123"
  }'
\`\`\`

### Login
\`\`\`bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "securepassword123"
  }'
\`\`\`

### Create a patient (requires authentication)
\`\`\`bash
curl -X POST http://localhost:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "phone": "+1234567890",
    "date_of_birth": "1990-01-01",
    "gender": "F",
    "address": "123 Main St, City, State",
    "emergency_contact": "John Smith",
    "emergency_phone": "+1234567891"
  }'
\`\`\`

### Assign doctor to patient
\`\`\`bash
curl -X POST http://localhost:8000/api/mappings/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "patient": 1,
    "doctor": 1,
    "notes": "Primary care physician",
    "is_primary": true
  }'
\`\`\`

## Project Structure

\`\`\`
healthcare_backend/
├── healthcare_backend/     # Main project settings
├── authentication/         # User authentication app
├── patients/              # Patient management app
├── doctors/               # Doctor management app
├── mappings/              # Patient-doctor mapping app
├── scripts/               # Database setup scripts
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
\`\`\`

## Security Features

- JWT-based authentication
- User-specific data access (patients belong to users)
- Password validation
- Input validation and sanitization
- Proper error handling
- CORS configuration

## Testing

You can test the API endpoints using:
- **Postman**: Import the API endpoints and test with proper authentication
- **curl**: Use the command-line examples provided above
- **Django Admin**: Access at `http://localhost:8000/admin/` to manage data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

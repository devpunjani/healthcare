-- Insert sample doctors data
-- Note: Run this after Django migrations are complete

INSERT INTO doctors_doctor (
    name, email, phone, specialization, license_number, 
    years_of_experience, hospital_affiliation, consultation_fee, 
    availability_hours, bio, is_active, created_at, updated_at
) VALUES 
(
    'John Smith', 'dr.johnsmith@hospital.com', '+1234567890', 
    'CARDIOLOGY', 'LIC001', 15, 'City General Hospital', 
    150.00, 'Mon-Fri 9AM-5PM', 
    'Experienced cardiologist with expertise in heart surgery.', 
    true, NOW(), NOW()
),
(
    'Sarah Johnson', 'dr.sarahjohnson@hospital.com', '+1234567891', 
    'PEDIATRICS', 'LIC002', 12, 'Children''s Medical Center', 
    120.00, 'Mon-Sat 8AM-6PM', 
    'Pediatric specialist focusing on child healthcare.', 
    true, NOW(), NOW()
),
(
    'Michael Brown', 'dr.michaelbrown@hospital.com', '+1234567892', 
    'ORTHOPEDICS', 'LIC003', 20, 'Orthopedic Specialty Clinic', 
    180.00, 'Tue-Thu 10AM-4PM', 
    'Orthopedic surgeon specializing in joint replacements.', 
    true, NOW(), NOW()
),
(
    'Emily Davis', 'dr.emilydavis@hospital.com', '+1234567893', 
    'DERMATOLOGY', 'LIC004', 8, 'Skin Care Institute', 
    100.00, 'Mon-Fri 9AM-3PM', 
    'Dermatologist with focus on cosmetic and medical dermatology.', 
    true, NOW(), NOW()
),
(
    'Robert Wilson', 'dr.robertwilson@hospital.com', '+1234567894', 
    'GENERAL_PRACTICE', 'LIC005', 25, 'Community Health Center', 
    80.00, 'Mon-Fri 7AM-7PM', 
    'Family medicine practitioner serving the community for over 25 years.', 
    true, NOW(), NOW()
);

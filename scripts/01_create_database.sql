-- Create the healthcare database
CREATE DATABASE healthcare_db;

-- Create a user for the application (optional)
-- CREATE USER healthcare_user WITH PASSWORD 'your_password_here';
-- GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO healthcare_user;

-- Connect to the database
\c healthcare_db;

-- Verify connection
SELECT current_database();

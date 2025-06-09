
"""
Setup script for Django Healthcare Backend
This script helps set up the project environment
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("🏥 Django Healthcare Backend Setup")
    print("=" * 40)
    
    # Check if virtual environment exists
    if not os.path.exists('venv') and not os.path.exists('.venv'):
        print("\n📦 Creating virtual environment...")
        if not run_command("python -m venv venv", "Virtual environment creation"):
            return
    
    # Activate virtual environment and install requirements
    if sys.platform.startswith('win'):
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    # Install requirements
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing Python packages"):
        return
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("\n📝 Creating .env file from template...")
        if os.path.exists('.env.example'):
            run_command("cp .env.example .env", "Copying environment template")
            print("⚠️  Please update the .env file with your database credentials")
        else:
            print("❌ .env.example file not found")
    
    # Django setup commands
    django_commands = [
        ("python manage.py makemigrations", "Creating Django migrations"),
        ("python manage.py migrate", "Running Django migrations"),
        ("python manage.py collectstatic --noinput", "Collecting static files"),
    ]
    
    for command, description in django_commands:
        if not run_command(command, description):
            print(f"⚠️  {description} failed, but continuing...")
    
    # Create superuser prompt
    print("\n👤 Would you like to create a superuser? (y/n): ", end="")
    if input().lower().startswith('y'):
        run_command("python manage.py createsuperuser", "Creating superuser")
    
    print("\n🎉 Setup completed!")
    print("\nNext steps:")
    print("1. Update your .env file with correct database credentials")
    print("2. Ensure PostgreSQL is running")
    print("3. Run: python manage.py runserver")
    print("4. Access the API at: http://localhost:8000/api/")
    print("5. Access Django Admin at: http://localhost:8000/admin/")

if __name__ == "__main__":
    main()

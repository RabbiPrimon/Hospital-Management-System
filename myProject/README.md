# Hospital Management System

A comprehensive Django-based web application for managing hospital operations, including departments, doctors, patients, and appointments.

## Table of Contents

- [Features](#features)
- [Models](#models)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Custom user model with Doctor and Patient roles
- **CRUD Operations**: Full Create, Read, Update, Delete functionality for all models
- **Relationship Management**:
  - Departments can have multiple doctors
  - Doctors can have multiple patients
  - Patients can book multiple appointments with doctors
- **Cascading Deletes**: Deleting a doctor automatically removes associated patients and appointments
- **Doctor Profiles**: View doctor's department, patients, and upcoming appointments
- **Responsive UI**: Clean, user-friendly interface with navigation
- **Email Notifications**: Signup confirmation emails

## Models

### Department
- `name` (CharField): Name of the department
- `location` (CharField): Location of the department

### Doctor
- `name` (CharField): Doctor's name
- `specialization` (CharField with choices): Doctor's specialization (Cardiology, Neurology, etc.)
- `phone` (CharField): Contact phone number
- `email` (EmailField): Email address
- `department` (ForeignKey): Associated department

### Patient
- `name` (CharField): Patient's name
- `age` (IntegerField): Patient's age
- `gender` (CharField with choices): Male, Female, or Other
- `phone` (CharField): Contact phone number
- `address` (TextField): Patient's address
- `doctor` (ForeignKey): Assigned doctor

### Appointment
- `patient` (ForeignKey): Associated patient
- `doctor` (ForeignKey): Associated doctor
- `appointment_date` (DateTimeField): Date and time of appointment
- `status` (CharField with choices): Pending, Completed, or Cancelled

### CustomUser
- `username` (CharField): Unique username
- `User_Type` (CharField with choices): Doctor or Patient
- Standard Django user fields (email, password, etc.)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd myProject
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. **Configure email settings** (in `myProject/settings.py`):
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-app-password'
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

### User Registration and Login
1. Visit the signup page to create an account as a Doctor or Patient
2. Login with your credentials
3. Access the dashboard and navigate through different sections

### Managing Departments
- View all departments
- Add new departments
- Edit existing departments
- Delete departments

### Managing Doctors
- View all doctors
- Add new doctors with specialization and department assignment
- Edit doctor information
- Delete doctors (cascades to patients and appointments)
- View doctors under a specific department

### Managing Patients
- View all patients
- Add new patients with doctor assignment
- Edit patient information
- Delete patients
- View patients of a specific doctor

### Managing Appointments
- View all appointments
- Book new appointments for patients with doctors
- Edit appointment details
- Delete appointments
- View appointments of a specific patient

### Doctor Profile
- View doctor's department
- See all patients assigned to the doctor
- Check upcoming appointments

## API Endpoints

The application uses Django views for handling requests. Key URLs include:

- `/` - Home page
- `/doctorPage/` - Doctor management
- `/patientPage/` - Patient management
- `/appointmentPage/` - Appointment management
- `/departmentPage/` - Department management
- `/loginPage/` - User login
- `/signupPage/` - User registration
- `/logoutPage/` - User logout

## Screenshots

### Home Dashboard
![Home Page](screenshots/home.png)

### Doctor Management
![Doctor Page](screenshots/doctor.png)

### Patient Management
![Patient Page](screenshots/patient.png)

### Appointment Booking
![Appointment Page](screenshots/appointment.png)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Technologies Used

- **Backend**: Django 4.x
- **Database**: SQLite (default), can be configured for PostgreSQL/MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Email**: SMTP (Gmail)
- **Media Handling**: Django's file upload system

## Future Enhancements

- Add role-based permissions
- Implement appointment reminders
- Add patient medical history tracking
- Integrate with payment gateways for billing
- Add REST API for mobile app integration
- Implement real-time notifications

## Support

For support, email support@hospitalmanagement.com or create an issue in the repository.

---

**Note**: This is a development version. For production deployment, ensure proper security configurations, database setup, and server configurations.

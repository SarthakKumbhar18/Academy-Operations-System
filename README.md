# Academy Operations System

## Overview
Academy Operations System is a web application built using Python and Django that helps manage subjects, student attendance, and subject-related details. It includes authentication for teachers and students, ensuring secure access to relevant functionalities.

## Features
- **User Authentication:** 
  - Secure login and logout for teachers and students.
  - Role-based access control.
- **Teacher Features:**
  - Add and manage subjects.
  - Take student attendance.
- **Student Features:**
  - View personal attendance records.
  - Access student profile details.
- **Subject Management:**
  - View subject details such as duration, topics covered, syllabus, and fees.

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:**  MySQL
- **Authentication:** Django Authentication System

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/academy-operations-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd academy-operations-system
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run database migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Admin/Teacher can log in, add subjects, and manage student attendance.
- Students can log in to view their attendance records and subject details.
- Public users can explore subject-related details.

## Future Enhancements
- Implement reports and analytics for attendance tracking.
- Add notifications for students about attendance updates.
- Improve UI with a responsive design.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.



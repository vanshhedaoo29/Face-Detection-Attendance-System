# 🧠 Face Detection Attendance System

A web-based attendance management system that uses **real-time face detection** to automatically mark attendance. Built using **Django**, **OpenCV**, **MediaPipe**, and **PostgreSQL**, this project features secure login, role-based access, and a responsive UI for viewing attendance records by **date** and **lecture**.

---

## 📌 Features

- 👤 **Role-Based Login**
  - **Student**: View personal attendance records
  - **Teacher/Admin**: Manage lectures and attendance
- 🎥 **Real-Time Face Detection** with MediaPipe + OpenCV
- 📅 **Lecture-based Attendance Tracking** with timestamps
- 📊 **Responsive Dashboard UI** using HTML, CSS, and JS
- 🔐 **Secure Authentication** using Django's built-in auth system
- 💾 **PostgreSQL Database** for scalable data storage

---

## 🚀 Tech Stack

| Layer         | Technology              |
|---------------|--------------------------|
| Frontend      | HTML, CSS, JavaScript    |
| Backend       | Django (Python)          |
| Face Detection| OpenCV + MediaPipe       |
| Database      | PostgreSQL               |
| Authentication| Django Auth System       |

---


## 📁 Project Structure

```py
face_attendance/
├── attendance/
│ ├── face_detect.py # Face detection logic
│ ├── templates/
│ │ └── attendance/
│ │ └── student_view.html
│ ├── static/ # Static files (CSS/JS)
│ ├── models.py # Models: User, Lecture, Attendance
│ ├── views.py # View logic
│ ├── urls.py # App-level routes
├── face_attendance/
│ ├── settings.py # Django settings
│ ├── urls.py # Project-level routes
├── manage.py # Django CLI
```


---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/vanshhedaoo29/Face-Detection-Attendance-System
cd face-attendance-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  
# Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install django opencv-python mediapipe psycopg2-binary
```

### 4. Set Up PostgreSQL

Create a database and update settings.py:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'attendance_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations and Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## 💻 Running the Project

### 1. Start Django Server

```bash
python manage.py runserver
```
Visit: http://localhost:8000

### 2. Start Face Detection (for Teachers/Admin)

```bash
python attendance/face_detect.py
```

This script will:
- Access your webcam

- Detect faces using MediaPipe

- Trigger attendance marking logic



### 🔐 Roles & Permissions

| Role         | Access              |
|---------------|--------------------------|
| Admin      | Full access to Django admin panel and face detection |
| Teacher       | Manage lectures and mark attendance          |
| Student| View their own attendance report       |

---


### 📸 Face Detection Overview

- Uses MediaPipe for fast face detection
- Uses OpenCV for webcam feed capture
- Logic can be extended to support face recognition

### 🖼️ Screenshots


✅ Login Page

📅 Attendance Dashboard

🎥 Face Detection in Action

📊 Responsive Attendance Table

### 📊 Optional Features To Add
 - Add face recognition support
 - Deploy to Render, Heroku, or Railway
 - Use Chart.js to visualize attendance reports
 - Add email alerts for absent students
 - Export attendance as CSV/PDF

### 📄 License
This project is licensed under the MIT License.

### 👨‍💻 Author
|         |             |                  |
|---------------|-------------|------------|
| Author      | Vansh Hedaoo | Vedant Rajurkar |
| Email       |vanshhedaooprpote@gmail.com|  rajurkarvedant8@gmail.com   |
| LinkedIn|        |              |
| Portfolio|        |                 |
---


### 🙌 Acknowledgments
  Django Documentation

MediaPipe by Google

OpenCV Docs
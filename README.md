# 🛡️ Django JWT Auth API with PostgreSQL & Cloudinary

A secure user authentication system built with **Django**, **PostgreSQL**, **JWT tokens**, and **Cloudinary** for profile photo storage.

## 📌 Features
✅ User Registration with profile photo upload  
✅ Email-based OTP Verification  
✅ JWT Token-based Login and Logout  
✅ Forgot Password with OTP  
✅ Token Refresh Endpoint  
✅ Profile retrieval (secured endpoint)  
✅ Image storage via [Cloudinary](https://cloudinary.com/)  
✅ PostgreSQL Database integration  

---

## 📁 Project Structure
```bash
DjangoAPI/
├── authapp/ # Main app for authentication
│ ├── migrations/
│ ├── models.py # Custom User model
│ ├── serializers.py # DRF serializers
│ ├── views.py # API views
│ ├── urls.py # Auth routes
├── DjangoAPI/
│ ├── settings.py # Settings including JWT & DB config
│ ├── urls.py # Project routes
├── manage.py
└── requirements.txt
```
---

## 🔧 Tech Stack

- Django 5+
- Django REST Framework
- PostgreSQL
- Cloudinary for media storage
- JWT Authentication (`simplejwt`)
- Email support for OTP (via SMTP)
- Token Blacklisting for logout

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/your-username/django-auth-api.git
cd django-auth-api
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

### 4️⃣ PostgreSQL Setup
Create a PostgreSQL DB and update DATABASES in settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Cloudinary Setup
Register on cloudinary.com and add the following to settings.py:
```bash
CLOUDINARY = {
  'cloud_name': 'your_cloud_name',
  'api_key': 'your_api_key',
  'api_secret': 'your_api_secret'
}
```

### 6️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ Run the Server
```bash
python manage.py runserver
```

### 🧑‍💻 Author
**Vivek Kumar**

💻 Mobile App Developer & Tech Enthusiast

🏆 1st Runner Up, Rajasthan IT Day Hackathon (March 2023)

🌐 vivekajee.in

📧 vnjvibhash@gmail.com



# 🌟 Starstream — Django OTT Streaming Platform

## 🎬 Overview
**Starstream** is a full-featured **OTT (Over-The-Top) streaming platform** built using **Django**.  
It allows users to browse, search, and stream movies, as well as manage a personalized watchlist.  
Inspired by platforms like **Netflix**, it includes both **web UI and REST APIs**.

---

## ⚙️ Tech Stack
| Category | Technologies Used |
|-----------|-------------------|
| **Backend** | Django 5.2.8, Django REST Framework |
| **Frontend** | HTML, Tailwind CSS, JavaScript (AJAX + jQuery) |
| **Database** | SQLite3 (default, can switch to PostgreSQL) |
| **Authentication** | Django’s built-in session-based auth |
| **API Testing** | DRF Browsable API, Postman |

---

## 📁 Project Structure
```
starstream/
│
├── core/
│   ├── models.py          # Movie and MovieList models
│   ├── views.py           # Web and API views
│   ├── serializers.py     # DRF serializers for Movies and Users
│   ├── urls.py            # App-level routes
│   ├── templates/         # HTML templates (index, login, signup, etc.)
│   └── static/            # CSS, images
│
├── starstream/
│   ├── settings.py        # Project configuration
│   ├── urls.py            # Root URL routing
│
├── media/                 # Uploaded movie images/videos
├── requirements.txt       # Dependencies
└── manage.py
```

---

## 🧩 Features

### 👤 User Authentication
- Secure **Signup**, **Login**, and **Logout**
- Session-based authentication
- API support for user management

### 🎥 Movie Management
- Each movie includes:
  - Title, Description, Genre, Release Date, and Length  
  - Card & Cover Images  
  - Video File for playback
- Dynamic homepage movie listing

### 🔎 Search and Genres
- Search movies by title
- Filter movies by genre (Action, Comedy, Drama, etc.)

### ❤️ My List (Watchlist)
- Add/remove movies to personal list using AJAX
- Stored per user in database
- Real-time UI update on addition

### 🔗 REST API Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/api/movies/` | GET | Retrieve all movies |
| `/api/genres/<genre>/` | GET | Filter by genre |
| `/api/search/?q=<term>` | GET | Search movies |
| `/api/signup/` | POST | Register a new user |
| `/api/login/` | POST | Authenticate user |
| `/api/my-list/` | GET | Get user’s saved movies |
| `/api/add-to-list/` | POST | Add movie to list |

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Shinxhan/starstream.git
cd starstream
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
# Activate
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Linux/Mac
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create a Superuser (optional)
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server
```bash
python manage.py runserver
```
---

## 🧠 Key Learnings
- Django authentication and session management  
- REST API creation using Django REST Framework  
- File uploads (images/videos)  
- AJAX integration with Django views  
- Template rendering and context usage  
- Combining backend logic with responsive frontend design  

---

## 🔮 Future Enhancements
- JWT authentication for API access  
- Subscription and payment integration  
- ML-based movie recommendations  
- Video streaming optimization  
- Watch history and progress saving  
- Dark/light theme toggle  

---

## 👨‍💻 Author
**Karan Joshi**   
---

## 📜 License
This project is licensed under the **MIT License** — feel free to use and modify it for educational purposes.

---

### ⭐ Don’t forget to star the repo if you like it!

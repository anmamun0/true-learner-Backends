# TrueLearner 🎓

**TrueLearner** is an advanced online learning platform where instructors can create courses and students can enroll to enhance their skills.

---

## 🚀 Live Links

🔹 **Backend Live:** [TrueLearner Backend](https://truelearner-backends.onrender.com/)  
🔹 **Backend GitHub:** [Backend Repository](https://github.com/anmamun0/true-learner-Backends)  
🔹 **Frontend Live:** [TrueLearner Frontend](https://truelearner.vercel.app/)  
🔹 **Frontend GitHub:** [Frontend Repository](https://github.com/anmamun0/true-learner-Frontend)  
🔹 **Admin Panel Credentials:**  
&nbsp;&nbsp;&nbsp;&nbsp;🟢 **Username:** `admin`  
&nbsp;&nbsp;&nbsp;&nbsp;🟢 **Password:** `123`  

---

## 📌 API Endpoints

### 🔹 **User Management**

| Action             | Method | Endpoint                                   | 
|--------------------|--------|--------------------------------------------| 
| **Register**       | `POST` | `/user/register/`                         | 
| **Login**         | `POST` | `/user/login/`                            |
| **Logout**        | `POST` | `/user/logout/`                           |  
| **Student List**  | `GET`  | `/user/students/`                         |    
| **Update Student** | `PUT`  | `/user/students/<user_id>/update/`        |      
| **Instructor List** | `GET` | `/user/instructors/`                      |  
| **Update Instructor** | `PUT` | `/user/instructors/<user_id>/update/` |  
    

### 🔹 **Course Management**

| Action                 | Method | Endpoint                                      |
|------------------------|--------|-----------------------------------------------|
| **All Courses**        | `GET`  | `/course/courses/`                           |
| **Create Course**      | `POST` | `/course/courses/create/`                    | 
| **Update Course**      | `PUT`  | `/course/courses/<course_id>/update/`        |
| **Filter by Category** | `GET`  | `/course/courses/?category=<category_slug>` |
| **Enrolled Students**  | `GET`  | `/course/paid_student/`                      |

### 🔹 **Video Management**

| Action            | Method | Endpoint                                  |
|------------------|--------|------------------------------------------|
| **All Videos**   | `GET`  | `/course/videos/`                        |
| **Create Video** | `POST` | `/course/videos/<course_id>/create/`     |
| **Update Video** | `PUT`  | `/course/videos/<video_id>/update/`      |
| **Delete Video** | `DELETE` | `/course/videos/<video_id>/delete/` |

### 🔹 **Category Management**

| Action            | Method | Endpoint          |
|------------------|--------|------------------|
| **All Categories** | `GET`  | `/course/category/` |



## 📄 API Fields

| API | Fields |
|---------|--------------------------------------------------------------------------------|
| **Register** | `role`, `username`, `email`, `first_name`, `last_name`, `password` |
| **Login** | `role`, `email`, `password` |
| **Logout** | `token` |
| **Create Course** | `token`, `title`,` thumble`, `category`, `description`, `price`, `total_lecture`, `total_session`, `total_length`, videos[{`title`, `url`, `durations`}] |
| **Update Student Profile** | `username`, `first_name`, `last_name`, `email`, `phone`, `address`, `bio` |




---

## 📄 API Examples

### 🔹 **User Login**
```json
{
  "role": "Instructor",
  "email": "anmamun0@gmail.com",
  "password": "12345mamun"
}
```

### 🔹 **Create Course**
```json
{
  "title": "Python for Beginners",
  "thumble": "https://example.com/images/python-course.jpg",
  "category": [1, 2], 
  "description": "Learn Python from scratch with hands-on projects.",
  "price": 19.99,
  "total_lecture": 25,
  "total_session": 10,
  "total_length": 720,
  "videos": [
    {
      "title": "Introduction to Python",
      "url": "https://example.com/videos/intro-python.mp4",
      "duration": 600
    },
    {
      "title": "Variables and Data Types",
      "url": "https://example.com/videos/variables.mp4",
      "duration": 900
    }
  ]
}
```



---

## 📌 Features
✔️ User Authentication (Instructor & Student)  
✔️ Course Management with Categories  
✔️ Video Management for Lessons  
✔️ Secure API Endpoints  
✔️ Responsive UI for an Engaging Learning Experience  
✔️ Admin Panel for Easy Management  

---

## 🛠 Tech Stack

🔹 **Backend:** Django, Django REST Framework (DRF), PostgreSQL  
🔹 **Frontend:** React, Tailwind CSS, Vercel  
🔹 **Hosting:** Render (Backend), Vercel (Frontend)  

---

## 💡 Contributing

We welcome contributions! To contribute:
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit changes and push to your branch
4. Submit a Pull Request

---

## 📬 Contact
📧 **Email:** [anmamun0@gmail.com](mailto:anmamun0@gmail.com)  
🔗 **GitHub:** [anmamun0](https://github.com/anmamun0)  
🔗 **LinkedIn:** [Mamun's LinkedIn](https://www.linkedin.com/in/anmamun0/)  

---

🚀 _Happy Learning with TrueLearner!_ 🎉
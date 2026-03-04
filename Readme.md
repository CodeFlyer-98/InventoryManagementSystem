# 🗂 Inventory Management System

A Full-Stack Inventory Management System built using FastAPI, PostgreSQL, and React, deployed on Render.
This project demonstrates backend API development, database integration, frontend integration, and full cloud deployment.

🚀 Live Application

Frontend:
https://inventorymanagementsystem-fcc5.onrender.com

Backend API:
https://inventorymanagementsystem-2-k2p4.onrender.com

API Documentation (Swagger UI):
https://inventorymanagementsystem-2-k2p4.onrender.com/docs

---

 🏗 Tech Stack

Backend
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Uvicorn / Gunicorn

 Frontend
- React
- Axios
- HTML / CSS

Deployment
- Render Web Service (Backend)
- Render Static Site (Frontend)
- Render PostgreSQL Database

---

📦 Features

- Add new products
- View all products
- Update product details
- Delete products
- RESTful API structure
- PostgreSQL database integration
- Environment variable configuration
- Health check endpoint for deployment monitoring

---

📂 Project Structure

```
InventoryManagementSystem/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── frontend/
    ├── package.json
    ├── public/
    └── src/
⚙️ Environment Variables

The backend uses environment variables for secure database configuration.

Example:

DATABASE_URL=postgresql://postgres:1234@localhost:5432/telusko


In production, this is configured inside the Render dashboard.
🛠 Local Development Setup

1️⃣ Clone Repository
git clone https://github.com/CodeFlyer-98/InventoryManagementSystem.git
cd InventoryManagementSystem

2️⃣ Backend Setup

Create virtual environment:
python -m venv venv

Activate environment:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt

Run backend server:
uvicorn main:app --reload
```

Backend runs at:
```
http://localhost:8000

API Docs:

http://localhost:8000/docs

3️⃣ Frontend Setup

Navigate to frontend folder:

cd frontend

Install dependencies:
npm install

Run development server:

npm start

Frontend runs at:

http://localhost:3000

🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET    | /health  | Health check endpoint |
| GET    | /products | Get all products |
| POST   | /products | Add a new product |
| PUT    | /products/{id} | Update product |
| DELETE | /products/{id} | Delete product |


 🧠 Deployment Architecture

1. PostgreSQL database created on Render
2. Backend deployed as Render Web Service
3. DATABASE_URL configured as environment variable
4. Frontend deployed as Render Static Site
5. Frontend API base URL updated to backend production URL

🛡 Why Environment Variables Are Used

The database URL is not hardcoded for security and flexibility.
Instead of:

postgresql://localhost:5432/dbname
We use:
os.getenv("DATABASE_URL")

This allows:
- Secure credential management
- Different configuration for local & production
- Cloud deployment compatibility

 🐞 Issues Faced & Solutions

 1️⃣ PostgreSQL localhost connection error
Error:
connection to server at "localhost", port 5432 failed
Reason:
Production environment does not have a local database.
Solution:
Used Render PostgreSQL and configured DATABASE_URL.

---

 2️⃣ react-scripts permission denied
Reason:
node_modules was committed from Windows system.
Linux deployment environment could not execute those files.
Solution:
Removed node_modules from Git and allowed Render to install dependencies.

📚 What This Project Demonstrates

- REST API development with FastAPI
- Database modeling using SQLAlchemy
- PostgreSQL cloud integration
- Full-stack integration (React + FastAPI)
- Environment variable handling
- CI/CD deployment workflow
- Debugging Linux deployment issues
- Professional Git practices


🚀 Future Improvements

- User Authentication (JWT)
- Role-Based Access Control
- Search and Filtering
- Pagination
- Docker containerization
- Automated CI/CD pipeline


## 👨‍💻 Author

Jash Kothari
GitHub: https://github.com/CodeFlyer-98

---

## 📄 License

This project is for educational and portfolio purposes.
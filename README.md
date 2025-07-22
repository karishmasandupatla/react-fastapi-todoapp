# React + FastAPI Todo App

This is a full-stack todo application built with:

- 🌐 **Frontend:** React.js  
- ⚙️ **Backend:** FastAPI (Python)

## Features

- Add, update, delete tasks
- Mark tasks as completed
- Persistent storage with backend API

## Setup Instructions

### Backend + Frontend (Combined Start)

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```

2. Start the FastAPI backend server:
   ```bash
   uvicorn main:app --reload
   ```

3. Open a **new terminal**, then navigate to the frontend folder:
   ```bash
   cd frontend
   npm install   # Only the first time to install dependencies
   npm start
   ```

> ✅ The backend will run on: `http://127.0.0.1:8000`  
> ✅ The frontend will run on: `http://localhost:3000`

---

### API Endpoints

- `GET /tasks` - Fetch all tasks
- `POST /tasks` - Add a new task
- `PUT /tasks/{id}` - Update an existing task
- `DELETE /tasks/{id}` - Delete a task

---

### Folder Structure

```
root/
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── public/
│   └── src/
│       └── App.js
│
└── README.md
```

---

### Author

- ✨ Created by [Karishma Sandupatla]

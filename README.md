# Agent Tracker

Agent Tracker is a Django-based web application designed to manage and track delivery agents and their assignments. This project includes features for tracking deliveries, managing schedules, and monitoring the performance of agents.

## 🚀 Features

- Manage delivery agents and their assignments.  
- Track the status of deliveries in real-time.  
- Administrative tools for overseeing delivery operations.  
- User-friendly interfaces with Django templates.  
- Simple SQLite database for storage.

## 🛠️ Installation and Setup

To set up and run this project locally, follow these steps:

### Prerequisites

Ensure you have Python 3.8+, Pip, and a virtual environment (optional).

### Installation

1. Clone the repository and navigate to the project directory:  
   `git clone https://github.com/drhinofficial/agent_tracker.git && cd agent_tracker`

2. (Optional) Set up a virtual environment:  
   `python -m venv venv && source venv/bin/activate` (Linux/Mac)  
   `python -m venv venv && venv\Scripts\activate` (Windows)

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Apply database migrations:  
   `python manage.py migrate`

5. (Optional) Create a superuser:  
   `python manage.py createsuperuser`

6. Run the development server:  
   `python manage.py runserver`

7. Access the application in your browser at `http://127.0.0.1:8000/`.


ADMIN CREDS: lokam, lokam
AGENT CREDS 1: modi, password123
AGENT CREDS 2: amitabh, password123

### Admin Dashboard:
![Screenshot 2025-01-22 120224](https://github.com/user-attachments/assets/e05ac3ef-5426-419d-983f-951d1c3d2f92)

### Agent Dashboard
![Screenshot 2025-01-22 120245](https://github.com/user-attachments/assets/96f0ea52-6c46-433c-ad03-0503674d44a7)

### Create Order
![Screenshot 2025-01-22 120251](https://github.com/user-attachments/assets/be628c8a-a635-401e-bfa7-c34217d9a0c3)



## Description
1. We can create the orders and based on that order creation, whoever agent we select the job will go to him, he can update only payment mode and delivered at


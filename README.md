# Hotel Management System - OOP Project

## 1. Overview

This project is a comprehensive hotel management system developed as an Object-Oriented Programming Project at KMITL. The system provides functionality for both guests and staff members to manage hotel operations through a web interface using `fasthtml` framework.

## 2. Team Members

All members contributed equally to the development:

- Phudith Janjaeng
- Siwakorn Titragool
- Bannasorn Lalod
- Korn Klinthong

## 3. Key Features

### User Management
- Guest and Staff user types with authentication
- Role-based access control

### Room Management
- Room search and filtering
- Availability checking
- Booking management

### Hotel Services
- Transport service and reservation
- Food ordering system
- Laundry service
- Cleaning service scheduling
- Repair service requests

## 4. Technologies Used
- Programming Language: Python
- Web Framework: FastHTML library
- Design Pattern: Object-Oriented Programming

## 5. Setup & Installation

### Prerequisites
- Python 3.12.9 or higher
- pip package manager

### Installation Steps

1. Clone the repository:
```sh
git clone https://github.com/KindleDrift/OOP-Website-Project.git
cd OOP-Website-Project
```

2. Create and activate a virtual environment:
```sh
# On Windows
python -m venv venv
venv\Scripts\activate

# or alternatively On Windows using setup file (also skip step 3)
setup_project.bat
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```sh
pip install -r requirements.txt
```

4. Run the application:
```sh
cd src
python main.py
```

5. Access the application:
Open your browser and navigate to `http://localhost:5001`

## 6. Project Structure

```
/OOP-Website-Project
│── /src
│   ├── main.py
│   ├── /classes
│   │   ├── hotel.py
│   └── /images
│── /docs
│── requirements.txt
└── README.md
```
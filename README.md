# Teacher and Group Management System

This is a Django-based system for managing teachers and groups.

## Endpoints

### POST /teacher/
This endpoint accepts a POST request, validates it, and saves the teacher's information into the database if the request is valid. It utilizes Django Forms. After saving, it redirects to `/teachers/`.

### GET /teacher/
This endpoint accepts a GET request and displays a form for saving a new teacher. It utilizes Django Forms.

### GET /teachers/
This endpoint accepts a GET request and displays a list of teachers stored in the database.

### POST /group/
This endpoint accepts a POST request, validates it, and saves the group information into the database if the request is valid. It utilizes Django Forms. After saving, it redirects to `/groups/`.

### GET /group/
This endpoint accepts a GET request and displays a form for saving a new group. It utilizes Django Forms.

### GET /groups/
This endpoint accepts a GET request and displays a list of groups stored in the database.

## Models

### Teacher
- Full Name (Name, Surname)
- Date of Birth
- Subjects (Optional)

### Group
- Name

## Usage

1. Clone the repository:
```bash
git clone <repository_url>
cd <project_directory>

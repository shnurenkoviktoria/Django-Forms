# Teacher and Group Management System

This is a Django-based system for managing teachers and groups.

## Endpoints
### /teacher/
- **HTTP method:** POST
- **URL:** /teacher/
- **Description:** Accepts a POST request, validates it, and saves it to the teachers table if the request is valid. Utilizes Django Forms. After saving, it redirects to /teachers/.

### /teacher/
- **HTTP method:** GET
- **URL:** /teacher/
- **Description:** Accepts a GET request and displays a form for saving a new teacher. Utilizes Django Forms.

### /teachers/
- **HTTP method:** GET
- **URL:** /teachers/
- **Description:** Accepts a GET request and displays a list of teachers in the database.

### /group/
- **HTTP method:** POST
- **URL:** /group/
- **Description:** Accepts a POST request, validates it, and saves it to the groups table if the request is valid. Utilizes Django Forms. After saving, it redirects to /groups/.

### /group/
- **HTTP method:** GET
- **URL:** /group/
- **Description:** Accepts a GET request and displays a form for saving a new group. Utilizes Django Forms.

### /groups/
- **HTTP method:** GET
- **URL:** /groups/
- **Description:** Accepts a GET request and displays a list of groups in the database.

## Models

### Teacher
- **Fields:** Full name (PIB), date of birth, subjects (optional).

### Group
- **Fields:** Name.

### Student
- **Fields:** Full name (PIB), date of birth, phone.

## Validation

- Added validation for phone number when saving a student. Invalid phone numbers are not allowed to be saved.

## Middleware

- Created LogMiddleware that saves request.path, request.method, and execution_time to a text file. Additional storage in the database can be implemented.
  
## Usage

1. Clone the repository:
```bash
git clone <repository_url>
cd <project_directory>

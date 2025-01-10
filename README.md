# National ID Validation System

This project provides a system for validating Egyptian National ID numbers. It includes two versions:
1. **Database Version:** Validates and stores national IDs in a database.
2. **API View Version:** Validates national IDs without using a database.

The system also includes **request logging** using middleware to track all interactions with the `/validate-national-id/` endpoint.

---

## Features

- **National ID Validation:**  
  - Validates 14-digit Egyptian National IDs using a custom `NationalIDValidator` class.
  - Checks for valid birth date, governorate code, and check digit.

- **Database Integration (Optional):**  
  - Stores valid national IDs in a database for faster future validation.

- **Request Logging:**  
  - Logs all requests to the `/validate-national-id/` endpoint.
  - Logs to a database (for the database version) or a file (for the API view version).

- **Middleware Implementation:**  
  - Centralized logging logic using middleware for cleaner and reusable code.

---

## How to Use

### 1. Database Version
- Ensure the database is set up and migrations are applied.
- Send a POST request to api/v1/validate-national-id/   with the `number` in the request body.
- If the national ID is valid, it will be stored in the database.

### 2. API View Version
- Send a POST request to `api/v2/validate-national-id/` with the `national_id` in the request body.


---

## Example Request

### Request:
```json
{
    "number": "29512011248431",
    "birth_date": "1995-12-01",
    "status": "valid",
    "location": "الدقهلية"
}



## Installation

python -m venv env
. env\bin\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


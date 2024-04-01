# FastAPI Python API

This is a simple FastAPI Python API for managing student records.
# pytest
poetry run pytest

This is a simple FastAPI Python API for managing student records.
## To Run Project
 poetry run dev
1. 
    ```

2. Install dependencies:

    ```
    **fastapi**
    **uvicorn**
    ```

## Usage

1. Run the FastAPI server:

    ```main
    uvicorn main:app --reload
    ```

2. Access the API documentation:

    Open your web browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Endpoints

### Get All Students

- **URL:** `/students`
- **Method:** `GET`
- **Description:** Retrieve details of all students.
- **Response:** JSON array containing student records.

### Get Single Student

- **URL:** `/singlestudent/{studentid}`
- **Method:** `GET`
- **Description:** Retrieve details of a single student by ID.
- **Parameters:**
    - `studentid`: Student ID (integer)
- **Response:** JSON object containing student details, or a message indicating the student was not found.

### Add Student

- **URL:** `/addstudent`
- **Method:** `POST`
- **Description:** Add a new student record.
- **Request Body:** JSON object with the following fields:
    - `studentid`: Student ID (integer)
    - `Name`: Student's name (string)
    - `Age`: Student's age (integer)
    - `Class`: Student's class (string)
- **Response:** JSON array containing updated list of students.

### Update Student

- **URL:** `/updatestudent`
- **Method:** `PUT`
- **Description:** Update an existing student record.
- **Request Body:** JSON object with the following fields:
    - `studentid`: Student ID (integer)
    - `Name`: Updated name (string)
    - `Age`: Updated age (integer)
    - `Class`: Updated class (string)
- **Response:** Message confirming the update.

### Delete Student

- **URL:** `/deletestudent/{studentid}`
- **Method:** `DELETE`
- **Description:** Delete a student record by ID.
- **Parameters:**
    - `studentid`: Student ID (integer)
- **Response:** JSON array containing updated list of students, or a message indicating the student was not found.

## Author

Your Name

## License



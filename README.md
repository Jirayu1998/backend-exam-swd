# School Management System API Documentation

This API allows you to manage data related to schools, classrooms, teachers, and students.

## 1. Data Structure

### 1.1 School

Attributes for school data:
- **Name**: The name of the school.
- **Abbreviation**: Shortened name or acronym of the school.
- **Address**: The location of the school.

### 1.2 Classroom

Attributes for classroom data:
- **Grade**: The academic level or year.
- **Section**: The specific section or division.

### 1.3 Teacher

Attributes for teacher data:
- **First Name**: Teacher's given name.
- **Last Name**: Teacher's surname.
- **Gender**: Teacher's gender.

### 1.4 Student

Attributes for student data:
- **First Name**: Student's given name.
- **Last Name**: Student's surname.
- **Gender**: Student's gender.

## 2. API Endpoints

### 2.1 School API

- **GET** `/api/schools/`  
  Retrieves a list of all schools. Supports filtering by `name`.
  
- **GET** `/api/schools/<id>/`  
  Retrieves details of a specific school by its ID. The details include:
  - Total number of classrooms.
  - Total number of teachers.
  - Total number of students.
  
- **POST** `/api/schools/`  
  Creates a new school record.
  
- **PUT** `/api/schools/<id>/`  
  Updates the details of an existing school by its ID.
  
- **DELETE** `/api/schools/<id>/`  
  Deletes a school by its ID.

### 2.2 Classroom API

- **GET** `/api/classrooms/`  
  Retrieves a list of all classrooms. Supports filtering by `school`.
  
- **GET** `/api/classrooms/<id>/`  
  Retrieves details of a specific classroom by its ID. The details include:
  - List of teachers.
  - List of students.
  
- **POST** `/api/classrooms/`  
  Creates a new classroom record.
  
- **PUT** `/api/classrooms/<id>/`  
  Updates the details of an existing classroom by its ID.
  
- **DELETE** `/api/classrooms/<id>/`  
  Deletes a classroom by its ID.

### 2.3 Teacher API

- **GET** `/api/teachers/`  
  Retrieves a list of all teachers. Supports filtering by `school`, `classroom`, `first name`, `last name`, and `gender`.
  
- **GET** `/api/teachers/<id>/`  
  Retrieves details of a specific teacher by their ID. The details include:
  - List of classrooms they are assigned to.
  
- **POST** `/api/teachers/`  
  Creates a new teacher record.
  
- **PUT** `/api/teachers/<id>/`  
  Updates the details of an existing teacher by their ID.
  
- **DELETE** `/api/teachers/<id>/`  
  Deletes a teacher by their ID.

### 2.4 Student API

- **GET** `/api/students/`  
  Retrieves a list of all students. Supports filtering by `school`, `classroom`, `first name`, `last name`, and `gender`.
  
- **GET** `/api/students/<id>/`  
  Retrieves details of a specific student by their ID. The details include:
  - The classroom they are enrolled in.
  
- **POST** `/api/students/`  
  Creates a new student record.
  
- **PUT** `/api/students/<id>/`  
  Updates the details of an existing student by their ID.
  
- **DELETE** `/api/students/<id>/`  
  Deletes a student by their ID.

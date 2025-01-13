# Task Management System

A simple task management web application built using Django and Django REST Framework (DRF). This application allows users to create, update, delete, and manage tasks, with an optional due date and task status. It includes basic authentication for users and offers a simple UI built with Bootstrap.

## Features

- User authentication (login/logout)
- CRUD functionality for tasks:
  - **Create**: Users can create new tasks with a title, description, status, and due date.
  - **Read**: Users can view the list of tasks.
  - **Update**: Users can update the title, description, status, and due date of a task.
  - **Delete**: Users can delete tasks.
- Task statuses: "To Do", "In Progress", "Done"
- Due date for tasks
- Built using Django, Django REST Framework, and Bootstrap

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/pmfe22/task_management.git
    ```

2. Navigate to the project directory:

    ```bash
    cd task-management
    ```

3. Set up a virtual environment (recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply the database migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser for admin access (optional):

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Access the application at `http://127.0.0.1:8000/`.

## Usage

- **Login**: Log in with your credentials to access the task management features.
- **Create Tasks**: Use the "Create Task" form to add a new task with a title, description, status, and due date.
- **View Tasks**: View the list of tasks with their details and statuses.
- **Update Tasks**: Edit the title, description, status, and due date of existing tasks.
- **Delete Tasks**: Remove tasks from the list.

## API Endpoints (if using Django REST Framework)

- **GET /api/tasks/**: List all tasks.
- **POST /api/tasks/**: Create a new task.
- **GET /api/tasks/{id}/**: Get details of a specific task.
- **PUT /api/tasks/{id}/**: Update a specific task.
- **DELETE /api/tasks/{id}/**: Delete a specific task.


# Gas Utility Service Request Management System

A Django-based web application for managing customer service requests for a gas utility company. The system allows customers to submit, track, and view service requests while providing a dashboard for customer support representatives to manage and resolve requests efficiently.

---

## Features

### Customer Portal
- **Service Request Submission**: Customers can select the type of request, provide details, and optionally upload attachments.
- **Request Tracking**: Customers can view the status of their requests and track resolution progress.

### Customer Support Dashboard
- **View Requests**: Support staff can view all service requests categorized by status (`Pending` or `In Progress` or `Resolved`).
- **Resolve Requests**: A dedicated button to mark pending requests as resolved, automatically updating the database.
- **Request Filtering**: Requests are displayed in separate tables for `Pending` and `Resolved` statuses.

---

## Installation

### Prerequisites
- Python 3.x
- Django 4.x

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/amaankhan4/bynryGas
    cd gas-utility-system
    ```

2. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Create a superuser for admin access:
    ```bash
    python manage.py createsuperuser
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

5. Access the application:
    - Service Request: `http://127.0.0.1:8000/service/create`
    - Request Tracking: `http://127.0.0.1:8000/service/request_details/{request_id}`
    - Customer Support Portal: `http://127.0.0.1:8000/dashboard`

---

## Usage

### Submitting a Service Request
1. Fill in the service request form with necessary details.
2. Submit the form to receive a unique request ID for tracking.

### Tracking Requests
1. Note the Request Id generated when a request is submitted.
2. Go to Request Tracking url and input your Request Id in place of {request_id}.

### Resolving Requests (Admin/Support)
1. View all pending requests and click the "Resolve" button to mark them as resolved.

---



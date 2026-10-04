````markdown
# Django Blog Application

A simple Blog Application developed using Django as a minor project.

## Features

- User Signup
- User Login and Logout
- Create Blog Posts
- View All Blog Posts
- View Individual Blog Post
- Edit Own Blog Posts
- Delete Own Blog Posts
- My Posts section
- Django Admin Panel
- User authentication and authorization
- Bootstrap-based UI
- Custom CSS styling

## Technologies Used

- Python
- Django 5.2
- SQLite
- HTML
- CSS
- Bootstrap 5.3.3
- Django Templates
- Django ORM

## Project Structure

```text
Blog-application/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── blog/
    ├── migrations/
    ├── static/
    │   └── blog/
    │       └── styles.css
    ├── templates/
    │   └── blog/
    │       ├── base.html
    │       ├── home.html
    │       ├── my_posts.html
    │       ├── post_detail.html
    │       ├── post_form.html
    │       ├── post_confirm_delete.html
    │       ├── login.html
    │       └── signup.html
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    └── views.py
````

## Installation and Setup

### 1. Clone the repository

```bash
git clone 
cd Blog-application
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create the admin account.

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## Admin Panel

The Django admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created during setup.

## Main Pages

| Page        | URL                  | Description                                  |
| ----------- | -------------------- | -------------------------------------------- |
| Home        | `/`                  | Displays all blog posts                      |
| Signup      | `/signup/`           | Create a new account                         |
| Login       | `/login/`            | Login to the application                     |
| My Posts    | `/my-posts/`         | Displays posts created by the logged-in user |
| Create Post | `/post/new/`         | Create a new blog post                       |
| Post Detail | `/post/<id>/`        | View the complete post                       |
| Edit Post   | `/post/<id>/edit/`   | Edit your own post                           |
| Delete Post | `/post/<id>/delete/` | Delete your own post                         |
| Admin       | `/admin/`            | Django administration panel                  |

## Authentication and Authorization

Users can create accounts and log in to the application.

Authenticated users can create posts.

Users can edit and delete only their own posts. Posts created by other users can be viewed, but their Edit and Delete options are not available.

The `My Posts` section displays only the posts created by the currently logged-in user.

## Database

The project uses SQLite by default.

The main model is `Post`, which contains:

* Title
* Content
* Author
* Created date
* Updated date

The author is connected to Django's built-in `User` model using a `ForeignKey`.

## Django Concepts Used

This project demonstrates:

* Django Project and App structure
* MVT architecture
* URL routing
* Views
* Models
* Django ORM
* Migrations
* Django Admin
* ModelForms
* Template inheritance
* Template tags and filters
* User authentication
* Login and logout
* Authorization
* Static files
* Bootstrap
* CRUD operations

## Author

Kirtana Kichmbare

BTech Computer Engineering


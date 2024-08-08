# Blog Platform

Live Project Link : <b> https://blogappbysanskar.pythonanywhere.com/ulogin/ </b>
<br/>
The Blog Platform is a Django-based web application designed for users to create, manage, and interact with blog posts. It includes user authentication, blog post management, comment functionality, and a like system. This project demonstrates a full-featured blogging system with essential features and a clean, responsive design.

Features
1) User Authentication: Register, login, and logout using Django's built-in authentication system.

2) Blog Post Management:
   i) Create, update, and delete blog posts.
   ii) View a list of all blog posts and individual post details.
   
3) Comment System:
   i) Add and view comments on blog posts.
  
4) Like Functionality:
   i) Like and unlike blog posts.
  ii) Track and display the number of likes for each post.

6) Responsive Design: The application is designed to be responsive and user-friendly on both desktop and mobile devices.
   
8) Made project Live Project on PythonAnyWhere.

<br/>
<b>Installation and Setup Instructions</b>

i) Clone the Repository

git clone https://github.com/Sanskar1811/blog_platform.git
<br/>
cd blog_platform

ii) Create and Activate a Virtual Environment

python -m venv venv
<br>
Activate the virtual environment:
On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

iii) Install Project Dependencies
With the virtual environment activated, install the required packages listed in requirements.txt.

pip install -r requirements.txt

iv) Apply Database Migrations

Apply the database migrations to set up database schema 
python manage.py makemigrations
<br/>
python manage.py migrate


v) Access the Django admin interface using create a superuser account.

python manage.py createsuperuser


vi) Run the Development Server
<br/>
python manage.py runserver


vii) Access the Admin Interface (Optional)

To access the Django admin interface, go to http://127.0.0.1:8000/admin/ 

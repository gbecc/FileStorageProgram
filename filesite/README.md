# Overview

File Vault is a web application I built using Python and Django to strengthen my skills as a software engineer and gain hands-on experience with full-stack development.  
It allows users to securely upload, store, search, download, and delete files, with each user having their own private space managed through authentication.

To start the test server, open a terminal in the project folder and run: python manage.py runserver

Then open a browser and go to: http://127.0.0.1:8000

This will load the main dashboard page of the app.

My purpose for building this project was to learn how Django handles routing, templates, user authentication, and database integration while creating something practical and secure for file management.

[Software Demo Video](https://youtu.be/2opZDohtT2E)

# Web Pages

**Login Page**  
Users sign in using Django’s authentication system. Once logged in, they are redirected to their personal dashboard.

**Dashboard Page**  
Displays all files uploaded by the logged-in user. The list is dynamically generated from the database and includes file name, size, and upload date.  
Users can also search for files by name or description.

**Upload Page**  
Allows users to upload a file with an optional description. The uploaded file is saved to the server, stored in the database, and immediately appears on the dashboard.

**File Detail / Delete Page**  
Shows detailed information about a specific file and provides options to download or delete it.  
The delete confirmation page is also generated dynamically before removing the file and its database record.

---

# Development Environment

I developed this project using Visual Studio Code on Windows 10.  
The programming language used is Python, and the web framework is Django.  
For testing, I used Django’s built-in development server and SQLite as the database.

---

# Useful Websites

* Django Documentation - https://docs.djangoproject.com/en/5.0/  
* Real Python – Django Tutorial - https://realpython.com/get-started-with-django-1/  
* TutorialsPoint – Django Guide - https://www.tutorialspoint.com/django/index.htm  

---

# Future Work

* Add success messages after file uploads and deletions.  
* Display file sizes in readable units (KB or MB).  
* Create a “Stats” page showing total storage used and number of uploads.  
* Improve the user interface and overall styling.  
* Integrate with tools in my homelab such as nextcloud.

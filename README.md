# MyProjects
This project contains small book tracking system used to keep track of books. It supports following functions:
1. Add
2. Delete
3. Search
4. Update
5. List

This project is created using Python's Django framework. Moreover, it needs MySQL database access to store the data.
To run this project, make sure you have mySQL daemon running. Connect MySQL client to the daemon and create database named 'BookTracker'.
Now, change settings.py contains right parameters for DATABASES field. Following is an example:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'booktracker',                     
        'USER': 'root',                     
        'PASSWORD': 'train1234',                 
    }
}

Change USER and PASSWORD fields with correct MySQL login details.
Next, simply run this App using following command:
- python manage.py runserver
Connect from your browser at http://127.0.0.1:8000

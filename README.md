# MyProjects
This project contains small book tracking system used to keep track of books. It supports following functions:
1. Add
2. Delete
3. Search
4. Update
5. List

Steps to run the project:
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

Design Decisions:
- All the features were implemented and tested
- Condition when null data is entered in HTML form is handled
- Add functionality creates new element if not present or else overwrites over the element already present
- Update functionality works similar to add functionality wherein if data is present, it updates it or else adds it into database

Possible improvements:
- Strict type checking can be implemented so as to avoid entering corrupt data. For eg: Character cannot be entered into rating field which is integer
- Update functionality should provide the list of books available and should be able to select from those rather than typing the title into form

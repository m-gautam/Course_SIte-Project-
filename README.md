# Course Site
 
*This is course guide website built with the python using Django Web Framework.Main features of website like ADD, SEARCH, REVIEW SYSTEM and  carrier fields corresponding to each course which will help the students to opt right course at right time.*


## The Project has four basic features:
* ADD a course
* SEARCH for a course
* ADD reviews
* SEARCH for a professor
* SEARCH for Career field(this will tell what courses you should do to go in a particular field)


## Installation Guide


> https://www.python.org/downloads/

> ### Installation of Django
* git clone git://github.com/django/django.git
* pip install -e django/


> ## Installation of Database
* sudo apt-get update
* sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
* sudo mysql_install_db
* sudo mysql_secure_installation



> git clone https://github.com/m-gautam/Course_SIte-Project-.git


> ### In app folder Coursesite/Coursesite/settings.py
  **edit above fields according to your system**
    
     DATABASES = {

         'default': {

             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'Courses',
             'USERNAME': 'root',
             'PASSWORD': '*******',
             'HOST': 'localhost',
             'PORT': ''
         }
     }



### After connecting the database, apply the project migrations.
> *sudo python manage.py migrate*

### RUN
> *sudo python manage.py runserver*






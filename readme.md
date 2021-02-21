#INTERVIEW SCHEDULE MANAGER
A Small application to manage the interview schedules for both the Interviewer and Candidates
This application allows to mark Available times for both the interviewers and candidates.

An HR manager/User can access the interview schedules and suggested interview times for the users by inputting both 
candidate and interviewer id's

##Setup

### Versions
``` python 3.8
    django 3.1.7
    drf 3.12.2
```
Create an environment to work with and install the required packages
### Virtual environment
Create a python 3.6 virtualenv
``` sh
    virtualenv -p python3 myprojectenv
    source myprojectenv/bin/activate
 
    pip install -r requirments.txt
```

### Create Database and User

``` postgresql
    sudo -i -u postgres
    psql
    
    CREATE DATABASE myproject;
    CREATE USER myprojectuser WITH PASSWORD 'password';

    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

    \q
    exit
```

### Django Setup

Download sample local.py file to save local settings in dir portal/local.py. Sample given below
https://github.com/sweenip/AppPortal/blob/f5b79d45b299f77259931daf7b400c28ca14ba2f/portal/local.py

Migrate database
```python manage.py migrate```

Create 1 interviewer and 1 candidate to get started quick       
```python manage.py loaddata init_users.json```
This creates 2 users, interviewer with user id=1, candidate with user id=2

Create superuser enter username, email and password (If a superuser is required)   
```python manage.py createsuperuser```

Run the Project       
```python manage.py runserver```

Website running at http://localhost:8000/

### API details
1. API to enter available time to respective users
``http://localhost:8000/api/v1/schedule/available-time/``


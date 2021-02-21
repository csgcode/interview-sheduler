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
General Info to take care while sending data.

All params are required
DateFormat sample - 2021-03-01 10:45:00+00:00 (Timezone in required)

1. API to enter available time to respective users -
``POST: http://localhost:8000/api/v1/schedule/available-time/``
   
   example params:
`` 
   {
    "user": 1,
    "start_time": 2021-03-01 10:00:00+00:00,
    "end_time": 2021-03-01 18:00:00+00:00
    }``   

2. API to get the available time slots to schedule an interview
``http://localhost:8000/api/v1/schedule/view-available-time/?interviewer=1&candidate=2``
   query params - `interviewer=<interviewer_id>`, `candidate=<candidate_id>`
   
   SAMPLE OUTPUT

``{
    "data": {
        "available_slots": [
            [
                "2021-03-03T13:00:00Z",
                "2021-03-03T14:00:00Z"
            ],
            [
                "2021-03-03T10:00:00Z",
                "2021-03-03T11:00:00Z"
            ]
            ...
        ],
        "available_times": [
            [
                "2021-03-03T13:00:00Z",
                "2021-03-03T14:00:00Z"
            ],
            [
                "2021-03-03T10:00:00Z",
                "2021-03-03T11:00:00Z"
            ],
            ...
        ]
    }
}``

`available_slots`: shows the suggested slots according to the interview duration(60 mins)
                    Note: slots less than 60 mis are not shown
`available_times`: shows the time range at which the both the users are free, this can show time ranges more than 60min durations(additional)

### Assumptions and validations
1. All datetime entered are in UTC.
2. All inputs are necessary and datetime should have timezone strings.
3. Default interview duration is 1hr, this can be changed.


### Improvements for the system TODO's or How to make it better
1. Enable Authentication.
2. Bring a manager user type to manage both user, Creation and listing acc. to permissions.
3. Ability to cancel/edit an available time.
4. AUTO-SCHEDULE - add skills to user profiles auto schedule interviewer and candidates with matching skills and setup a calender API
5. write unit-tests to check the logic used while calculating overlaps - Break it , Fix it
6. dockerize

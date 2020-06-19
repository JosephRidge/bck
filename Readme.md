
What: 
- Microservice(s).
- Api.

But Why?  :  **The purpose of this "nouriture/dish" is to  allow IoT devices or in our case, nodes, to register their details and on the client side (exposed via an API) allow them to see the available/ registered devices, their status( functionality, location..etc..) all dependent on the payload sent.**

Microservice : 
Built as a Device Management micro-service: 
    - Collection of Devices details.    

API:
Built as a communication medium between the services and client: 
    - Delete device.
    - Add device.
    - Get all the available devices.                           

Results: 
    - The data fetched will be received in a semi-structured from ( JSON )  



Lets Start Cooking !!  **(8-)**

****************************************************************
Requirements : 
- Python.
- DJango.
- Django Rest Framework.

Tips: 
- Install python on you machine( windows or linux or mac)
- Install Django -- > ***pip install Django==3.0.7 or pip3 install Django==3.0.7*** (depending on your version of pip installed)
- Install  Django rest framework ---> ***pip install djangorestframework or pip3 install djangorestframework*** (depending on your version of pip installed)


Start by creating your project package file : 

**django-admin startproject bck** --> creates the root directory of your project
kindly note that the project basically contains the configurations and settings of the app.

inside the project dir, we will have: 
    - manage.py --> this is basically the commandline utility for admins and at the same time it points the program to the django_settings module.
    - bck --> this dir is the main python project.
    -  __init__.py --> basically tells the system " Yoh! this is a python file, handl me the python way".
    - settings.py --> has setting n configs for the project
    - urls.py --> this is basically the "content" directory of your site, aid in navigation from route to route
    - asgi.py --> asynchronous web server (this promotes instant intergrations amid changes made in your system) 
    - wsgi.py --> this is the Deployemnt "Team lead " haha.. 


create the project app : 
**python manage.py startapp device_info**

kindly note that if you were using pip3 you will run:
**python3 manage.py startapp device_info**


Microservices to be built: 
 - User 
 - Device + payload
 - Analysis + payload 


    **User Microservice** 
    - The core purpose is to log in the user to the system
    - authenitication

    **Device and Payload data**
    - get device details
    - Store device details
    - store device status
    - last seen
    

    **Analysis**
    - Perform data analysis from the payloads attained
    - push latest data to client-side
    - perform weekly analysis
    - perfrom monthly analysis
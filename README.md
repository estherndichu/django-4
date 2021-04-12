# VICINITY APP

#### By [Esther Ndichu](https://github.com/estherndichu)
  
# Description  
This is an app that keeps track of neighborhood happenings and contains all the businesses in the vicinity, contacts of basic services such as police hotline and local hospital.
 
## User Story  
  
* Sign in to the application to start using it.
* Set up a profile which contains:name,location and neighborhood name.
* Find a list of different businesses in the neighborhood.
* Find Contact Information for the health department and Police authorities near the neighborhood.
* Create Posts that will be visible to everyone in the neighborhood.
* Change neighborhood when user decides to move out.
* Only view details of a single neighborhood.
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 git clone 
https://github.com/estherndichu/django-4.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd django-4
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host

 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* Python3.6  
* Django 3.2  
* Heroku  
  
  
## Known Bugs  
* None 
  
## Support and contact details
For any queries or further clarification on the directions to use the application, contact via email:itskuijenga@gmail.com

### License

MIT License

Copyright (c) 2021 estherndichu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
  
# endevel-entry-django-api
 
API containing articles and tags 
 - with an option to show articles per tag
Entry task for Endevel

# Prerequirements

# to run with docker - at your own risk, might not work

requirements.txt in /endevel_entry/ directory with the following content:<br>
`django==4.0`<br/>
`psycopg2-binary==2.9.3`<br/>
`django-cors-headers==3.8.0`<br/>
`django-environ==0.8.1`<br/>
`djangorestframework==3.13.1`<br/>
`Pillow==9.0.1`<br/>

To run the server: <br>
`cd endevel_entry/`<br/>
`docker build -t blogapi .`<br/>
`docker run -d -p 8000:8000 blogapi`<br/>


# to run with pipenv
Install Pipenv package: <br>
`pip install pipenv`<br/>

requirements.txt in root of the directory with the following content:<br>
`django==4.0`<br/>
`psycopg2-binary==2.9.3`<br/>
`django-cors-headers==3.8.0`<br/>
`django-environ==0.8.1`<br/>
`djangorestframework==3.13.1`<br/>
`Pillow==9.0.1`<br/>

To run the server: <br>
`#stay in root`<br/>
`pipenv update`<br/>
`pipenv shell`<br/>
`cd endevel_entry`<br/>
`python3 manage.py runserver`<br/>

## Getting the data from the API



To get all Articles <br>
a GET request with the following format authenticated as `admin:admin` <br>
`http://127.0.0.1:8000/articles/?format=json` <br>
or with httpie: <p>`http -a admin:admin GET http://127.0.0.1:8000/articles/?format=json`</p>


To get all Tags <br>
a GET request with the following format authenticated as `admin:admin`<br>
`http://127.0.0.1:8000/tags/?format=json` <br>
or with httpie: <p>`http -a admin:admin GET http://127.0.0.1:8000/tags/?format=json`</p>


To get all Articles for a given Tag <br>
a GET request with the following format authenticated as `admin:admin`<br>
`http://127.0.0.1:8000/articles/Name?format=json` <br>
or with httpie: <p>`http -a admin:admin GET http://127.0.0.1:8000/articles/Beta?format=json`</p>




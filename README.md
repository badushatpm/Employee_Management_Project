# Employee_Management_Project

## Setup

The first thing to do is to clone the repository:

```sh
$ https://github.com/badushatpm/Employee_Management_Project.git
$ cd Employee_Management_Project
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```

APIs for CRUD:

List or Create
```sh
http://127.0.0.1:8000/api/employees/
```

Delete or Patch
```sh
http://127.0.0.1:8000/api/employees/<id>
```

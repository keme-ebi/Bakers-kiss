# Bakers-kiss
Bakers-kiss is an API service for bakers to be able to manage their orders, store recipes (in order to avoid deterioration in case the recipe is primarily written on paper), keep their recipes secure and get notifications via email reminding them to stock up. This project is a Webstack: Portfolio Project, signaling the last phase of ALX SWE training, under the short specialisation. The project is aimed to showcase what the student can do having come so far into the program.

## Project Description
### What It Does
The API service helps bakers to manage their activities like keep track of their orders and not forget due dates, store recipes for safe keeping (either by theft or deteriotation of the paper it was written on), and get reminder to stock up their ingredients.

### Technologies Used
- Python programming language for its simplicity.
- Flask for building the backend web application in Python. This was chosen since Flask is a light-weight and flexible micro-framework.
- Flask-SQLALchemy for easy interaction with the database.
- Flask-JWT for implementing authentication and authorization mechanisms which allows users to authenticate and access protected endpoints securely.
- Flask-RESTX for documenting the API endpoints. Flask-RESTX makes it easier to automatically generate interactive API documentation from code annotations (using Swagger).
- SQLite / MySQL for database.
- Python virtual environment for managing dependencies used during the project development.
- Git for version control, Github for hosting the repository.
- sqlite for testing without having to use a complicated database during development stage.
- Insomnia for API mocking (debugging and testing).
- [Ethereal.email](http://ethereal.email) to generate dummy email accounts.

## Table Of Contents
- [Project-Description](#project-description)
- [Technologies-used](#technologies-used)
- [Installation](#installation)
- [End-Points](#end-points)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation
**NOTE:** This was done on linux
- Clone or fork this repo
```$ git clone https://github.com/keme-ebi/Bakers-kiss.git```
- Setup python virtual environment in the Bakers-kiss folder.
```:~/Bakers-kiss$ python3 -m venv {name of virtual environment}```
- example: ```$ python3 -m venv env```
- Activate virtual environment
```:~/Bakers-kiss$ source env/bin/activate```
- To deactivate virtual environment
```(env) :~/Bakers-kiss$ deactivate```
- Install dependencies
```(env) :~/Bakers-kiss$ pip install -r requirements.txt```
Environment for the project is setup.

## Usage
After activation of virtual environment run:

```(env) :~/Bakers-kiss$ export FLASK_APP=app/```

Then open flask shell: ```(env) :~/Bakers-kiss$ flask shell```

If you're using MySQL (**Make sure MySQL is running in the background first**) to run the program, edit the file **create_db.py** and put your credentials, then run it to create the database for the project. If you're using SQLite, skip this:

```(env) :~/Bakers-kiss$ python create_db.py```

Create the database in the shell and exit the shell:

```>>> db.create_all()```

After installation, run the server

```(env) :~/Bakers-kiss$ python server.py```

**Open another terminal and access the [endpoints](#end-points) or test it directly in your browser by using [localhost:5000](http://localhost:5000)**

### End-Points
This is a table of the API endpoints and their uses. The endpoints are used to access various routes provided after server has started runnning. Can be mocked using Postman or Insomnia according to your preferred choice.

**NOTE:** localhost is used in place of actual url, for testing/development purposes
| URL | HTTP METHOD | USE |
|----------|----------|----------|
| localhost:5000/signup | POST | signs a new user up / registers a new user |
| localhost:5000/login | POST | logins in a registered user |
| localhost:5000/orders | GET | gets all orders of an authorized user |
| localhost:5000/orders | POST | puts or inserts a new order |
| localhost:5000/orders/\<int:order_id\> | GET | gets a specific order of an authorized user by its order id |
| localhost:5000/orders/\<int:order_id\> | PUT | updates a specific order of an authorized user by its order id |
| localhost:5000/orders/\<int:order_id\> | DELETE | deletes a specific order of an authorized user by its order id |
| localhost:5000/recipes | GET | gets all recipes of an authorized user |
| localhost:5000/recipes | POST | inserts new recipes for an authorized user |
| localhost:5000/recipes/\<int:recipe_id\> | GET | gets a specific recipe of an authorized user by its reciped id |
| localhost:5000/recipes/\<int:recipe_id\> | PUT | updates the data of a specific recipe of an authorized user by its recipe id |
| localhost:5000/recipes/\<int:recipe_id\> | DELETE | deletes a specific recipe of an authorized user by its recipe id |

**NOTE**: Each routes except the signup and login, are jwt_required, so a token is needed to access other routes, this will ensure that a user is authorized.

**NOTE**: Some actions sends a mail to user, so ensure you put a valid mail for testing purpose. You can create a fake/dummy mail from [ethereal.email](http://ethereal.email)

#### Sign a user up
```$ curl -X 'POST' 'http://localhost:5000/auth/signup' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"username": "Nonso", "email": "testa@email.com", "password": "password"}'```

#### Login a user
```$ curl -X 'POST' 'http://localhost:5000/auth/login' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"email": "test@email.com", "password": "password"}'```

#### Place an order
```$ curl -X 'POST' 'http://localhost:5000/orders/' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNzM3MDIxNiwianRpIjoiMTc0MmVjZGEtMTE3OS00NjY0LTliMGEtMGIxNDUwYjk5YjllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImthcmlhIiwibmJmIjoxNzE3MzcwMjE2LCJjc3JmIjoiZTIxZTkyYzMtY2FlZi00N2FlLTk0ZjItNTIyODA4NTgxMzJhIiwiZXhwIjoxNzE3MzcyMDE2fQ.P3KIZoFTKdEDMezHQQjlsVxZUKMew1BUqG66e-QTYAI' -H 'Content-Type: application/json' -d '{"client": "Tochi", "order_title": "birthday cake", "description": "1 layer red velvet, black whipped cream", "price": 30.49, "due_date": "2024-06-07"}'```

#### Get all orders
```$ curl -X 'GET' 'http://localhost:5000/orders/' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNzM3MDIxNiwianRpIjoiMTc0MmVjZGEtMTE3OS00NjY0LTliMGEtMGIxNDUwYjk5YjllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImthcmlhIiwibmJmIjoxNzE3MzcwMjE2LCJjc3JmIjoiZTIxZTkyYzMtY2FlZi00N2FlLTk0ZjItNTIyODA4NTgxMzJhIiwiZXhwIjoxNzE3MzcyMDE2fQ.P3KIZoFTKdEDMezHQQjlsVxZUKMew1BUqG66e-QTYAI'```

#### Get an order by its id
```$ curl -X 'GET' 'http://localhost:5000/orders/1' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNzM3MDIxNiwianRpIjoiMTc0MmVjZGEtMTE3OS00NjY0LTliMGEtMGIxNDUwYjk5YjllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImthcmlhIiwibmJmIjoxNzE3MzcwMjE2LCJjc3JmIjoiZTIxZTkyYzMtY2FlZi00N2FlLTk0ZjItNTIyODA4NTgxMzJhIiwiZXhwIjoxNzE3MzcyMDE2fQ.P3KIZoFTKdEDMezHQQjlsVxZUKMew1BUqG66e-QTYAI'```

#### Update an order by its id
```$ curl -X 'PUT' 'http://localhost:5000/orders/1' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNzM3MDIxNiwianRpIjoiMTc0MmVjZGEtMTE3OS00NjY0LTliMGEtMGIxNDUwYjk5YjllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImthcmlhIiwibmJmIjoxNzE3MzcwMjE2LCJjc3JmIjoiZTIxZTkyYzMtY2FlZi00N2FlLTk0ZjItNTIyODA4NTgxMzJhIiwiZXhwIjoxNzE3MzcyMDE2fQ.P3KIZoFTKdEDMezHQQjlsVxZUKMew1BUqG66e-QTYAI' -H 'Content-Type: application/json' -d '{"client": "Joel"}'```

#### Delete an order by its id
```$ curl -X 'DELETE' 'http://localhost:5000/orders/1' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNzM3MDIxNiwianRpIjoiMTc0MmVjZGEtMTE3OS00NjY0LTliMGEtMGIxNDUwYjk5YjllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImthcmlhIiwibmJmIjoxNzE3MzcwMjE2LCJjc3JmIjoiZTIxZTkyYzMtY2FlZi00N2FlLTk0ZjItNTIyODA4NTgxMzJhIiwiZXhwIjoxNzE3MzcyMDE2fQ.P3KIZoFTKdEDMezHQQjlsVxZUKMew1BUqG66e-QTYAI'```

#### Create a new recipe
```$ curl -X 'POST' 'http://localhost:5000/recipes/' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNzM3MDIxNiwianRpIjoiMTc0MmVjZGEtMTE3OS00NjY0LTliMGEtMGIxNDUwYjk5YjllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImthcmlhIiwibmJmIjoxNzE3MzcwMjE2LCJjc3JmIjoiZTIxZTkyYzMtY2FlZi00N2FlLTk0ZjItNTIyODA4NTgxMzJhIiwiZXhwIjoxNzE3MzcyMDE2fQ.P3KIZoFTKdEDMezHQQjlsVxZUKMew1BUqG66e-QTYAI' -H 'Content-Type: application/json' -d '{"pastry_name": "sponge cake", "ingredients": "2 cups of..." "recipe": "add flour to..."}'```

#### Get all recipes of an authorized user
```$ curl -X 'GET' 'http://localhost:5000/recipes/' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNzM3MDIxNiwianRpIjoiMTc0MmVjZGEtMTE3OS00NjY0LTliMGEtMGIxNDUwYjk5YjllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImthcmlhIiwibmJmIjoxNzE3MzcwMjE2LCJjc3JmIjoiZTIxZTkyYzMtY2FlZi00N2FlLTk0ZjItNTIyODA4NTgxMzJhIiwiZXhwIjoxNzE3MzcyMDE2fQ.P3KIZoFTKdEDMezHQQjlsVxZUKMew1BUqG66e-QTYAI'```

#### Get a recipe by its id
```$ curl -X 'GET' 'http://localhost:5000/recipes/1' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNzM3MDIxNiwianRpIjoiMTc0MmVjZGEtMTE3OS00NjY0LTliMGEtMGIxNDUwYjk5YjllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImthcmlhIiwibmJmIjoxNzE3MzcwMjE2LCJjc3JmIjoiZTIxZTkyYzMtY2FlZi00N2FlLTk0ZjItNTIyODA4NTgxMzJhIiwiZXhwIjoxNzE3MzcyMDE2fQ.P3KIZoFTKdEDMezHQQjlsVxZUKMew1BUqG66e-QTYAI'```

#### Update a recipe by its id
```$ curl -X 'PUT' 'http://localhost:5000/recipes/1' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNzM3MDIxNiwianRpIjoiMTc0MmVjZGEtMTE3OS00NjY0LTliMGEtMGIxNDUwYjk5YjllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImthcmlhIiwibmJmIjoxNzE3MzcwMjE2LCJjc3JmIjoiZTIxZTkyYzMtY2FlZi00N2FlLTk0ZjItNTIyODA4NTgxMzJhIiwiZXhwIjoxNzE3MzcyMDE2fQ.P3KIZoFTKdEDMezHQQjlsVxZUKMew1BUqG66e-QTYAI' -H 'Content-Type: application/json' -d '{"pastry_name": "super sponge cake"}'```

#### Delete a recipe by its id
```$ curl -X 'DELETE' 'http://localhost:5000/recipes/1' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNzM3MDIxNiwianRpIjoiMTc0MmVjZGEtMTE3OS00NjY0LTliMGEtMGIxNDUwYjk5YjllIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImthcmlhIiwibmJmIjoxNzE3MzcwMjE2LCJjc3JmIjoiZTIxZTkyYzMtY2FlZi00N2FlLTk0ZjItNTIyODA4NTgxMzJhIiwiZXhwIjoxNzE3MzcyMDE2fQ.P3KIZoFTKdEDMezHQQjlsVxZUKMew1BUqG66e-QTYAI'```

**After playing around with it, you can terminate via the 1st terminal using *ctrl C***

## Contributing
## License
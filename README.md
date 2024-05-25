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
- Python virtual environment for managing dependencies used during the project development.
- Git for version control, Github for hosting the repository.
- sqlite for testing without having to use a complicated database during development stage.
- Insomnia for API mocking (debugging and testing).
### Challenges Faced
## Table Of Contents
- [Installation](#installation)
- [End-Points](#end-points)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
## Installation
**NOTE:** This was done on linux
- Clone or fork this repo
```$ git clone https://github.com/keme-ebi/Bakers-kiss.git```
- Setup python virtual environment.
```$ python3 -m venv {name of virtual environment}```
- example: ```$ python3 -m venv env```
- Activate virtual environment
```$ source env/bin/activate```
- To deactivate virtual environment
```$ deactivate```
- Install dependencies
```$ pip install -r requirements.txt```
Environment for the project is setup.
## Usage
After installation, run the server
```$ python server.py```
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
## Contributing
## License

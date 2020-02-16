
<img src="=https://66.media.tumblr.com/6849576fe4489f33f25b722b32d95c0e/e89b7ceae0572455-d9/s1280x1920/f6e6a8aa3e4d82d9411b5e7aee2065890a0a8946.png" width="300" height="120" align="left">

## About 
Yurtzy🏕️ is an application targeted to urbanites that allows visitors to find campsites near the 25 largest urban agglomerations in the United States.
<img src="https://66.media.tumblr.com/0747c4bf4ec67c243ecd2d2b9f612e90/d4d94426805716f4-b5/s1280x1920/79decc3c555719442d33714c45de8ff9e0cd9043.png" align="right" width="350" height="200"> 

## Website
The site is live at <a href="http://www.yurtzy.com">Yurtzy.com</a>. This is the official site. Not all functionalities are fully integrated with the frontend. The `backend site` is hosted through Heroku and is at <a></a>. Essentially, the `backend site` only returns JSON objects for each endpoint. For more views of the site, you can also look at the `Screenshots` folder. 

## Installing Dependencies
Use `pip3 install requirements.txt` to download the requirements for this app. It is recommended to use a <a href="https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/">virtual environment</a>. The file `setup.sh` contains all of the environment variables. 

## Local Development Instructions 
Create an account on Heroku. Install Heroku with Homebrew.
`brew tap heroku/brew && brew install heroku`
Use the command `heroku login` to login with your credentials. 

The application can be deployed using the <a href="https://gunicorn.org/">Gunicorn</a> web server, a pure-Python HTTP server for WSGI applications. Install Gunicorn with `pip install gunicorn`. Create a <a href="https://devcenter.heroku.com/articles/procfile">Procfile</a> with `touch Procfile` to create. This file only needs the following line: `web: gunicorn app:app`, where `app.py` contains the app. 

<img src="https://66.media.tumblr.com/8cac95db8aa973556c1956e31e930e85/d4d94426805716f4-03/s1280x1920/b4122881c0bd459b8acc2c4bfdf2788a84cf24eb.png" align="right" width="350" height="200"> 

Use `heroku create name_of_your_app` to create the app. Then add git remote to the local repository with `git remote add heroku heroku_git_url`. Finally, we must incorporate the add on *heroku-postgresql* for apps containing a postgreSQL instance. To create a database and connect with the application, use `heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_app`. 

To check configuration variables, run `heroku config --app name_of_your_app`. To push, use `git push heroku master`. 

If you wish to use database migrations, use pip to install *flask_script*, *flask_migrate*, and *psycopg2-binary* and run
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
To run database migrations, use the command `heroku run python manage.py db upgrade --app name_of_your_app`.

## Roles
- `Contributor` can add and edit campsites. 
- `Admin` can edit, add, and delete campsites.
All visitors may access the public **GET /campsites** endpoint. 

# Endpoints
## GET /campsites
<br/>**Description:** Gets all campsites organized by nearest urban center.
<br/>**Roles:** a public endpoint. All visitors may access.
<br/>**Request Arguments:** None
<br/>**Returns**:
```
to be completed
```
<br/>**Errors:** If no campsites found, aborts in 404 error. If there is an issue with querying and retrieving the campsites, aborts in 422 error. 

## GET /campsites/<int:campsite_id>/
<br/>**Description:** Retrieves the campsite with the given campsite id.
<br/>**Roles:** a public endpoint. All visitors may access.
<br/>**Request Arguments:** campsite_id
<br/>**Returns**:
```
to be completed
```
<br/>**Errors:** If no campsite with given id found, aborts in 404 error. If there is an issue with querying and retrieving the campsite, aborts in 422 error.   

## PATCH /campsites
<br/>**Description:** Allows users to edit existing campsites. 
<br/>**Roles:** must be `Contributor` or `Admin` user.
<br/>**Request Arguments:** None 
<br/>**Returns**:
```
to be completed
```
<br/>**Errors:** If an error has arisen in attempting to edit an existing campsite, it will abort in 422 error. If no campsite with the id has been found, it will abort in a 404 error. 

## POST /campsites
<br/>**Description:** Allows users to add a new campsite to the database. 
<br/>**Roles:** must be `Contributor` or `Admin` user.
<br/>**Request Arguments:** None 
<br/>**Returns**:
```
to be completed
```
<br/>**Errors:** If a new campsite cannot be added to the datbase, it aborts in a 422 error.

## DELETE /campsites/<int:campsite_id>
<br/>**Description:** Allows an administrative user to delete a campsite in the database. 
<br/>**Roles:** must be `Admin` user. 
<br/>**Request Arguments:** campsite_id
<br/>**Returns**:
```
to be completed
```
<br/>**Errors:** If no such campsite has been found, it will abort in a 404 error. If there is a problem implementing the successful deletion of the campsite through the database connection, it will result in a 422 error.

## Error Handling
Errors are returned as JSON objects. See an example error handler below.

```
{
"success": False, 
"error": 422,
"message": "unprocessable"
}, 422
```

- **400:** Bad Request
- **404:** Resource Not Found
- **422:** Not Processable 
- **500:** Internal Server Error
- **416:** Range Not Satisfiable 

  
<img src="https://66.media.tumblr.com/5816b11c11188626b84b644b7f00c6c0/590414abc0b7ae51-26/s1280x1920/9bc735d421dd66bb4b6e5797c0df816481412cde.png" width="350" height="300" align="right">

## Authentication (under construction) 
The authentication system is Auth0. ./src/services/auth.service.ts contains the logic to direct a user to the Auth0 login page, managing the JWT token upon successful callback, and handle setting and retrieving the token from the local store. This token is then consumed by our DrinkService (./src/services/auth.service.ts) and passed as an Authorization header when making requests to our backend.

## Authorization (under construction) 
The Auth0 JWT includes claims for permissions based on the user's role within the Auth0 system. This project makes use of these claims using the auth.can(permission) method which checks if particular permissions exist within the JWT permissions claim of the currently logged-in user. This method is defined in ./src/services/auth.service.ts and is then used to enable and disable buttons in ./src/pages/drink-menu/drink-form/drink-form.html.

## Testing Endpoints with Postman (under construction) 
A <a href="https://www.postman.com/">Postman</a> collection is included to test the various endpoints. 

## Unit Tests (under construction)
To be added.

## Login 
RBAC is implemented with <a href="http://www.auth0.com">Auth0</a>. Two sample users have been added, one with an `Admin` role and one with a `Contributor` role.  

## Credits
Logos and website created with <a href="https://www.tailorbrands.com/">Tailor Brands</a>. 

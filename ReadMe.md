
<img src="https://66.media.tumblr.com/6849576fe4489f33f25b722b32d95c0e/e89b7ceae0572455-d9/s1280x1920/f6e6a8aa3e4d82d9411b5e7aee2065890a0a8946.png" width="300" height="120" align="left">

## About 
Yurtzy🏕️ is an application for urbanites that allows site visitors to find campsites near the 25 largest urban agglomerations in the United States.
<img src="https://66.media.tumblr.com/0747c4bf4ec67c243ecd2d2b9f612e90/d4d94426805716f4-b5/s1280x1920/79decc3c555719442d33714c45de8ff9e0cd9043.png" align="right" width="350" height="200"> 

## Website
The site is live at <a href="http://www.yurtzy.com">Yurtzy.com</a>. This is the official site. Frontend and backend are not integrated yet. The `backend site` is hosted through Heroku at <a href="https://yurtzy.herokuapp.com/">yurtzy.herokuapp.com</a>. Essentially, the `backend site`</a> only returns JSON objects for each endpoint. For more views of the site, you can also look at the `Screenshots` folder. 

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
<br/>**Description:** Gets all campsites organized under listings of nearest urban centers.
<br/>**Roles:** a public endpoint. All visitors may access.
<br/>**Request Arguments:** None
<br/>**Returns**:
```
{
  'success': True,
  'campsites': campsites
}
``` 
where campsites is an array containing the formatted data of all the campsites in the database.
<br/>**Errors:** If no campsites found, aborts in 404 error. If there is an issue with querying and retrieving the campsites, aborts in 422 error. 

## GET /campsites/<int:campsite_id>/
<br/>**Description:** Retrieves the campsite with the given campsite id.
<br/>**Roles:** a public endpoint. All visitors may access.
<br/>**Request Arguments:** campsite_id
<br/>**Returns**:
```
{
  'success': True,
  'campsite': campsite
}
```
where campsite is the formatted data of the campsite with the given campsite id. 
<br/>**Errors:** If no campsite with given id found, aborts in 404 error. If there is an issue with querying and retrieving the campsite, aborts in 422 error.   

## PATCH /campsites/int:campsite_id
<br/>**Description:** Allows users to edit the given campsite.
<br/>**Roles:** must be `Contributor` or `Admin` user.
<br/>**Request Arguments:** campsite_id
<br/>**Returns**:
```
{
  'success': True,
  'campsite': campsite.format()
}
```
where campsite is the object representing the model that has been updated according to form data. 
<br/>**Errors:** If an error has arisen in attempting to edit an existing campsite, it will abort in 422 error. If no campsite with the id has been found, it will abort in a 404 error. 

## POST /campsites
<br/>**Description:** Allows users to add a new campsite to the database. 
<br/>**Roles:** must be `Contributor` or `Admin` user.
<br/>**Request Arguments:** None 
<br/>**Returns**:
```
{
  'success': True,
  'campsite': campsites
}
```
where campsites is an array of the formatted data of each campsite in the database. 
<br/>**Errors:** If a new campsite cannot be added to the datbase, it aborts in a 422 error.

## DELETE /campsites/<int:campsite_id>
<br/>**Description:** Allows an administrative user to delete a campsite in the database. 
<br/>**Roles:** must be `Admin` user. 
<br/>**Request Arguments:** campsite_id
<br/>**Returns**:
```
{
  'success': True,
  'delete': campsite_id,
}
```
where *campsite_id* holds the id of the successfully deleted campsite. 
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

  
<img src="https://66.media.tumblr.com/5816b11c11188626b84b644b7f00c6c0/590414abc0b7ae51-26/s1280x1920/9bc735d421dd66bb4b6e5797c0df816481412cde.png" width="350" height="300" align="right">

## Authentication 
The authentication system is <a href="auth0.com">Auth0</a>. `./src/services/auth.service.ts` contains the logic to direct a user to the Auth0 login page, managing the JWT token upon successful callback, and handle setting and retrieving the token from the local store. This token is then consumed by our DrinkService (`./src/services/auth.service.ts`) and passed as an Authorization header when making requests to our backend.

## Authorization 
The Auth0 JWT includes claims for permissions based on the user's role within the Auth0 system. This project makes use of these claims using the auth.can(permission) method which checks if particular permissions exist within the JWT permissions claim of the currently logged-in user. This method is defined in `./src/services/auth.service.ts` and is then used to enable and disable buttons in `./src/pages/drink-menu/drink-form/drink-form.html`.

The link to the **Login** page through Auth0 is <a href="https://yurtzy.auth0.com/authorize?audience=campsite&response_type=token&client_id=Y2RH2wZ5e7OcysD25vjbb4v022PMcfCc&redirect_uri=https://yurtzy.com/login-success">here</a>.

## Testing Endpoints with Postman  
A <a href="https://www.postman.com/">Postman</a> collection is included in the **Tests** directory. For more information about Postman, click <a href="https://www.postman.com/product/api-client">here</a>.

- `Contributor` can patch and add campsites: 
(Permissions: `patch:campsites` and `post:campsites`.)

- `Admin` can patch, add, *and* delete campsites: 
(Permissions: `patch:campsites`,`post:campsites`,`delete:campsites`)


## Two Sample Insertions
To fill the default empty database, run `heroku pg:psql postgresql-clear-82843 --app yurtzy` and use the two following commands in SQL.

```
INSERT INTO "Campsite" (name,website,address,distance_from_city,closest_city,image,description,costs,yurts_and_cabins,bathrooms,parking,ada_access,campfires,showers,wifi,trash_bins,picnic_area,pets_allowed,potable_water,rv_parks,hiking,kayaking,camping,biking,swimming,cooking_grills,hunting) VALUES ('Oxbow Regional Park','https://tinyurl.com/qwwhv22','3010 SE Oxbow Pkwy, Gresham, OR 97080',23.8,'Portland','https://tinyurl.com/s8yers4','Perfect place for adventuring in the Sandy River Gorge.',22,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False);
```

```
INSERT INTO "Campsite" (name,website,address,distance_from_city,closest_city,image,description,costs,yurts_and_cabins,bathrooms,parking,ada_access,campfires,showers,wifi,trash_bins,picnic_area,pets_allowed,potable_water,rv_parks,hiking,kayaking,camping,biking,swimming,cooking_grills,hunting) VALUES ('Trillum Lake','https://www.fs.usda.gov/recarea/mthood/recarea/?recid=53634','Highway 26
Government Camp, Oregon 97028',50,'Portland','https://tinyurl.com/slcnop9','Incredible views of Mount Hood.',50,False,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,False);
```

## Unit Tests
Unit tests can be run with the commands `python3 test_flaskr.py`. Before you run the unit tests, set up the environment variable: 
```
DATABASE_URL="postgres://kwwzwozzasiqiw:8e70aed4e726e6e2d96cdf380525fa2884689070fdcda2daf3b0c389d879433f@ec2-18-213-176-229.compute-1.amazonaws.com:5432/df2ce01ne4r1gj"
export DATABASE_URL
```
Only unit tests for the two public endpoints are provided. All endpoints requiring authentication can be tested in Postman according to the instructions above. 

## Login 
RBAC is implemented with <a href="http://www.auth0.com">Auth0</a>. As noted, two sample users have been added, one with an `Admin` role and one with a `Contributor` role.  

## Overview of Drawbacks 
- Many sites offer similar services. See <a href="http://wwww.recreation.gov">Recreation.gov</a> and <a href="https://www.alltrails.com/?ref=header">AllTrails</a>.
- The database model has limitations. For examples, `costs` only provides a range of costs for the location, instead of detailed information on the costs for picnicking, the costs for camping sites for a night, etc. 
- More data could be added. Options like horseback riding, fishing, etc. 
- Only data for two campsites and one location is provided. Should be expanded to include campsites near the 25 largest urban agglomerations in the U.S., for example. See `docs/urban agglomerations.txt` for this list of the largest urban sites in 2010, provided by <a href="https://www.currentresults.com/Weather-Extremes/US/largest-cities-list.php">Current Results</a>.

## Credits
Logos and website created with <a href="https://www.tailorbrands.com/">Tailor Brands</a>. 

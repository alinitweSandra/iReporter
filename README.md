
[![Build Status](https://travis-ci.org/alinitweSandra/iReporter.svg?branch=challenge2_develop)](https://travis-ci.org/alinitweSandra/iReporter)  [![Coverage Status](https://coveralls.io/repos/github/alinitweSandra/iReporter/badge.svg?branch=challenge2_develop)](https://coveralls.io/github/alinitweSandra/iReporter?branch=challenge2_develop)  [![Maintainability](https://api.codeclimate.com/v1/badges/96cfdaef524b132b6048/maintainability)](https://codeclimate.com/github/alinitweSandra/iReporter/maintainability)


# iReporter

# iReporter
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

## Getting Started

Follow the instructions below to help you get a copy of this project and be able to run it on your local machine for development and testing.

### Prerequisites for API

What you need to install

* Python 

### Installing
To deploy this application follow these steps;
* clone/download the project from git hub
```
 git clone https://github.com/alinitweSandra/iReporter.git
```
* open the project in any Editor forexample Vs code ,Pycharm or any editor of your choice.
* create a python virtual environment using the following command
```
 virtualenv  env 
``` 
* In windows, navigate to scripts in the env folder where the virtual environment exists.
```
 cd env\scripts
```
*  Activate the virtual environment using the following command ;
```
activate.bat
```
* In linux, activate the virtual environment using ;
```
source bin/activate
```
* Execute the application by running a a given command
```
 python run.py
``` 
* After running that command the server will start running at http://127.0.0.1:5000/ which is the default URL

API Endpoints currently available are;

|__Http header__| __Endpoint__ | __Functionality__    | __Body__  |
|------|-------------|------------|--------------------------------|
|POST|  /api/v1/red-flags      | Create a ​red-flag​ record     | {"status":"draft","createdOn":"2/3/2018",
	"createdBy":"user",
	"location":[0,0],
	"comment":"comment",
	"type":"type"
}

|__Http header__| __Endpoint__ | __Functionality__ | 
|------|-------------|------------|
|POST|  /api/v1/red-flags      | create a red-flag record : {"status":"draft","createdOn":"2/3/2018","createdBy":2,
	"location":[0,0],"comment":"comment",	"type":"type"}  |
|POST| /api/v1/create-users           | sign up a  user :{"firstname":"aheebwa","lastname":"kukute","othernames":"bob","email":"sandraalinitwe@gmail.com","phoneNumber":"256757852937","username":"user","registered":"29/09/2015","isAdmin":True,"password":"user"}| 
|GET|  /api/v1/red-flags        | get all records   |
|GET|  /api/v1/red-flags/<int:id>     | get a specific record by id    |
|PUT|  /api/v1/red-flags/<int:id>     | update a record by the user and specific id of the record  |
|DELETE|  /api/v1/red-flags/<int:id>     | delete a record by id by user who created it    |
|POST| /api/v1/auth/login           | login a user {"username":user,"password":"user"}| 



## Testing 
Tests are run by installing pytest using the command below ;
```
 pip install pytest
```
Then after installing pytest, type the command below to run the tests
```
 pytest
```
## Built With
* [Flask](http://flask.pocoo.org/docs/1.0/) - Python web framework used

## Versioning
* URL Versioning has been used to version this applications endpoint 
* Currently only version:1 is available 

## Deployment
* The app is deployed on heroku  https://ireporter2.herokuapp.com/api/v1/red-flags
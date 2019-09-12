# Awards

* This is an application that allows a user to post a project that he/she has created and get it reviewed by other users.

### Author 

_Created by_: **Danmark Mutai**

## Technologies Used

* Python
* HTML
* Django micro-framework
* W3 schools
* Bootstrap(used for styling)


## Setup/Installation Requirements

- To start using this project use the following commands:

`git clone https://github.com/Dnmrk4/awards.git`

`cd awards`

`code .` _if your using VS code as your text editor._

> Then use the terminal to run the app, you'll have to run the following commands in your terminal

`pip install -r requirements.txt`

> On your terminal,Create database instagram using the command below.

`CREATE DATABASE awwards;`

> Migrate the database using the command below

`python3.6 manage.py migrate`

> , so that the app will be available on localhost:8000, to do this run the command below

`python manage.py runserver`

* access the application on this localhost address http://127.0.0.1:8000/

## Behaviour Driven Development

|  Behaviour |  Input  |  Output |
|------------|---------|---------|
| The program should navigate to the index page on load | On page load | Navigate to the home/index page |
| The program should navigate to sign up page when Sign Up is clicked | Click on Sign Up on the navigation bar | Redirected to the sign up page |
|The program should navigate to the login page when Login is clicked | Click on Login on the registration form |Redirected to the login page |
|The program should direct the user to the home page when logged in | Click on See More |  Redirected to the single project page with the project's description |
|The program should navigate to the vote form when Vote is clicked |  Click on Vote button |  A vote form pops up |
|The program should navigate to the profile editing form when the My Account is clicked on the navigation bar | Click on My Account on the navigation bar |  Redirected to the profile editing form |
|The program should load the live site on a new tab when View Site is clicked | Click on View Site | Live site of a specific project loads on a new tab|

## Prerequisites

* You need the following to work on the project: 
- Python 3.6 
- Django 
- Pip 
- virtualenv 
- A text Editor

#### Link to Live Website: https://aawrds.herokuapp.com/

## Known Bugs

* None at the moment, but if found please contact.

### Contact

* For contact and surport email me: _danmark.mutai@gmail.com_

## License

* This application uses a [MIT license](/LICENSE)

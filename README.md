# A simple twitter replica with django

An utterly fantastic project using Django 1.9.

## Features

1. register
2. login
3. twit
4. follow others (other people who log into your software)
5. view twits which are posted by the people I follow.

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Run the project

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, at [toucan-twitter application](https://toucan-twitter.herokuapp.com).

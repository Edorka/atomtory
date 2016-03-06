# atomtory
Small example project, a REST API and an AngularJS inventory

The target of this project is implement a basic imaginary inventory to show the advantages of python flask and angular.

Back-end guidelines are mainly influenced by Miguel Grinberg's articles.

# What is this?

As target of this exercice, atoms are choosen as subjects of an inventory because they have the posibility to expire in seconds or exists much longer provoking an overflow on the date format (year 9999)

At the moment, this exercise is able to add and retrieve items from this inventory. They could have caducity date or not and in case this caducity date has extended the user will be properly informed.

However types of items are limited to isotopes on the testing data, they could be easily changed and extended. Just notice that type is a mandatory attribute on any item.

Currently no security features has been added but Angular, Restangular and Flask have appropiate solutions to authenticate users and evaluate security levels and roles.

This system is configured to run with sqlite on development environment but it's recommended to upgrade into a proper SQL solution to prevent concurrency issues.

Inmediate needs of this project will be written as github's issues, anyone is welcome to colaborate.

#Installation instructions

## Development environment

Preparing back-end environment will requier python2.7 and virtualenv installed
``` sh
cd server
virtualenv venv
source venv/bin/activate
pip install -r requirements/prod.txt
```
Before running must initialize database
``` sh
python manage.py importdb -t items
```
And then run the server itself
``` sh
python manage.py runserver
```

Front-end requires node.js, npm and bower to install required dependencies
``` sh
cd client
npm install && bower install
```
Be advised that if error messages appears must insist on last intruction, if this would not work then delete node_modules and bower_components directories.

``` sh
grunt serve
```
This will run a dedicated web server and execute default browser

## Testing the project

Before running tests the enviroment will need to be provided with some extra dependencies.

``` sh
cd server
source venv/bin/activate
pip install -r requirements/dev.txt
```
Then simply call the test command on the management console
``` sh
python manage.py test
```

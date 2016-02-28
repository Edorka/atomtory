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

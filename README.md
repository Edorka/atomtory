# atomtory
Small example project, a REST API and an AngularJS inventory

The target of this project is implement a basic imaginary inventory to show the advantages of python flask and angular.

Back-end guidelines are mainly influenced by Miguel Grinberg's articles.

# What is this?

As target of this exercice, atoms are choosen as object of an inventory; as they have the posibility to expire in seconds or be able much longer provoking a ovoreflow on the date format (year 9999)

The target of this exercise is being able to add items to this inventory and obviosly retrieve them. They could have caducity date or not, in case this caducity date has extended the user will be properly informed.

How ever types of items are limited to isotopes on the testing data they cuuld be easily changed and extended. Just notice that type is a mandatory attribute on any items.

Currently no security features has been added, however Angular, Restangular and Flask have appropiate solutions to authenticate users and evaluate security levels and roles.

This system is configured to run with sqlite on development environment but it's recommended to upgrade into a proper SQL solution to prevent concurrency issues.

Inmediate needs of this projects will be written on github issues, anyone is welcome to colaborate.

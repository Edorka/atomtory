'use strict';

/**
 * @ngdoc overview
 * @name atomtoryApp
 * @description
 * # atomtoryApp
 *
 * Main module of the application.
 */
angular
  .module('atomtoryApp', [

    'ngAnimate',
    'ngCookies',
    'ngMaterial',
    'restangular',
    'ngMessages',
    'ngResource',
    'ngRoute',
    'ngSanitize'
  ])
  .config(function (RestangularProvider) {
        RestangularProvider.setBaseUrl('api/v1');
        RestangularProvider.addResponseInterceptor(function(data, operation, what, url, response/*, deferred*/) {
            if (response.status === 200){
                if (operation === 'getList' && angular.isObject(data) ){
                    // .. and handle the data and meta data
                    return data.items ? data.items : data;
                }
                return data;
            }
        });
  })
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        redirectTo: '/items'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/items', {
        templateUrl: 'views/items.html',
        controller: 'ItemsCtrl as items',
        controllerAs: 'items'
      })
      .otherwise({
        redirectTo: '/items'
      });
  });

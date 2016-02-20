'use strict';

/**
 * @ngdoc service
 * @name atomtoryApp.items
 * @description
 * # items
 * Service in the atomtoryApp.
 */
angular.module('atomtoryApp')
  .service('items', function (Restangular) {
    console.log('items service running')
    var resource = Restangular.all('items');
    function list(){
        return resource.getList();
    }
    return {list: list};
  });

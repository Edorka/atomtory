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
    var resource = Restangular.all('items');
    function list(){
        return resource.getList();
    }
    function types(){
        return Restangular.all('types').getList();
    }
    function create(item){
        return resource.post(item);
    }
    return {list: list, types: types, create: create};
  });

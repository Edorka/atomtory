'use strict';

/**
 * @ngdoc function
 * @name atomtoryApp.controller:ItemsCtrl
 * @description
 * # ItemsCtrl
 * Controller of the atomtoryApp
 */
angular.module('atomtoryApp')
  .controller('ItemsCtrl', function (items) {
    var vm = this;
    this.list = [];
    items.list().then(function(items){
        vm.list = items;
    });
    vm.expirationOf = function(item){
        console.log(item)
        if (! item.expires_at|| item.expires_at === 'None'){
            return 'will virtually not expire'
        } else {
            return item.expires_at
        }

    }
  });

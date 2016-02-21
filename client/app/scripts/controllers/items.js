'use strict';

/**
 * @ngdoc function
 * @name atomtoryApp.controller:ItemsCtrl
 * @description
 * # ItemsCtrl
 * Controller of the atomtoryApp
 */
angular.module('atomtoryApp')
  .controller('ItemsCtrl', function (items, $mdDialog) {
    var vm = this;
    this.list = [];
    items.list().then(function(items){
        vm.list = items;
    });
    this.types = [];
    items.types().then(function(types){
        vm.types = types;
    });
    this.appendItem = function(newItem){
        vm.list.unshift(newItem);
    }
    vm.create = function(){
       $mdDialog.show({
          clickOutsideToClose: true,
          // Since GreetingController is instantiated with ControllerAs syntax
          // AND we are passing the parent '$scope' to the dialog, we MUST
          // use 'vm.<xxx>' in the template markup
          templateUrl: 'views/new-item.html',
          controller: 'NewItemCtrl',
          locals:{
            appendItem: vm.appendItem,
            items: items,
            types: vm.types
          }
       });
    }
    vm.expirationOf = function(item){
        if (! item.expires_at|| item.expires_at === 'None'){
            return 'will virtually not expire'
        } else {
            return item.expires_at
        }

    }
  });

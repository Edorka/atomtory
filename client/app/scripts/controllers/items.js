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
    this.searchTerm = "";
    items.list().then(function populateItemsList(items){
        vm.list = items;
    });
    this.types = [];
    items.types().then(function populateTypes(types){
        vm.types = types;
    });
    this.appendItem = function prependInListn(newItem){
        vm.list.unshift(newItem);
    };
    vm.create = function askNewData(){
       $mdDialog.show({
            clickOutsideToClose: false,
            templateUrl: 'views/new-item.html',
            controller: 'NewItemCtrl',
            locals:{
                appendItem: vm.appendItem,
                items: items,
                types: vm.types
            }
       });
    };
    vm.expirationOf = function putMessage(item){
        // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
        if (! item.expires_at || item.expires_at === 'None'){
            return 'will virtually not expire';
        } else {
            return item.expires_at;
        }
    };
  });

'use strict';

/**
 * @ngdoc function
 * @name atomtoryApp.controller:ItemsCtrl
 * @description
 * # ItemsCtrl
 * Controller of the atomtoryApp
 */
angular.module('atomtoryApp')
  .controller('ItemsCtrl', function (items, $mdDialog, $mdToast) {
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
    this.retrieve = function retrieveItem(item){
        var index = vm.list.indexOf(item);
        item.remove().then(function allOK(e){
            vm.list.splice(index,1);
            $mdToast.show($mdToast.simple()
                .textContent('Retrieved '+item.label+'from inventory:' +e.message)
                .theme("success-toast"));
        }, function wentWrong(response){
            var message =  'Error while retrieving item';
            if ( response && response.data ){
                message = response.data.message || message;
            }
            $mdToast.show($mdToast.simple()
                .textContent(message)
                .theme("error-toast"));
            if (response.status === 410){
                vm.list.splice(index,1);
            }
        });
    };
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

'use strict';

/**
 * @ngdoc function
 * @name atomtoryApp.controller:NewitemCtrl
 * @description
 * # NewitemCtrl
 * Controller of the atomtoryApp
 */
angular.module('atomtoryApp')
  .controller('NewItemCtrl', function ($scope, $mdDialog, types, items, appendItem) {
    $scope.types = types;
    $scope.closeDialog = function() {
        $mdDialog.hide();
    };
    $scope.submit = function(item){
        items.create(item).then(appendItem).then($mdDialog.hide);
    }
  });

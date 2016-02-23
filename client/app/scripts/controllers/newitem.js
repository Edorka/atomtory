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
    $scope.item = {};
    $scope.canSubmit = false;
    console.log('scope'. $scope);
    $scope.expireType = 'none';
    $scope.close = function close() {
        $mdDialog.hide();
    };
    $scope.$watch('item', function(value){
        $scope.canSubmit = ( item.label.length > 0 ) && ( item.type_id !== undefined );
    });
    $scope.submit = function requestSave(item){
        items.create(item).then(appendItem).then($mdDialog.hide);
    };
  });

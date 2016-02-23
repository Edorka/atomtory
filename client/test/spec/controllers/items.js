'use strict';

describe('Controller: ItemsCtrl', function () {

  // load the controller's module
  beforeEach(module('atomtoryApp'));

  var ItemsCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ItemsCtrl = $controller('ItemsCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));
});

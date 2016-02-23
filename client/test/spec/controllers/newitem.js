'use strict';

describe('Controller: NewItemCtrl', function () {

  // load the controller's module
  beforeEach(module('atomtoryApp'));

  var NewItemCtrl, scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    NewItemCtrl = $controller('NewItemCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));
  it('should instantiate a blank item to the scope', function () {
    console.log('NewItemCtrl');
    expect(NewItemCtrl.item).toBe({});
  });
  it('should toggle canSubmit flag when data is not valid', function () {
    expect(NewItemCtrl.canSubmit).toBe(true);
  });
});

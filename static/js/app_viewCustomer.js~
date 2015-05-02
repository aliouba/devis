var my_app = angular.module("viewCustomer", [ "ngSanitize","ngResource", "ngRoute","ui.tinymce", "ngCookies","ActivityServiceMock"]);
my_app.config(function($httpProvider,$resourceProvider,$routeProvider,$interpolateProvider) {
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

my_app.controller("viewCustomerCtrl", function($scope,$routeParams, $location, $filter ,$http, $cookies,activitiesService ) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
	/////////////////////////////////////////Get Customer///////////////
	$scope.customer = activitiesService.getCustomerInPath();
	///Données///////////
	$scope.estimates = activitiesService.getCEstimates($scope.customer).query();
});

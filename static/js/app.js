var my_app = angular.module("newEstimate", [ "ngSanitize","ngResource", "ngRoute","ui.tinymce", "ngCookies" ,"ActivityServiceMock","MesDirectives"]);
my_app.config(function($httpProvider,$resourceProvider,$routeProvider,$interpolateProvider) {
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

my_app.controller("formMakedevisCtrl", function($scope,$routeParams, $location, $filter ,$http, $cookies,activitiesService ) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
	/////////////////////////////////////////Get Siret///////////////
	$scope.siret = activitiesService.getSiretInPath();
	///Données///////////
	$scope.detailsCompany = activitiesService.getEntrDetails($scope.siret).get();
	$scope.conf = activitiesService.getEntrConf($scope.siret).get();
	$scope.groups = activitiesService.getGroups($scope.siret).query();
	//Par défaut , on montre que la page d'accueil
	$scope.showHome = true;
	$scope.showformPltsActs = false;
	$scope.showformPltsActsParam = false;
	$scope.showformUser = false;
	///Superficie ou plant/////
	$scope.parPlant = false;
	$scope.parSuperficie = false;	
	$scope.typePlOuSup = null;
	////params////////
	$scope.allParams = {
		nombrePlants: 0
	};
	////benefits////////
	$scope.allbenefits = {};
    $scope.userauthedfalse = 0;
    $scope.userauthedtrue = 1;
});
my_app.controller("formloginnavCtrl", function($scope,$routeParams, $location, $filter ,$http, $cookies,activitiesService ) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    $scope.userauthedfalse = 0;
    $scope.userauthedtrue = 1;
    $scope.loginbyajax = function function_name (email,password) {
    	$scope.loginAjax = activitiesService.loginByAjax(email,password);
    	console.log($scope);
    }
});
my_app.controller("viewCustomerCtrl", function($scope,$routeParams, $location, $filter ,$http, $cookies,activitiesService ) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
	/////////////////////////////////////////Get Customer///////////////
	$scope.customer = activitiesService.getCustomerInPath();
	///Estimates of customer///////////
	$scope.estimates = activitiesService.getCEstimates($scope.customer).query();
});



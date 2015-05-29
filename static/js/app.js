var my_app = angular.module("newEstimate", [ "ngSanitize","ngResource", "ngRoute","ui.tinymce", "ngCookies" ,"ActivityServiceMock","MesDirectives"]);
my_app.config(function($httpProvider,$resourceProvider,$routeProvider,$interpolateProvider) {
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

my_app.controller("formMakedevisCtrl", function($scope,$timeout,$routeParams, $location, $filter ,$http, $cookies,activitiesService ) {
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
    $scope.$on('handleBroadcastAuth', function(event, args) {
        $scope.userauthedfalse = $scope.userauthedtrue;
    });
});
my_app.controller("formloginnavCtrl", function($scope,$rootScope,$timeout,$routeParams, $location, $filter ,$http, $cookies,activitiesService ) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
	$scope.userauthedfalse = 0;
	$scope.userauthedtrue = 1;
	$scope.loginAjax = false;

	$scope.loginAjaxFunc = function(email,password) {
		
		activitiesService.loginByAjax(email,password)
		.then(function(data) {
			$scope.htmlsuccesslogin = '<a href="#" class="dropdown-toggle" data-toggle="dropdown">'+ data +'<span class="caret"></span></a><ul class="dropdown-menu" role="menu"><li><a href="/prestaviticoles/Clogout">Déconnexion</a></li></ul>';
			document.getElementById("loginnavbarform").innerHTML = $scope.htmlsuccesslogin;
			$scope.loginAjax = true;
			console.log(data);
			$rootScope.$broadcast('handleBroadcastAuth', "yes");
		}, function(data) {
			document.getElementById("erreurAjaxLog").innerHTML = '<div class="alert alert-danger" role="alert">'+ data +'</div>';
			$scope.loginAjax = false;
			$timeout(emptyajaxloginerror, 3000);
		}, function(data) {
			document.getElementById("formLoginnavbar").innerHTML = '<center><img src="/media/loading_spinner.gif" /></center>';
		});
	}
});
my_app.controller("viewCustomerCtrl", function($scope,$timeout,$routeParams, $location, $filter ,$http, $cookies,activitiesService ) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
	/////////////////////////////////////////Get Customer///////////////
	$scope.customer = activitiesService.getCustomerInPath();
	///Estimates of customer///////////
	$scope.estimates = activitiesService.getCEstimates($scope.customer).query();
});

emptyajaxloginerror = function() {
	document.getElementById("erreurAjaxLog").innerHTML = '';
}

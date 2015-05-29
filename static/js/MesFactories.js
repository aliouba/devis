angular.module("ActivityServiceMock", [])
.factory("activitiesService", function($http, $resource, $location, $q) {
    //Recupération des infos de l'entreprise
    return {
        getEntrDetails: function (siret) {
         return $resource('/prestaviticoles/api/company/:siret/',{siret:siret});
       },
       getEntrConf: function (siret) {
         return $resource('/prestaviticoles/api/conf/:siret/',{siret:siret});
       },
       getGroups: function (siret) {
         return $resource('/prestaviticoles/api/group_activities/:siret/',
          {siret:siret}
          );  
       },
       getCEstimates: function (customer) {
         return $resource('/prestaviticoles/api/Cbenefits/:customer/',
          {customer:customer}
          );  
       },
       getSiretInPath: function(){
        newPath = $location.absUrl();
        var tabPath = newPath.split("/");
        for (var i = 0; i < tabPath.length ; i++) {
          if(tabPath[i] == "make_estimate"){
            return  tabPath[i+1];
          }
        };          
      },
       getSiretInPath: function(){
        newPath = $location.absUrl();
        var tabPath = newPath.split("/");
        for (var i = 0; i < tabPath.length ; i++) {
          if(tabPath[i] == "make_estimate"){
            return  tabPath[i+1];
          }
        };          
      },
       loginByAjax: function(email,password){
        var deferred = $q.defer();
        $http({
            url: "/prestaviticoles/CloginAjax/",
            contentType: 'application/json',
            method: 'POST',
            data: { 'email': email,'password' : password},
            dataType: 'json'
        }).success(function (data, status, response, header) {
          if (data.erreur) {
            deferred.reject(data.erreur,response);
          } else{
              deferred.resolve(data.username);
          }
            deferred.resolve(data);
        }).error(function (data, status, response, header) {
            deferred.reject(data,response);
        });
        return deferred.promise;
      },
      makeDeis: function (siret,groups,alloptions) {
        $http({
            url: "/prestaviticoles/make_estimate/"+siret+"/",
            contentType: 'application/json',
            method: 'POST',
            data: { 'benefits': groups,'allparams' : alloptions},
            dataType: 'json'
        }).success(function (data, status, response, header) {

        }).error(function (data, status, response, header) {

        });
      }
    }
})  

angular.module("ActivityServiceMock", [])
.factory("activitiesService", function($http, $resource, $location) {
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
      $http({
          url: "/prestaviticoles/CloginAjax/",
          contentType: 'application/json',
          method: 'POST',
          data: { 'email': email,'password' : password},
          dataType: 'json'
      });
    },
    makeDeis: function (siret,groups,alloptions) {
      $http({
          url: "/prestaviticoles/make_estimate/"+siret+"/",
          contentType: 'application/json',
          method: 'POST',
          data: { 'benefits': groups,'allparams' : alloptions},
          dataType: 'json'
      });
    }
  }
})  

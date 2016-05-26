var pollsControllers = angular.module('pollsControllers',[]);


pollsControllers.controller('PollsDetailController',['$scope', '$routeParams', '$http',
	function($scope, $routeParams, $http){
		$http.get('http://localhost:8000/polls/api/polls/' + $routeParams.pollsId + '?format=json').success(function(data){
			$scope.polls = data;
		});
	}
]);

pollsControllers.controller('PollsAllController',['$scope', '$routeParams', '$http',
	function($scope, $routeParams, $http){
		$http.get('http://localhost:8000/polls/api/polls?format=json').success(function(data){
			$scope.polls = data;
		});
	}
]);
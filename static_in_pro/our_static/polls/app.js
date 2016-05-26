var pollsApp = angular.module('pollsApp', ['ngRoute', 'pollsControllers']);

pollsApp.config(['$routeProvider',
	function($routeProvider){
		$routeProvider.
		when('/id/:pollsId',{
			templateUrl: '/static/polls/partials/polls-details.html',
			controller: 'PollsDetailController'
		})
		.when('/',{
			templateUrl: '/static/polls/partials/polls.html',
			controller:'PollsAllController'
		});
	}
]);

pollsApp.config([
	'$httpProvider', function($httpProvider){
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	}
]);
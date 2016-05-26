$interpolateProvider.startSymbol('[[').endSymbol(']]');

$httpProvider.defaults.xsrfCokieeName = 'csrftoken';
$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

$resourceProvider.defaults.stripTrailingSlashes = false;

angular.module('twitterApp.services', ['ngResource'])
	.factory('Tweet', function($resource){
		return $resouce('/api/tweets/:id/');
	});

var newTweet = new Tweet();
newTweet.name = "My new tweet!";
newTweet.$save();

Tweet.get({id:123}, function(tweet){
	console.log(tweet);
});

Tweet.get({id:123})
	.$promise.then(function(tweet){
		$scope.tweet = tweet;
	});


tweeterController.controller('TweeterCtrl', function 
	TweeterCtrl($scope, Tweeter){

	});

Tweet.query(function(response){
	$scope.tweets = response;
});

$scope.submitTweet = function(text){
	var tweet = new Tweet({text: text});
	$tweet.$save(function(){
		$scope.tweets.unshift(tweet);
	})
}
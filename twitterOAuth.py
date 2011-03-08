import twitter, sys

drinks = { 'Budweiser': '', 'Pinot Noir': 'fr', 'Cava': 'es' }
terms = [ 'drinking', '#drunk' ]

api = twitter.Api(consumer_key='LAXmG8IRbqDc9ALD7Eg', consumer_secret='5Cw2CFwwznLiI8fZxn2NuUCz8uGyEiqzsTHh8bW8BzY', access_token_key='14787753-piEfHYbBzEfINj3McdIFcl6vCIFA98dyMyji7qDJG', access_token_secret='vtyZgpcwEBkNf1cw74EdGZBNxBucZkyWArU8XwEKJA') 

if len( sys.argv ) > 1:
	if sys.argv[1] in drinks:
		#print drinks[ sys.argv[1] ]
		drink = sys.argv
		region = drinks[ sys.argv[1] ]


#print api.VerifyCredentials()
#print api.GetSearch("#drunk")
results = api.GetSearch( term="drinking", lang=region, page=1, per_page=50 )
#for result in results:
#	print result.text
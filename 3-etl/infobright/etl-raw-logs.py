#################################
# FUNCTION USED 
#################################

# processLine parses the line and returns a string of tab delimited fields suitable for import into Infobright / Postgres
import re
def processLine(inputLine):


	# Decompose the line into list using each tab delimited separator

	fieldsList = inputLine.split('\t')
	for field in fieldsList:
		print "field = ", field

	# Now check that fields are the correct format
	if checkFormat(fieldsList):
		# process the line
		dt = fieldsList[0]
		tm = fieldsList[1]
		user_ipaddress = fieldsList[5]
		page_url = fieldsList[10]
		user_agent = fieldsList[11]
		uri_query = fieldsList[10]

		browserAndOsDetails = processUserAgent(user_agent) # browserAndOsDetails is a map containing descriptors of the browser and OS (TODO: list fields in comment for clarity)

		queryFields = processUriQuery(uri_query) # the remaining fields are packed in this map (TODO: list fields in comment for clarity)

	else:
		# handle the error (log it to a file? or just ignore the line)
		return 0


# checks if the format of the line of data is as expected, and handles the error if not
def checkformat(fieldsList):
	isCorrectFormat = True

	# check that the first field contains the date
	if not(re.match(r'\d\d\d\d-\d\d-\d\d',fieldsList[0])) then isCorrectFormat = False
	
	# check that the second field contains the time
	if not(re.match(r'\d\d:\d\d:\d\d', fieldsList[1])) then isCorrectFormat = False

	# check that the cs-method is a GET
	if not(fieldsList[6] == 'GET') then isCorrectFormat = False

	# check that the GET is for ice.png
	if not(fieldsList[8] == '/ice.png') then isCorrectFormat = False

	# check that HTTP status code is 200
	if not(fieldsList[9] == 200) then isCorrectFormat = False

	return isCorrectFormat

def processUserAgent(user_agent):
	# insert code here, leverage existing library (Google for best)
	return 

def processUriQuery(queryFields):
	# Decompose the query string based on the '&' character into a a key value map, using the "=" in the string to differentiate keys from values

	# Note: do we want someway to capture query values that do not live in the schema? 
	return


##################################
# UNIT TEST DATA 
##################################

sampleDataLine1 = '''2012-05-18	10:50:29	FRA2	3344	83.5.80.148	GET	d3gs014xn8p70.cloudfront.net	/ice.png	200	https://psychic.skynet/shop/checkout/	Mozilla/5.0%20(X11;%20Ubuntu;%20Linux%20x86_64;%20rv:11.0)%20Gecko/20100101%20Firefox/11.0	&ev_ca=ecomm&ev_ac=checkout&ev_la=email&ev_pr=ERROR&r=263447&urlref=https%253A%252F%252Fpsychic.skynet%252F2-tarot-cards&_id=a24c01072e3bc2ae&lang=en-US&visit=18&pdf=0&qt=1&realp=0&wma=1&dir=0&fla=1&java=1&gears=0&ag=0&res=1920x1080&cookie=1
'''
sampleDataLine2 = '''2012-05-18	10:50:38	FRA2	3344	83.5.80.148	GET	d3gs014xn8p70.cloudfront.net	/ice.png	200	https://psychic.skynet/shop/checkout/	Mozilla/5.0%20(X11;%20Ubuntu;%20Linux%20x86_64;%20rv:11.0)%20Gecko/20100101%20Firefox/11.0	&ev_ca=ecomm&ev_ac=checkout&ev_la=id_last_name&r=365103&urlref=https%253A%252F%252Fpsychic.skynet%252F2-tarot-cards&_id=a24c01072e3bc2ae&lang=en-US&visit=18&pdf=0&qt=1&realp=0&wma=1&dir=0&fla=1&java=1&gears=0&ag=0&res=1920x1080&cookie=1
'''



print "Processing line 1"
print "Line 1 input: ", sampleDataLine1
print "Line 1 output: ", processLine(sampleDataLine1)
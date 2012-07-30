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
		page_url = fieldsList[9]
		user_agent = fieldsList[10]
		uri_query = fieldsList[11]

		# commenting out below line for testing purposes (haven't decided which user agent utils library to use)	
		# browserAndOsDetails = processUserAgent(user_agent) # browserAndOsDetails is a map containing descriptors of the browser and OS (TODO: list fields in comment for clarity)

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
	queryList = queryFields[1:].split('&') # split the list of queries into separate key=value pairs, each of which forms an item in a list. Note - we drop the first character ('&') so that we don't start the list with an empty item

	# Now create convert the list of parameters in the form (key=value) into a dictionary where each entry takes the form (key, value)
	queryDictionary = map(splitKeyValue, queryList)

	# Now extract the relevant fields from the query string, or set the values to NULL if they are not present
	possibleParametersList = ["tid", "uid", "vid", "lang", "cookie", "refr", "page", "url", "ev_ca", "ev_la", "ev_pr", "ev_va"]

	# Query string parameters map onto those in the Hive table definition as follows:
	# tid = txn_id 
	# uid = user_id
	# vid = visit_id (really visit counter)
	# lang = br_lang
	# cookie = br_cookies
	# refr = page_referrer
	# url = page_url
	# page = page_title
	# ev_ca = ev_category
	# ev_ac = ev_action
	# ev_la = ev_label
	# ev_pr = ev_property
	# ev_va = ev_value 
	# utm_source = mkt_source
	# utm_medium = mkt_medium
	# utm_term = mkt_term
	# utm_content = mkt_content
	# utm_campaign = mkt_name
	

	browserFeatureList = ["pdf", "fla", "java", "dir", "qt", "realp", "wma", "gears", "ag"]


	# Note: do we want someway to capture query values that do not live in the schema? 
	return

# splits a query parameter of the form key=value into a tuple (key, value)
def splitKeyValue(queryParameter):
	(key, value) = queryParameter.split('=')
	return key, value


##################################
# UNIT TEST DATA 
##################################

sampleDataLine1 = r'2012-07-23	18:01:25	DUB2	3402	82.23.113.162	GET	d3gs014xn8p70.cloudfront.net	/ice.png	200	https://www.psychicbazaar.com/shop/checkout/	Mozilla/5.0%20(iPhone;%20CPU%20iPhone%20OS%205_1_1%20like%20Mac%20OS%20X)%20AppleWebKit/534.46%20(KHTML,%20like%20Gecko)%20Version/5.1%20Mobile/9B206%20Safari/7534.48.3	&ev_ca=ecomm&ev_ac=checkout&ev_la=email&ev_pr=ERROR&tid=534263&uid=71b74fd331fa1eb5&vid=1&lang=en-gb&refr=http%253A%252F%252Fwww.psychicbazaar.com%252F4-jewellery&f_pdf=0&f_qt=1&f_realp=0&f_wma=0&f_dir=0&f_fla=0&f_java=0&f_gears=0&f_ag=0&res=320x480&cookie=1&url=https%253A%252F%252Fwww.psychicbazaar.com%252Fshop%252Fcheckout%252F'
sampleDataLine2 = r'2012-07-23	18:01:25	DUB2	3402	82.23.113.162	GET	d3gs014xn8p70.cloudfront.net	/ice.png	200	https://www.psychicbazaar.com/shop/checkout/	Mozilla/5.0%20(iPhone;%20CPU%20iPhone%20OS%205_1_1%20like%20Mac%20OS%20X)%20AppleWebKit/534.46%20(KHTML,%20like%20Gecko)%20Version/5.1%20Mobile/9B206%20Safari/7534.48.3	&ev_ca=ecomm&ev_ac=checkout&ev_la=paypal-button&tid=109138&uid=71b74fd331fa1eb5&vid=1&lang=en-gb&refr=http%253A%252F%252Fwww.psychicbazaar.com%252F4-jewellery&f_pdf=0&f_qt=1&f_realp=0&f_wma=0&f_dir=0&f_fla=0&f_java=0&f_gears=0&f_ag=0&res=320x480&cookie=1&url=https%253A%252F%252Fwww.psychicbazaar.com%252Fshop%252Fcheckout%252F'



print "Processing line 1"
print "Line 1 input: ", sampleDataLine1
print "Line 1 output: ", processLine(sampleDataLine1)
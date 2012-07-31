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
		page_url, mkt_source, mkt_medium, mkt_campaign, mkt_term, mkt_content = processCallingUrl(fieldsList[9])
		user_agent = fieldsList[10]
		uri_query = fieldsList[11]

		# commenting out below line for testing purposes (haven't decided which user agent utils library to use)	
		
		browserAndOsDetails = processUserAgent(user_agent) # browserAndOsDetails is a map containing descriptors of the browser and OS (TODO: list fields in comment for clarity)

		queryParameters = urlparse.qs(uri_query) # fields from the query string are packed in this dictionary

		# Map snowplow.js query parameters to associated fields in Hive / Infobright / PostgreSql
		txn_id 			= queryParameters.get('tid', None)
		user_id 		= queryParameters.get('uid', None)
		visit_id 		= queryParameters.get('vid', None)
		lang 			= queryParameters.get('br_lang', None)
		cookie 			= queryParameters.get('br_cookie', None)
		page_referrer 	= queryParameters.get('refr', None)
		page_url 		= queryParameters.get('url', None)
		ev_category 	= queryParameters.get('ev_ca', None)
		ev_action 		= queryParameters.get('ev_ac', None)
		ev_label 		= queryParameters.get('ev_la', None)
		ev_property 	= queryParameters.get('ev_pr', None)
		ev_value 		= queryParameters.get('ev_va', None)
		if mkt_source = None:
			mkt_source		= queryParameters.get('utm_source', None) 
		if mkt_medium = None:
			mkt_medium		= queryParameters.get('utm_medium', None)
		if mkt_campaign = None:
			mkt_campaign	= queryParameters.get('utm_campaign', None)
		if mkt_term = None:
			mkt_term		= queryParameters.get('utm_term', None)
		if mkt_content = None:
			mkt_content		= queryParameters.get('utm_content', None)
		
		return # return a string of tab delimited fields, by concatenating together

	else:
		# handle the error (log it to a file? or just ignore the line)
		return None


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

def processCallingUrl(referrerUrl):
	o = urlparse.urlparse(referrerUrl)
	p = urlparse.qs(o.query)
	return (o.geturl, p.get(utm_source, None), p.get(utm_medium, None), p.get(utm_campaign, None), p.get(utm_term, None), p.get(utm_content, None))


##################################
# UNIT TEST DATA 
##################################

sampleDataLine1 = r'2012-07-23	18:01:25	DUB2	3402	82.23.113.162	GET	d3gs014xn8p70.cloudfront.net	/ice.png	200	https://www.psychicbazaar.com/shop/checkout/	Mozilla/5.0%20(iPhone;%20CPU%20iPhone%20OS%205_1_1%20like%20Mac%20OS%20X)%20AppleWebKit/534.46%20(KHTML,%20like%20Gecko)%20Version/5.1%20Mobile/9B206%20Safari/7534.48.3	&ev_ca=ecomm&ev_ac=checkout&ev_la=email&ev_pr=ERROR&tid=534263&uid=71b74fd331fa1eb5&vid=1&lang=en-gb&refr=http%253A%252F%252Fwww.psychicbazaar.com%252F4-jewellery&f_pdf=0&f_qt=1&f_realp=0&f_wma=0&f_dir=0&f_fla=0&f_java=0&f_gears=0&f_ag=0&res=320x480&cookie=1&url=https%253A%252F%252Fwww.psychicbazaar.com%252Fshop%252Fcheckout%252F'
sampleDataLine2 = r'2012-07-23	18:01:25	DUB2	3402	82.23.113.162	GET	d3gs014xn8p70.cloudfront.net	/ice.png	200	https://www.psychicbazaar.com/shop/checkout/	Mozilla/5.0%20(iPhone;%20CPU%20iPhone%20OS%205_1_1%20like%20Mac%20OS%20X)%20AppleWebKit/534.46%20(KHTML,%20like%20Gecko)%20Version/5.1%20Mobile/9B206%20Safari/7534.48.3	&ev_ca=ecomm&ev_ac=checkout&ev_la=paypal-button&tid=109138&uid=71b74fd331fa1eb5&vid=1&lang=en-gb&refr=http%253A%252F%252Fwww.psychicbazaar.com%252F4-jewellery&f_pdf=0&f_qt=1&f_realp=0&f_wma=0&f_dir=0&f_fla=0&f_java=0&f_gears=0&f_ag=0&res=320x480&cookie=1&url=https%253A%252F%252Fwww.psychicbazaar.com%252Fshop%252Fcheckout%252F'
sampleDataLine3 = r'2012-07-24	16:54:50	LAX3	3448	64.60.168.146	GET	d3gs014xn8p70.cloudfront.net	/ice.png	200	https://www.psychicbazaar.com/shop/checkout/	Mozilla/5.0%20(iPhone;%20CPU%20iPhone%20OS%205_1_1%20like%20Mac%20OS%20X)%20AppleWebKit/534.46%20(KHTML,%20like%20Gecko)%20Version/5.1%20Mobile/9B206%20Safari/7534.48.3	page=Psychic%2520Bazaar%2520Checkout&tid=654477&uid=5636c31749a19950&vid=1&lang=en-us&refr=http%253A%252F%252Fwww.psychicbazaar.com%252Fsearch%253Fsearch_query%253DEden&f_pdf=0&f_qt=1&f_realp=0&f_wma=0&f_dir=0&f_fla=0&f_java=0&f_gears=0&f_ag=0&res=320x480&cookie=1&url=https%253A%252F%252Fwww.psychicbazaar.com%252Fshop%252Fcheckout%252F'



print "Processing line 1"
print "Line 1 input: ", sampleDataLine1
print "Line 1 output: ", processLine(sampleDataLine1)
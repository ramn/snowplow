import optparse
p = optparse.OptionParser()

# output file
p.add_option("-o", action="store", dest="outfile")
p.add_option("--output", action="store", dest="outfile")

# source file
p.add_option("-i", dest="infile")
p.add_option("--input", dest="infile")

# parse the command line
opts, args = p.parse_args()

# retrieve the options settings
outfile = opts.outfile
infile = opts.infile 

print "infile is ",  infile
print "outfile is ", outfile

i = open(infile)
line = i.readline()

while line:
	# parse the input line of data, creating a list of fields each delimited by the ctrl-a character (chr(1))
	fieldsList = line.split(chr(1)) 
	fieldsString = '\t'.join(map(str, fieldsList))
	print fieldsString

# processLine takes an input line of Hive data (ctrl-a delimited with browser features packed into an array) 
# and returns a tab delimited string suitable for import into InfoBright
def processLine(inputLine):
	# check that the line of data corresponds to the expected format (i.e. X fields, each ctrl-a delimited)
	
	# create a list, where each field in the original line of data constitues one element in the list
	fieldsList = inputLine.split(chr(1))

	# convert the browser features array (the Xth element in the list) into a single tab delimited string
	fieldsList[X] = convertBrowserFeatures(fieldsList[X])

	# then convert the list into a tabl delimited string suitable to be imported into InfoBright
	outputLine = '\t'.join(map(str, fieldsList))
	
	return outputLine

# function takes the Hive formatted browser features field (a ctrl-b separated list of the browser features a
# browser does have) and replaces it with a tab delimited list of boolean fields listing all the possible
# browser features, suitable for importing into InfoBright
def convertBrowserFeatures(inputFeatures):

	# create a list, where each element is one of the features
	browserFeaturesList = inputFeatures.split(chr(2))

	# now check for the existence of each browser feature, and assign the appropriate value to the feature variable
	br_features_pdf = false
	br_features_flash = false
	br_features_java = false
	br_features_director = false
	br_features_quicktime = false
	br_features_realplayer = false
	br_features_windowsmedia - false
	br_features_gears = false
	br_features_silverlight = false

	if 'pdf' in browserFeaturesList:
		br_features_pdf = true

	if 'flash' in browserFeaturesList:
		br_features_flash = true

	if 'java' in browserFeaturesList:
		br_features_java = true

	if 'director' in browserFeaturesList:
		br_features_director = true

	if 'quicktime' in browserFeaturesList
		br_features_quicktime = true

	if 'realplayer' in browserFeaturesList:
		br_features_realplayer = true

	if 'wma' in browserFeaturesList:
		br_features_windowsmedia = true

	if 'gears' in browserFeaturesList:
		br_features_gears = true

	if 'silverlight' in browserFeaturesList:
		br_features_silverlight = true

	# now concatenate the results together into a single tab delimited string 
	outputBrowserFeatures = str(br_features_pdf) + '\t' + str(br_features_flash) + '\t' str(br_features_java) +	'/t' + str(br_features_director) + '/t' + str(br_features_quicktime) + '/t' + str(br_features_realplayer) + '/t' + str(br_features_windowsmedia) + '/t' + str(br_features_gears) + '/t' + str(br_features_gears) + '/t' + br_features_silverlight

	return outputBrowserFeatures
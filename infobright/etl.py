#***********************************************************************************************************
# FUNCTIONS DEPLOYED IN PROGRAMME FLOW
# ***********************************************************************************************************

# following function looks in specified directory and returns a list of folders
import os
import re
def get_eligible_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if (os.path.isdir(os.path.join(dir, name)) and re.match(r'dt=\d\d\d\d-\d\d-\d\d', name))]

# processLine takes an input line of Hive data (ctrl-a delimited with browser features packed into an array) 
# and returns a tab delimited string suitable for import into InfoBright
def processLine(inputLine):
	# check that the line of data corresponds to the expected format (i.e. 24 fields, each ctrl-a delimited)
	
	# create a list, where each field in the original line of data constitues one element in the list
	fieldsList = inputLine.split(chr(1))

	# convert the browser features array (the Xth element in the list) into a single tab delimited string
	fieldsList[24] = convertBrowserFeatures(fieldsList[24])
	# NOTE: is there a better way to do this than using a mutable list?

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
	br_features_pdf = False
	br_features_flash = False
	br_features_java = False
	br_features_director = False
	br_features_quicktime = False
	br_features_realplayer = False
	br_features_windowsmedia = False
	br_features_gears = False
	br_features_silverlight = False

	if 'pdf' in browserFeaturesList:
		br_features_pdf = True

	if 'flash' in browserFeaturesList:
		br_features_flash = True

	if 'java' in browserFeaturesList:
		br_features_java = True

	if 'director' in browserFeaturesList:
		br_features_director = True

	if 'quicktime' in browserFeaturesList:
		br_features_quicktime = True

	if 'realplayer' in browserFeaturesList:
		br_features_realplayer = True

	if 'wma' in browserFeaturesList:
		br_features_windowsmedia = True

	if 'gears' in browserFeaturesList:
		br_features_gears = True

	if 'silverlight' in browserFeaturesList:
		br_features_silverlight = True

	# now concatenate the results together into a single tab delimited string 
	outputBrowserFeatures = str(br_features_pdf) + '\t' + str(br_features_flash) + '\t' + str(br_features_java) + '\t' + str(br_features_director) + '\t' + str(br_features_quicktime) + '\t' + str(br_features_realplayer) + '\t' + str(br_features_windowsmedia) + '\t' + str(br_features_gears) + '\t' + str(br_features_gears) + '\t' + str(br_features_silverlight)

	return outputBrowserFeatures



# ***********************************************************************************************************
# PROGRAM FLOW BEGINS HERE
# ***********************************************************************************************************


# optparse used to handle parameters passed in at the command line
import optparse
p = optparse.OptionParser()

# output file
p.add_option("-o", action="store", dest="outfile")
p.add_option("--output", action="store", dest="outfile")

# source folder
p.add_option("-i", dest="infolder")
p.add_option("--input", dest="infolder")

# parse the command line
opts, args = p.parse_args()

# retrieve the options settings
outfile = opts.outfile
inputFolder = opts.infolder 

# Create an output file
o = open(outfile, 'w')

listOfSubFolders = get_eligible_subdirectories(inputFolder)
for subFolder in listOfSubFolders:
	print "Processing folder ", subFolder
	
	listOfFiles = os.listdir(os.path.join(inputFolder, subFolder))
	for file in listOfFiles:
		i = open(os.path.join(inputFolder, subFolder, file), 'r')
		print "Processing file" + os.path.join(inputFolder, subFolder, file)
		inputLine = i.readline()
		while inputLine:
			o.writelines(processLine(inputLine))
			inputLine = i.readline()

i.close()
o.close()

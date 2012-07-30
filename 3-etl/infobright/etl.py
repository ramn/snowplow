#***********************************************************************************************************
# FUNCTIONS DEPLOYED IN PROGRAMME FLOW
# ***********************************************************************************************************

# following function looks in specified directory and returns a list of folders
import os
import re
def getEligibleSubFolders(dir):
    return [name for name in os.listdir(dir)
            if (os.path.isdir(os.path.join(dir, name)) and re.match(r'dt=\d\d\d\d-\d\d-\d\d', name))]
 
# following function parses the date from the folder name
def getDate(subFolder):
	# folder name is of the form 'dt=YYYY-MM-DD' so extracting the date just means eliminating the first three characters
	return subFolder[3:]

# processLine takes an input line of Hive data (ctrl-a delimited with browser features packed into an array) 
# and returns a tab delimited string suitable for import into InfoBright
def processLine(inputLine, dt, debugFile):
	# check that the line of data corresponds to the expected format (i.e. 24 fields, each ctrl-a delimited)
	
	# create a list, where each field in the original line of data constitues one element in the list
	fieldsList = inputLine.split(chr(1))

	# convert the browser features array (the Xth element in the list) into a single tab delimited string
	try: 
		fieldsList[24] = convertBrowserFeatures(fieldsList[24]) # NOTE: is there a better way to do this than using a mutable list?
	except:
		print "ERROR! inputLine is \t", inputLine
		debugFile.writelines("Error converting 24th field (browser features)  to new format.\n Date = \t" + dt + "\n Line = \t" + inputLine)

	# then convert the list into a tab delimited string suitable to be imported into InfoBright
	outputLine = dt +'\t' + '\t'.join(map(str, fieldsList))
	
	return outputLine

# function takes the Hive formatted browser features field (a ctrl-b separated list of the browser features a
# browser does have) and replaces it with a tab delimited list of boolean fields listing all the possible
# browser features, suitable for importing into InfoBright
def convertBrowserFeatures(inputFeatures):

	# create a list, where each element is one of the features
	browserFeaturesList = inputFeatures.split(chr(2))

	allBrowserFeaturesList = ["pdf", "fla", "java", "dir", "qt", "realp", "wma", "gears", "ag"]

	browserFeaturesPresent = lambda feature: str(int(feature in browserFeaturesList)) # inclusion of int ensures that output is in 1s and 0s not Trues and Falses (necessary for Infobright)
	return "\t".join(map(browserFeaturesPresent, allBrowserFeaturesList))


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

# debug file. (This is set to error.log if not alternative argument is supplied)
p.add_option("-d", dest="debugfile")
p.add_option("--debug", dest="debugfile")

# set default debug file to error.log
p.set_defaults(debugfile = "error.log")

# parse the command line
opts, args = p.parse_args()

# retrieve the options settings
outfile = opts.outfile
inputFolder = opts.infolder 
debugFile = opts.debugfile

# Create an output file
o = open(outfile, 'w')

# create the debug file
d = open(debugFile, 'w')

listOfSubFolders = getEligibleSubFolders(inputFolder)
for subFolder in listOfSubFolders:
	print "Processing folder ", subFolder
	
	listOfFiles = os.listdir(os.path.join(inputFolder, subFolder))
	for file in listOfFiles:
		i = open(os.path.join(inputFolder, subFolder, file), 'r')
		print "Processing file" + os.path.join(inputFolder, subFolder, file)
		inputLine = i.readline()
		while inputLine:
			o.writelines(processLine(inputLine, getDate(subFolder), d))
			inputLine = i.readline()

i.close()
o.close()

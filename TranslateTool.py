#########

__author__ = "William <williamsukatube@gmail.com>"
__version__ = "v 0.1"

import os
import sys

# how to use?
# python3 TranslateTool.py <fileName>  <space or tab>
# parameter space means replace 4 space by tab
# tab means replace tab by 4 space
# example:
#   python3 TranslateTool.py testdata space   // which means replace all 4 space each line by tab

if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print ("your input must equals to 3 parameters, which contains file name and translate command")
		print ("you can have a look at the ")
		os._exit(0)
	
	# parse filename and command
	fileName = sys.argv[1]
	command = sys.argv[2]

	# replace 	
	filep = open(fileName)
	content = ""
	while True:
		line = filep.readline()
		if not line:
			break
		if "space" in command:
			content = content + line.replace('\t', '    ')
		else:
			content = content + line.replace('    ', '\t')
	filep.close()
	os.system("rm " + fileName)
	
	# write down content to origin file
	f = open(fileName, 'w')
	f.write(content)
	f.close()
	print ("replace data success! check it!")

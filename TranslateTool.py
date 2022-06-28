#########

__author__ = "William <williamsukatube@gmail.com>"
__version__ = "v 0.1"

import os
import sys

# how to use?
# python3 TranslateTool.py <fileName>  <space or tab>
# parameter space means replace tab by 4 space
# tab means replace 4 space by tab
# example:
#   python3 TranslateTool.py testdata space   // which means replace all 4 space each line by tab

def IsBlankLine(content):
	content = content.rstrip('\n')
	content = content.replace('\t', '    ')
	for i in range(0, len(content)):
		if (content[i] != ' '):
			return False
	return True

def replaceFile(fileName, command):
	# replace 	
	filep = open(fileName)
	content = ""
	while True:
		line = filep.readline()
		if not line:
			break
		if IsBlankLine(line):
			print ("bingo")
			content = content + "\n"
			continue
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

if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print ("your input must equals to 3 parameters, which contains file name and translate command")
		print ("you can have a look at the ")
		os._exit(0)
	
	# parse filename and command
	fileName = sys.argv[1]
	command = sys.argv[2]

	if (fileName == "-all"):
		if (len(sys.argv) < 4):
			print ("if you select replace all file module, you need input file type!")
			os._exit(0)
		fileType = sys.argv[3]
		cmd = "find * -name *" + fileType + " > data" 
		os.system(cmd)
		f_data = open("data")
		while True:
			fileName = f_data.readline()
			if not fileName:
				break
			fileName = fileName.rstrip('\n')
			replaceFile(fileName, command)
		os._exit(0)

	# single file replace	
	replaceFile(fileName, command)

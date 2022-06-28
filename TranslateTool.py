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
			content = content + "\n"
			continue
		if "space" in command:
			content = content + line.replace('\t', '    ').rstrip().rstrip('\t') + "\n"
		elif "tab" in command:
			content = content + line.replace('    ', '\t').rstrip().rstrip('\t') + "\n"
		else:
			content = content + line.rstrip().rstrip('\t') + "\n"
	filep.close()
	os.system("rm " + fileName)
	
	# write down content to origin file
	f = open(fileName, 'w')
	f.write(content)
	f.close()
	print ("clean file <" + fileName.rstrip('\n') + "> success! check it!")

def DoCleanupJob():
	fileType = sys.argv[2]
	cmd = "find * -name *" + fileType + " > data"
	os.system(cmd)
	f_data = open("data")
	while True:
		fileName = f_data.readline()
		if not fileName:
			break
		fileName = fileName.rstrip('\n')
		command = "cleanup"
		replaceFile(fileName, command)
	os.system("rm -rf data")
	os._exit(0)

def PrintUsage():
	print ("usage:")
	print ("python3 TranslateTool.py -h")
	print ("python3 TranslateTool.py cleanup  <fileType|fileName>      // to clean extra space or tab")
	print ("python3 TranslateTool.py <filename> <space|tab>            // which means replace file indent by 4 space or by tab")
	print ("python3 TranslateTool.py testdata space                    // which means replace all 4 space each line by tab")
	print ("python3 TranslateTool.py -all <space|tab>  <fileType>      // which means all .c file replace all 4 space each line by tab, fileType means .c .cpp .go .py etc...")

if __name__ == "__main__":
	if (len(sys.argv) < 3):
		cmd = sys.argv[1]
		if (cmd.find("-h") != -1 or cmd.find("--help") != -1):
			PrintUsage()
			os._exit(0)
	
	# parse filename and command
	fileName = sys.argv[1]
	command = sys.argv[2]

	# cleanup extra space or extra tab
	if (fileName.find("cleanup") != -1):
		DoCleanupJob()
		os._exit(0)

	if (fileName == "-all"):
		if (len(sys.argv) < 4):
			print ("if you select replace all file module, you need input file type!")
			PrintUsage()
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
		os.system("rm -rf data")
		os._exit(0)

	# single file replace
	replaceFile(fileName, command)

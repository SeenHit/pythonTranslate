#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2021-2022 Hacash Device Co., Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__author__ = "William <williamsukatube@gmail.com>"
__version__ = "v 0.1"

import os
import sys

def PrintUsage():
	print ("usage:")
	print ("python3 AddLicenseTool.py -h")
	print ("python3 AddLicenseTool.py <fileName> <licenseFileName>    // Add license header by your license file")

def AddLicense(fileName, licenseFileName):
	if (os.access(licenseFileName, os.F_OK) == False):
		print ("license file path is invalid, check again!")
		PrintUsage()
		os._exit(0)

	file = open(licenseFileName)
	content = ""
	while True:
		line = file.readline()
		if not line:
			break
		content = content + line.rstrip('\n') + "\n"
	content = content + "\n"
	file.close()

	file = open(fileName)
	while True:
		line = file.readline()
		if not line:
			break
		content = content + line.rstrip('\n') + "\n"
	file.close()

	os.system("rm " + fileName)
	# write down content to origin file
	f = open(fileName, 'w')
	f.write(content)
	f.close()

if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print ("need input parameter file name and license file name!!!")
		PrintUsage()
		os._exit(0)

	fileName = sys.argv[1]
	licenseFileName = sys.argv[2]
	cmd = "find * -name \"*" + fileName + "\" > data"
	os.system(cmd)

	f_data = open("data")
	while True:
		fileName = f_data.readline()
		if not fileName:
			break
		fileName = fileName.rstrip('\n')
		AddLicense(fileName, licenseFileName)

	os.system("rm -rf data")
	os._exit(0)

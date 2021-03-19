#! /usr/bin/env python
from collections import OrderedDict
import os
import subprocess
import time 

FOLDER_WITH_OUTPUTS = 'outputs'

finalArr = {}

for filename in os.listdir(FOLDER_WITH_OUTPUTS):	
	if filename.endswith(".txt"):
		theFile = FOLDER_WITH_OUTPUTS + '/' + filename
		
		with open(theFile) as fp:
			line = fp.readline()
			cnt = 1

			while line:
				line = line.strip()
				if "https://arweave.net/" in line: 
					fileNum = filename[6:]
					fixed = int(fileNum.split(".", 1)[0])

					finalArr[fixed] = line
				
				line = fp.readline()
				cnt += 1

result = dict(sorted(finalArr.items()))

for i in result: 
	print(str(i) + " : " + finalArr[int(i)])

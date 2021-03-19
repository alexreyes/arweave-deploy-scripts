#! /usr/bin/env python
import os
import subprocess
import time 

FOLDER_WITH_PNGS = 'named'

for filename in os.listdir(FOLDER_WITH_PNGS):	
	if filename.endswith(".png"):
		print(filename)	
		runCommand = 'arweave deploy ' + FOLDER_WITH_PNGS + '/' + filename + ' --key-file quarantine-journal-keyfile.json <<< CONFIRM >> outputs/output' + filename + '.txt'
		output = subprocess.run(runCommand, shell=True)

		print(output)

	else:
		continue
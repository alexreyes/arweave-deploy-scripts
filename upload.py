#! /usr/bin/env python
import os
import subprocess
import time 

def uploadFiles(uploadFolder):
	if (uploadFolder == "images"): 
		os.mkdir("imageOutputs")
	
	elif(uploadFolder == "metadata"): 
		os.mkdir("metadataOutputs")

	for filename in os.listdir(uploadFolder):	
		if filename.endswith(".png"):
			print(filename)	

			runCommand = 'arweave deploy ' + uploadFolder + '/' + filename + ' --key-file quarantine-journal-keyfile.json <<< CONFIRM >> imageOutputs/output' + filename + '.txt'
			output = subprocess.run(runCommand, shell=True)

			print(output)

		elif filename.endswith(".json"):
			print(filename)	
			runCommand = 'arweave deploy ' + uploadFolder + '/' + filename + ' --key-file quarantine-journal-keyfile.json <<< CONFIRM >> metadataOutputs/output' + filename + '.txt'
			output = subprocess.run(runCommand, shell=True)

			print(output)

		else: 
			continue

	print()
	print("UPLOAD COMPLETE")
	print()
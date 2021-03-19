import os

finalArr = {}

def getLinks(folder): 
	for filename in os.listdir(folder):	
		if filename.endswith(".txt") or filename.endswith(".json"):
			theFile = folder + '/' + filename
			
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

	if (folder == "imageOutputs"): 
		f = open("getImageLinks.txt", "w+")

		for i in result: 
			f.write(str(i) + " : " + finalArr[int(i)])
			f.write("\n")

		f.close()

	elif (folder == "metadataOutputs"): 
		f = open("getMetadataLinks.txt", "w+")

		for i in result: 
			f.write(str(i) + " : " + finalArr[int(i)])
			f.write("\n")

		f.close()

	print()
	print("GOT THE LINKS")
	print()
import os 

external_url = "https://million-dollar-nft.vercel.app/"
description = "testing new covers"

def makeMetadata():
	os.mkdir("metadata")
	f = open("getImageLinks.txt", "r")
	Lines = f.readlines()
 
	count = 0
	# Strips the newline character
	for line in Lines:
		count += 1
		splitUp = line.split(' ')

		blockNum = int(splitUp[0])
		imageURL = splitUp[2].rstrip("\n")
		name = "Million Dollar NFT" + " #" + str(blockNum)

		metadata = {"attributes":[{"trait_type":"Block number","value":blockNum}],"description":description,"external_url":external_url,"image":imageURL,"name":name}

		directory = "metadata/" + str(blockNum) + ".json"

		writeMetadata = open(directory, "w+")
		writeMetadata.write(str(metadata))
		writeMetadata.close()

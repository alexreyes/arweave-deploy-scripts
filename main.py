# import makeMetadata
from upload import uploadFiles
from links import getLinks
from createMetadata import makeMetadata
import time

def main(): 
	uploadFiles('images')
	getLinks('imageOutputs')
	makeMetadata()
	uploadFiles('metadata')
	getLinks('metadataOutputs')

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
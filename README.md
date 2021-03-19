# arweave-deploy-scripts

I made this in order to batch upload 10k images to arweave & generate 10k pieces of metadata (and upload the metadata to arweave) in order to create metadata links for an NFT project. 


## Requirements: 

- Put all images in a folder named images

## Running: 

```python3 main.py```

## Outputs: 

imageOutputs folder -- arweave-deploy outputs from uploading images
getImageLinks.txt -- links to each of the uploaded images

metadata folder -- folder containing all generated metadata files
metadataOutputs folder -- arweave-deploy outputs from uploading metadata
getMetadataLinks.txt -- links to each of the uploaded metadata files
arr = []

with open("getMetadataLinks.txt") as fp:
	line = fp.readline()
	cnt = 1
	while line:
		# print("Line {}: {}".format(cnt, line.strip()))
		line = fp.readline()
		lineResult = line.split(' ')
		if (lineResult[0] != ""): 
			final = lineResult[2].rstrip("\n")
			arr.append(final)
			

		cnt += 1

print(arr)
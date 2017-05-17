f1=open('03.protein.fa')

labels=set()

for line in f1:
	#print (line)
	if line[0]!='>':
		line=line.strip()
		#print (line)
		for i in line:
			labels.add(i)

print (labels)
print (len(labels))

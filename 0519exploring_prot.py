f=open('03.protein.fa')
#o=open('03.pro.oneline.fa','w')

first_aa=set()
list_of_line=[]
num_seq=0

for line in f:
	list_of_line.append(line)
f.close()

names=locals()
for i in range(0,len(list_of_line),1):
	if list_of_line[i][0]=='>':
		num_seq+=1
		first_aa.add(list_of_line[i+1][0])
first_aa=list(first_aa)
print ('number of sequence=', num_seq)

for i in range(0,len(first_aa),1):
	names['label_%s'%first_aa[i]]=0
	#print (names['label_%s'%first_aa[i]])
	#print ('label_%s'%first_aa[i])

for i in range(0,len(list_of_line),1):
	if list_of_line[i][0]=='>':
		names['label_%s'%list_of_line[i+1][0]]+=1

for i in range(0,len(first_aa),1):
	print ('number of label %s='%first_aa[i], names['label_%s'%first_aa[i]])
	print ('frequency of label %s='%first_aa[i], names['label_%s'%first_aa[i]]/num_seq)


#num_total=0
#for line in f:
	#line=line.strip()
	#if line[0]!='>':
		#for i in line:
			#num_total+=1


###Raw code for giving variables in a loop:
#print (num_total)
names=locals()
for i in range(0,10,1):
	names['x%s'%i]=i
	print (names['x%s'%i])

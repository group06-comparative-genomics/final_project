

#####Make a dictionary & a list of all the nucleotides
f=open('03.fa.txt')
seq_dict={}
key=0
seq_list=[]

for line in f:
	if line[0]!='>':
		line=line.strip()
		for i in line:
			seq_dict[key]=i
			key+=1
			seq_list.append(i)
#print(seq_dict)
print('Total number of nucleotides in this genome=', len(seq_list))
f.close()

#####Count the numbers of start codons(total)
num_start_codon=0
for key,value in seq_dict.items():
	if key<=len(seq_dict)-3:
		if seq_dict[key]=='A' and seq_dict[key+1]=='T' and seq_dict[key+2]=='G':
			num_start_codon+=1
print ('Total number of start codon(ATG) in this genome=', num_start_codon)

#####Count the numbers of stop codons(total)
num_stop_codon=0
for key,value in seq_dict.items():
	if key<=len(seq_dict)-3:
		if seq_dict[key]=='T' and seq_dict[key+1]=='A' and seq_dict[key+2]=='A':
			num_stop_codon+=1
		elif seq_dict[key]=='T' and seq_dict[key+1]=='A' and seq_dict[key+2]=='G':
			num_stop_codon+=1
		elif seq_dict[key]=='T' and seq_dict[key+1]=='G' and seq_dict[key+2]=='A':
			num_stop_codon+=1
print ('Total number of stop codons(TAAs, TAGs and TGAs) in this genome=', num_stop_codon)


#####Give out predicted orfs. Minimum length need to be set(not included). Overlapping allowed. Only start codon(ATG) and stop codons (TAA,TAG,TGA) are taken into account. Has to be used togerther with former codes as the list of all the nucleotides is needed.
o1=open('03.predictedgenes.50.fa','w')
n=0
for nucleo_num1 in range (0,len(seq_list)-2,1):
	if seq_list[nucleo_num1]=='A' and seq_list[nucleo_num1+1]=='T' and seq_list[nucleo_num1+2]=='G':
		genelist=['A','T','G']
		for nucleo_num2 in range (nucleo_num1+3,len(seq_list),1):
			if seq_list[nucleo_num2]=='T' and seq_list[nucleo_num2+1]=='A' and seq_list[nucleo_num2+2]=='A':
				break
			if seq_list[nucleo_num2]=='T' and seq_list[nucleo_num2+1]=='A' and seq_list[nucleo_num2+2]=='G':
				break
			if seq_list[nucleo_num2]=='T' and seq_list[nucleo_num2+1]=='G' and seq_list[nucleo_num2+2]=='A':
				break
			genelist.append(seq_list[nucleo_num2])
		if len(genelist)>50:##Set your minimum length for predicted ORFs.
			n+=1
			o1.write('>03.fa.txt--orf%s'%n+'  possition%s'%(nucleo_num1+1)+'  length='+str(len(genelist))+'\n')
			for i in genelist:
				o1.write(i)
			o1.write('\n')
o1.close()

###Annex1:visualise the content of genome at certain positions
f=open('03.fa.txt')
seq_list=[]

for line in f:
	if line[0]!='>':
		line=line.strip()
		for i in line:
			seq_list.append(i)
print (seq_list[198293:201280])
f.close()

###Annex2: eukaryote genome (30.fa.txt)
h=open('30.fa.txt')
i=0
for line in h:
	#if line[0]=='>':
	i+=1
print (i)
h.close()

###Annex3: explore proteome
h=open('03.protein.fa')
i=0
for line in h:
	if line[0]=='>':
		i+=1
print(i)
h.close()

###Annex4: Rewrite long ORF file. Remove '\n'. IMPORTANT!!!!
h=open('03.longorf')
o=open('03.longorf.oneline','w')
line_list=[]
for line in h:
	line=line.strip()
	line_list.append(line)
for i in range(0,len(line_list),1):
	if line_list[i][0]=='>':
		o.write(line_list[i]+'\n')
	elif i+1<len(line_list) and line_list[i+1][0]=='>':
		o.write(line_list[i]+'\n')
	else:
		o.write(line_list[i])
#print(line_list)
h.close()

###Annex5
#h=open('03.longorf')
o=open('03.longorf.oneline')
line_list=[]
for line in o:
	line=line.strip()
	line_list.append(line)
maxlen=0
maxlenseq='AS'
minlen=8607
minlenseq='AS'
#print (line)
for i in line_list:
	#print (i)
	if i[0]!='>':
		thelen=len(i)
		#print (thelen)
		if thelen>maxlen:
			maxlen=thelen
			maxlenseq=i
		if thelen<minlen:
			minlen=thelen
			minlenseq=i
print (maxlen,maxlenseq,minlen,minlenseq)
o.close()

###Annex6
f=open('03.fa.txt')
unique_set=set()
num_uni=0
for line in f:
	if line[0]!='>':
		line=line.strip()
		for i in line:
			if i!='A' and i!='T' and i!='C' and i!='G':
				unique_set.add (i)
				num_uni+=1
print (unique_set, num_uni)
f.close()

#print(seq_dict)
#d={3:4,1:2,5:6,7:8}
#for k,v in d.items():
	#print (k,v)

#c=set([87,2,2,2,4,5,87])
#for i in c:
	#print(i)

NNN
TAG
TGA
TAA
ATG



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


#####
o1=open('03.predictedgenes.fa','w')
for nucleo_num1 in range (0,len(seq_list)-2,1):
	if seq_list[nucleo_num1]=='A' and seq_list[nucleo_num1+1]=='T' and seq_list[nucleo_num1+2]=='G':
		genelist=[]
		for nucleo_num2 in range (nucleo_num1,len(seq_list),1):
			if seq_list[nucleo_num2]=='T' and seq_list[nucleo_num2+1]=='A' and seq_list[nucleo_num2+2]=='A':
				break
			if seq_list[nucleo_num2]=='T' and seq_list[nucleo_num2+1]=='A' and seq_list[nucleo_num2+2]=='G':
				break
			if seq_list[nucleo_num2]=='T' and seq_list[nucleo_num2+1]=='G' and seq_list[nucleo_num2+2]=='A':
				break
			genelist.append(seq_list[nucleo_num2])
		o1.write('>03.fa.txt--orf starting from position%s'%nucleo_num1+'\n')
		o1.write(str(genelist)+'\n')
o1.close()
#d={3:4,1:2,5:6,7:8}
#for k,v in d.items():
	#print (k,v)

#c=set([87,2,2,2,4,5,87])
#for i in c:
	#print(i)

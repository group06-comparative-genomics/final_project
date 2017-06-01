#####Instruction: This script is divided into six parts, for the prediction of ORFs on the four prokaryotes. It also outputs the total number of nucleotides in the genome, start codon(ATG) and stop codons(TAAs, TAGs and TGAs).
#####Part 1: Make a dictionary & a list of all the nucleotides.
f=open('09.fa.txt')
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

print('Total number of nucleotides in this genome=', len(seq_list))
f.close()

#####Part 2: Count the numbers of start codons(total)
num_start_codon=0
for key,value in seq_dict.items():
	if key<=len(seq_dict)-3:
		if seq_dict[key]=='A' and seq_dict[key+1]=='T' and seq_dict[key+2]=='G':
			num_start_codon+=1
print ('Total number of start codon(ATG) in this genome=', num_start_codon)

#####Part 3: Count the numbers of stop codons(total)
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


#####Part 4: Give out predicted orfs in both the direct and reverse strand. Minimum length need to be set(not included). Overlapping allowed. Start codon(ATG) and stop codons (TAA,TAG,TGA) are taken into account. Has to be used togerther with former codes as the list of all the nucleotides is needed.
###Shine-Dalgarno consensus sequence is added. In this script only GAGG consensus sequence is added. The searching interval is 2 to 50 bases upstream of the start codon.
o1=open('09.pregenes.SD4-50.0601.fa','w')###The name of the primary ORF file with overlapping ones.
n=0
for nucleo_num1 in range (50,len(seq_list)-2,1):
	if seq_list[nucleo_num1]=='A' and seq_list[nucleo_num1+1]=='T' and seq_list[nucleo_num1+2]=='G':
		for k in range (-50,-2,1):
			if seq_list[(nucleo_num1+k):(nucleo_num1+k+4)]==['G','A','G','G']:
				#print (seq_list[(nucleo_num1+k):(nucleo_num1+k+7)])
				#n+=1
				#print (n)
				genelist=['A','T','G']
				for nucleo_num2 in range (nucleo_num1+3,len(seq_list)-2,3):
					if seq_list[nucleo_num2]=='T' and seq_list[nucleo_num2+1]=='A' and seq_list[nucleo_num2+2]=='A':
						break
					if seq_list[nucleo_num2]=='T' and seq_list[nucleo_num2+1]=='A' and seq_list[nucleo_num2+2]=='G':
						break
					if seq_list[nucleo_num2]=='T' and seq_list[nucleo_num2+1]=='G' and seq_list[nucleo_num2+2]=='A':
						break
					genelist.append(seq_list[nucleo_num2])
					genelist.append(seq_list[nucleo_num2+1])
					genelist.append(seq_list[nucleo_num2+2])
				if len(genelist)>100:##Set your minimum length for predicted ORFs.
					n+=1
					o1.write('>09.fa.txt--orf direct%s'%n+'  position%s'%(nucleo_num1+1)+'  length='+str(len(genelist))+'\n')
					for i in genelist:
						o1.write(i)
					o1.write('\n')


###Now take the reverse strand into account.
n=0
for nucleo_num1 in range (len(seq_list)-58,1,-1):
	if seq_list[nucleo_num1]=='T' and seq_list[nucleo_num1-1]=='A' and seq_list[nucleo_num1-2]=='C':
		for k in range (2,50,1):
			if seq_list[(nucleo_num1+k):(nucleo_num1+k+4)]==['C','T','C','C']:
				genelist=['A','T','G']
				for nucleo_num2 in range (nucleo_num1-3,1,-3):
					if seq_list[nucleo_num2]=='A' and seq_list[nucleo_num2-1]=='T' and seq_list[nucleo_num2-2]=='T':
						break
					if seq_list[nucleo_num2]=='A' and seq_list[nucleo_num2-1]=='T' and seq_list[nucleo_num2-2]=='C':
						break
					if seq_list[nucleo_num2]=='A' and seq_list[nucleo_num2-1]=='C' and seq_list[nucleo_num2-2]=='T':
						break
					#if seq_list[nucleo_num2]=='N':
						#break
					for revnucl in range (nucleo_num2, nucleo_num2-3, -1):
						if seq_list[revnucl]=='A':
							genelist.append('T')
						if seq_list[revnucl]=='T':
							genelist.append('A')
						if seq_list[revnucl]=='C':
							genelist.append('G')
						if seq_list[revnucl]=='G':
							genelist.append('C')
						if seq_list[revnucl]=='N':###Only for 03.fa.txt, as there are a lot 'N' in it.
							genelist.append('N')
				if len(genelist)>100:##Set your minimum length for predicted ORFs.
					n+=1
					o1.write('>09.fa.txt--orf reverse%s'%n+'  position%s'%(nucleo_num1+1)+'  length='+str(len(genelist))+'\n')
					for i in genelist:
						o1.write(i)
					o1.write('\n')
o1.close()

#####Part 5: Remove the overlapping ORFs.
o4=open('09.pregenes.SD4-50.0601.fa')

stop=[]
for line in o4:
	if line[0]=='>':
		line=line.strip()
		line=line.split(' ')
		if line[1][0]=='d':
			stopposition=int(line[3][8:len(line[3])])+int(line[5][7:len(line[5])])
			stop.append(stopposition)
		if line[1][0]=='r':
			stopposition=int(line[3][8:len(line[3])])-int(line[5][7:len(line[5])])
			stop.append(stopposition)

stopset=set(stop)
o4.close()

o6=open('09.pregenes.SD4-50.0601.fa')
o5=open('09.nonoverpregenes.SD4-50.0601.fa','w')
alllist=[]
for line in o6:
	alllist.append(line)
for index in range (0,len(stop),1):
	if stop[index]!=stop[index-1]:
		o5.write(alllist[index*2])
		o5.write(alllist[index*2+1])
o6.close()
o5.close()


#####Part 6: Translate the predicted orfs.
o2=open('09.nonoverpregenes.SD4-50.0601.fa')#put the name of your newly created orf file (without overlapping ones) here.
o3=open('09.nonoverpreproteins.SD4-50.0601.fa','w')
i=0
for line in o2:
	i+=1
	if line[0]=='>':
		o3.write(line)
	if line[0]!='>':
		line=line.strip()
		for nucl in range(0,len(line),3):
			if line[nucl]=='T' and line[nucl+1]=='T' and line[nucl+2]=='T':
				o3.write('F')
			if line[nucl]=='T' and line[nucl+1]=='T' and line[nucl+2]=='C':
				o3.write('F')
			if line[nucl]=='T' and line[nucl+1]=='T' and line[nucl+2]=='A':
				o3.write('L')
			if line[nucl]=='T' and line[nucl+1]=='T' and line[nucl+2]=='G':
				o3.write('L')
			if line[nucl]=='C' and line[nucl+1]=='T':
				o3.write('L')
			if line[nucl]=='A' and line[nucl+1]=='T' and line[nucl+2]=='T':
				o3.write('I')
			if line[nucl]=='A' and line[nucl+1]=='T' and line[nucl+2]=='C':
				o3.write('I')
			if line[nucl]=='A' and line[nucl+1]=='T' and line[nucl+2]=='A':
				o3.write('I')
			if line[nucl]=='A' and line[nucl+1]=='T' and line[nucl+2]=='G':
				o3.write('M')
			if line[nucl]=='G' and line[nucl+1]=='T':
				o3.write('V')
			if line[nucl]=='T' and line[nucl+1]=='C':
				o3.write('S')
			if line[nucl]=='C' and line[nucl+1]=='C':
				o3.write('P')
			if line[nucl]=='A' and line[nucl+1]=='C':
				o3.write('T')
			if line[nucl]=='G' and line[nucl+1]=='C':
				o3.write('A')
			if line[nucl]=='T' and line[nucl+1]=='A' and line[nucl+2]=='C':
				o3.write('Y')
			if line[nucl]=='T' and line[nucl+1]=='A' and line[nucl+2]=='T':
				o3.write('Y')
			if line[nucl]=='C' and line[nucl+1]=='A' and line[nucl+2]=='T':
				o3.write('H')
			if line[nucl]=='C' and line[nucl+1]=='A' and line[nucl+2]=='C':
				o3.write('H')
			if line[nucl]=='C' and line[nucl+1]=='A' and line[nucl+2]=='A':
				o3.write('Q')
			if line[nucl]=='C' and line[nucl+1]=='A' and line[nucl+2]=='G':
				o3.write('Q')
			if line[nucl]=='A' and line[nucl+1]=='A' and line[nucl+2]=='T':
				o3.write('N')
			if line[nucl]=='A' and line[nucl+1]=='A' and line[nucl+2]=='C':
				o3.write('N')
			if line[nucl]=='A' and line[nucl+1]=='A' and line[nucl+2]=='A':
				o3.write('K')
			if line[nucl]=='A' and line[nucl+1]=='A' and line[nucl+2]=='G':
				o3.write('K')
			if line[nucl]=='G' and line[nucl+1]=='A' and line[nucl+2]=='T':
				o3.write('D')
			if line[nucl]=='G' and line[nucl+1]=='A' and line[nucl+2]=='C':
				o3.write('D')
			if line[nucl]=='G' and line[nucl+1]=='A' and line[nucl+2]=='A':
				o3.write('E')
			if line[nucl]=='G' and line[nucl+1]=='A' and line[nucl+2]=='G':
				o3.write('E')
			if line[nucl]=='T' and line[nucl+1]=='G' and line[nucl+2]=='T':
				o3.write('C')
			if line[nucl]=='T' and line[nucl+1]=='G' and line[nucl+2]=='C':
				o3.write('C')
			if line[nucl]=='T' and line[nucl+1]=='G' and line[nucl+2]=='G':
				o3.write('W')
			if line[nucl]=='C' and line[nucl+1]=='G':
				o3.write('R')
			if line[nucl]=='A' and line[nucl+1]=='G' and line[nucl+2]=='C':
				o3.write('S')
			if line[nucl]=='A' and line[nucl+1]=='G' and line[nucl+2]=='T':
				o3.write('S')
			if line[nucl]=='A' and line[nucl+1]=='G' and line[nucl+2]=='A':
				o3.write('R')
			if line[nucl]=='A' and line[nucl+1]=='G' and line[nucl+2]=='G':
				o3.write('R')
			if line[nucl]=='G' and line[nucl+1]=='G':
				o3.write('G')
		o3.write('\n')
o2.close()
o3.close()

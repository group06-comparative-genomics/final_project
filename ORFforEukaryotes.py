#####Instruction: This script is divided into six parts, for the prediction of ORFs on the eukaryote. It also outputs the total number of nucleotides in the genome, start codon(ATG) and stop codons(TAAs, TAGs and TGAs).
#####Part 1: Make a dictionary & a list of all the nucleotides
f=open('30.fa.txt')##the eukaryote genome.
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


#####Part 4: Give out predicted orfs in both strands. Minimum length need to be set(not included). Overlapping allowed (but will be removed later on). Start codon(ATG) and stop codons (TAA,TAG,TGA) are taken into account. Has to be used togerther with former codes as the list of all the nucleotides is needed.
#####Kozak consensus sequence is added. In this script only positions -3 and +4 from the translation start site is added. 
o1=open('30.pregenes.kozak100.0528.fa','w')
n=0
for nucleo_num1 in range (3,len(seq_list)-2,1):
	if seq_list[nucleo_num1]=='A' and seq_list[nucleo_num1+1]=='T' and seq_list[nucleo_num1+2]=='G' and seq_list[nucleo_num1+3]=='G':
		if seq_list[nucleo_num1-3]=='A' or seq_list[nucleo_num1-3]=='G':
			genelist=['A','T','G']
			for nucleo_num2 in range (nucleo_num1+3,len(seq_list),3):
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
				o1.write('>30.fa.txt--orf direct %s'%n+'  position%s'%(nucleo_num1+1)+'  length='+str(len(genelist))+'\n')
				for i in genelist:
					o1.write(i)
				o1.write('\n')


#####Now take the reverse strand into account.
n=0
for nucleo_num1 in range (len(seq_list)-4,2,-1):
	if seq_list[nucleo_num1]=='T' and seq_list[nucleo_num1-1]=='A' and seq_list[nucleo_num1-2]=='C' and seq_list[nucleo_num1-3]=='C':
		if seq_list[nucleo_num1+3]=='T' or seq_list[nucleo_num1+3]=='C':
			genelist=['A','T','G']
			for nucleo_num2 in range (nucleo_num1-3,-1,-3):
				if seq_list[nucleo_num2]=='A' and seq_list[nucleo_num2-1]=='T' and seq_list[nucleo_num2-2]=='T':
					break
				if seq_list[nucleo_num2]=='A' and seq_list[nucleo_num2-1]=='T' and seq_list[nucleo_num2-2]=='C':
					break
				if seq_list[nucleo_num2]=='A' and seq_list[nucleo_num2-1]=='C' and seq_list[nucleo_num2-2]=='T':
					break
				for revnucl in range (nucleo_num2, nucleo_num2-3, -1):
					if seq_list[revnucl]=='A':
						genelist.append('T')
					if seq_list[revnucl]=='T':
						genelist.append('A')
					if seq_list[revnucl]=='C':
						genelist.append('G')
					if seq_list[revnucl]=='G':
						genelist.append('C')
			if len(genelist)>100:##Set your minimum length for predicted ORFs.
				n+=1
				o1.write('>30.fa.txt--orf reverse%s'%n+'  position%s'%(nucleo_num1+1)+'  length='+str(len(genelist))+'\n')
				for i in genelist:
					o1.write(i)
				o1.write('\n')
o1.close()


#####Part 5: Translate the predicted orfs.
o2=open('30.pregenes.kozak100.0528.fa')#put the name of your newly created orf file here.
o3=open('30.preprotein.kozak100.0528','w')
i=0
for line in o2:
	i+=1
	#print (i)
	if line[0]=='>':
		o3.write(line)
	if line[0]!='>':
		line=line.strip()
		for nucl in range(0,len(line),3):
			#print (nucl)
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

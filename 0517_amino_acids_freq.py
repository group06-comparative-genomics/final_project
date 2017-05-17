#Amino acids in 03.protein.fa: {'P', 'E', 'N', 'K', 'G', 'H', 'A', 'M', 'I', 'V', 'C', 'F', 'X', 'L', 'T', 'S', 'W', 'Q', 'R', 'D', 'Y'}, total number 21

f1=open('03.protein.fa')

labels=set()

for line in f1:
	#print (line)
	if line[0]!='>':
		line=line.strip()
		for i in line:
			labels.add(i)
labels=list(labels)
number_of_aa=len(labels)
number_of_P=0
number_of_E=0
number_of_N=0
number_of_K=0
number_of_G=0
number_of_H=0
number_of_A=0
number_of_M=0
number_of_I=0
number_of_V=0
number_of_C=0
number_of_F=0
number_of_X=0
number_of_L=0
number_of_T=0
number_of_S=0
number_of_W=0
number_of_Q=0
number_of_R=0
number_of_D=0
number_of_Y=0
#print(labels)
f1.close()

f2=open('03.protein.fa')
ori_num=0
for line in f2:
	if line[0]!='>':
		line=line.strip()
		for i in line:
			if i=='P':
				number_of_P+=1
			elif i=='E':
				number_of_E+=1
			elif i=='N':
				number_of_N+=1
			elif i=='K':
				number_of_K+=1
			elif i=='G':
				number_of_G+=1
			elif i=='H':
				number_of_H+=1
			elif i=='A':
				number_of_A+=1
			elif i=='M':
				number_of_M+=1
			elif i=='I':
				number_of_I+=1
			elif i=='V':
				number_of_V+=1
			elif i=='C':
				number_of_C+=1
			elif i=='F':
				number_of_F+=1
			elif i=='X':
				number_of_X+=1
			elif i=='L':
				number_of_L+=1
			elif i=='T':
				number_of_T+=1
			elif i=='S':
				number_of_S+=1
			elif i=='W':
				number_of_W+=1
			elif i=='Q':
				number_of_Q+=1
			elif i=='R':
				number_of_R+=1
			elif i=='D':
				number_of_D+=1
			elif i=='Y':
				number_of_Y+=1
			ori_num+=1
#print (number_of_P,ori_num)
freq_P=float(number_of_P/ori_num)
freq_E=float(number_of_E/ori_num)
freq_N=float(number_of_N/ori_num)
freq_K=float(number_of_K/ori_num)
freq_G=float(number_of_G/ori_num)
freq_H=float(number_of_H/ori_num)
freq_A=float(number_of_A/ori_num)
freq_M=float(number_of_M/ori_num)
freq_I=float(number_of_I/ori_num)
freq_V=float(number_of_V/ori_num)
freq_C=float(number_of_C/ori_num)
freq_F=float(number_of_F/ori_num)
freq_X=float(number_of_X/ori_num)
freq_L=float(number_of_L/ori_num)
freq_T=float(number_of_T/ori_num)
freq_S=float(number_of_S/ori_num)
freq_W=float(number_of_W/ori_num)
freq_Q=float(number_of_Q/ori_num)
freq_R=float(number_of_R/ori_num)
freq_D=float(number_of_D/ori_num)
freq_Y=float(number_of_Y/ori_num)
print ('freq_P=',freq_P)
print ('freq_E=',freq_E)
print ('freq_N=',freq_N)
print ('freq_K=',freq_K)
print ('freq_G=',freq_G)
print ('freq_H=',freq_H)
print ('freq_A=',freq_A)
print ('freq_M=',freq_M)
print ('freq_I=',freq_I)
print ('freq_V=',freq_V)
print ('freq_C=',freq_C)
print ('freq_F=',freq_F)
print ('freq_X=',freq_X)
print ('freq_L=',freq_L)
print ('freq_T=',freq_T)
print ('freq_S=',freq_S)
print ('freq_W=',freq_W)
print ('freq_Q=',freq_Q)
print ('freq_R=',freq_R)
print ('freq_D=',freq_D)
print ('freq_Y=',freq_Y)

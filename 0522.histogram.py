import numpy as np
import matplotlib.pyplot as plt

f1=open('03.predictedgenes.100-1.0522.fa')
f2=open('03.longorf.glimmer.oneline')
len_list_predicted=[]
len_list_glimmer=[]
for line in f1:
	if line[0]=='>':
		line=line.strip()
		for i in range (0,len(line),1):
			if line[i] =='=':
				a=line[i+1:len(line)]
				len_list_predicted.append(int(a))
for line in f2:
	if line[0]=='>':
		line=line.strip()
		for i in range (0,len(line),1):
			if line[i] =='=':
				b=line[i+1:len(line)]
				len_list_glimmer.append(int(b))
#print (len_list_glimmer)
f1.close()
f2.close()

plt.xlabel('gene length')
plt.ylabel('frequency')
plt.legend(loc='upper right')
plt.hist(len_list_predicted,histtype='step',label='genes predicted by group 6')
plt.hist(len_list_glimmer,histtype='step',label='genes predicted by Glimmer')
plt.show()

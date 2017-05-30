#it counts the frequency of di-amino acids in proteomes file
def count_diaminoacid(proteomelist):
    single_aa = "ACDEFGHIKLMNPQRSTVWY"
    i = 0
    j = 0
    di_aa = []
    for i in range (0, 20):
        for j in range (0,20):
            di_aa.append(single_aa[i]+single_aa[j])
            j += 1
        i += 1
    print (di_aa)
    f = open(proteomelist, "r").readlines()

    di_aaFre = {}
    for item in di_aa:
        di_aaFre[item] = float(0)

    for line in f:
        frame = []
        if line[0] != ">":

            frame = []
            position = 0
            for nucleotide in line:
                frame.append(line[position:(position + 2)])
                position += 1
            print (frame)
            for k in range (len(di_aa)):
                for item in frame:
                    if item == di_aa[k]:
                        di_aaFre[str(di_aa[k])] += 1
    print (di_aaFre)

    all_aminoacids = 00
    for item in di_aaFre:
        all_aminoacids += di_aaFre[item]
    print (all_aminoacids)
    di_aaPercentage = {}
    for item in di_aaFre:
        di_aaPercentage[item]= di_aaFre[item]/float(all_aminoacids)
    print (di_aaPercentage)
count_diaminoacid("03.protein.fa")

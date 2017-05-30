#this program count the percentage of a single nucleotide in the genome
#A, T, C, G undefined nucleotide
# it is already proved that it contains "N" ONLY as undefined nucleotides other than ATCG


#count_N ("singleFasta")

def count_Stopcodon(proteome):
    f = open(proteome, "r").readlines()

    TAA = 0
    TAG = 0
    TGA = 0
    for line in f:
        line = line.rstrip()
        if line[0] != ">" and line.endswith("TAA"):
            TAA += 1
        elif line[0] != ">" and line.endswith("TAG"):
            TAG += 1
        elif line[0] != ">" and line.endswith("TGA"):
            TGA += 1

    all_Stopcondons = TAA + TAG + TGA

    percentage_TAA = float(TAA)/all_Stopcondons
    percentage_TAG = float(TAG)/all_Stopcondons
    percentage_TGA = float(TGA)/all_Stopcondons
    #print (percentage_TAA)


    return(percentage_TAA, percentage_TAG, percentage_TGA)
#count_Stopcodon("03.protein.fa")

def Distance(proteomelist):

    i = 0
    j = 0
    outsidelist1 = []


    while i <= 4:
        insidelist1 = []
        for j in range (0,5):
            Distance1 = (count_Stopcodon(proteomelist[i])[0]-count_Stopcodon(proteomelist[j])[0])**2 + (count_Stopcodon(proteomelist[i])[1]-count_Stopcodon(proteomelist[j])[1])**2 + (count_Stopcodon(proteomelist[i])[2]-count_Stopcodon(proteomelist[j])[2])**2
            Distance1 = Distance1 ** 0.5
            #print (Distance1)
            insidelist1.append(Distance1)

            j += 1
        i +=1
        outsidelist1.append(insidelist1)

    print (outsidelist1)
    return(outsidelist1)
    #print (outsidelist2)


proteomelist = ["03.protein.fa.withstop", "08.protein.fa.withstop", "09.protein.fa.withstop", "18.protein.fa.withstop","30.protein.fa.withstop"]
Distance(proteomelist)






